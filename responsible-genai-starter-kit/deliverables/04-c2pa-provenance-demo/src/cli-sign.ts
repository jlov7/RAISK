#!/usr/bin/env node

/**
 * C2PA Content Signing CLI
 *
 * This tool signs image files with C2PA manifests to establish content provenance.
 * Compliant with C2PA Technical Specification v2.2
 *
 * WARNING: This demo uses DEVELOPMENT KEYS ONLY
 * DO NOT USE IN PRODUCTION - Generate proper certificates for production use
 */

import { Command } from 'commander';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { createC2pa, ManifestBuilder, SigningAlgorithm } from 'c2pa-node';
import chalk from 'chalk';
import { basename } from 'path';

interface SignOptions {
  input: string;
  output: string;
  cert: string;
  key: string;
  metadata?: string;
  title?: string;
  author?: string;
  aiGenerated?: boolean;
}

async function signContent(options: SignOptions): Promise<void> {
  console.log(chalk.bold.blue('\nC2PA Content Signing Tool'));
  console.log(chalk.yellow('━'.repeat(60)));

  // Validate inputs
  if (!existsSync(options.input)) {
    console.error(chalk.red(`Error: Input file not found: ${options.input}`));
    process.exit(1);
  }

  if (!existsSync(options.cert)) {
    console.error(chalk.red(`Error: Certificate file not found: ${options.cert}`));
    process.exit(1);
  }

  if (!existsSync(options.key)) {
    console.error(chalk.red(`Error: Private key file not found: ${options.key}`));
    process.exit(1);
  }

  try {
    const c2pa = createC2pa();

    console.log(chalk.cyan(`\nReading input file: ${options.input}`));
    const inputBuffer = readFileSync(options.input);

    const cert = readFileSync(options.cert);
    const privateKey = readFileSync(options.key);

    const format = getFormatFromFilename(options.input);
    const manifestBuilder = new ManifestBuilder({
      claim_generator: 'C2PA Provenance Demo v0.1.0',
      format,
      title: options.title ?? basename(options.input),
    });

    const definition = manifestBuilder.definition;
    const assertions: any[] = definition.assertions ?? [];

    if (options.metadata && existsSync(options.metadata)) {
      console.log(chalk.cyan(`Loading metadata from: ${options.metadata}`));
      const customMetadata = JSON.parse(readFileSync(options.metadata, 'utf-8'));
      const { assertions: customAssertions, ...rest } = customMetadata;
      Object.assign(definition, rest);
      if (Array.isArray(customAssertions)) {
        assertions.push(...customAssertions);
      }
    }

    // Title assertion
    if (options.title) {
      assertions.push({
        label: 'stds.schema-org.CreativeWork',
        data: {
          '@context': 'https://schema.org',
          '@type': 'CreativeWork',
          name: options.title,
          author: options.author || 'Unknown'
        }
      });
    }

    // AI Generation assertion (C2PA v2.2)
    if (options.aiGenerated) {
      assertions.push({
        label: 'c2pa.ai-generative-training',
        data: {
          'c2pa.training': 'notAllowed',
          'c2pa.softwareAgent': {
            name: 'Example AI Generator',
            version: '1.0.0'
          }
        }
      });

      assertions.push({
        label: 'c2pa.actions',
        data: {
          actions: [{
            action: 'c2pa.created',
            softwareAgent: {
              name: 'Example AI Generator',
              version: '1.0.0'
            },
            when: new Date().toISOString()
          }]
        }
      });
    }

    definition.assertions = assertions;

    console.log(chalk.cyan('\nManifest summary:'));
    console.log(chalk.gray('  Claim Generator:'), definition.claim_generator);
    console.log(chalk.gray('  Format:'), definition.format);
    console.log(chalk.gray('  Assertions:'), definition.assertions?.length ?? 0);

    console.log(chalk.cyan('\nSigning content with C2PA manifest...'));

    const result = await c2pa.sign({
      manifest: manifestBuilder,
      asset: {
        buffer: inputBuffer,
        mimeType: format,
      },
      signer: {
        type: 'local',
        certificate: cert,
        privateKey,
        algorithm: SigningAlgorithm.PS256,
      },
    });

    const signedAsset = result.signedAsset;
    const signedBuffer = signedAsset.buffer;

    // Write output
    writeFileSync(options.output, signedBuffer);

    console.log(chalk.green('\n✓ Successfully signed content!'));
    console.log(chalk.gray('  Input:'), options.input);
    console.log(chalk.gray('  Output:'), options.output);
    console.log(chalk.gray('  Size:'), `${inputBuffer.length} → ${signedBuffer.length} bytes`);

    console.log(chalk.yellow('\n⚠ WARNING: This file is signed with DEVELOPMENT KEYS'));
    console.log(chalk.yellow('  DO NOT USE IN PRODUCTION'));

  } catch (error) {
    console.error(chalk.red('\n✗ Error signing content:'));
    console.error(chalk.red((error as Error).message));
    if (process.env.DEBUG) {
      console.error(error);
    }
    process.exit(1);
  }
}

function getFormatFromFilename(filename: string): string {
  const ext = filename.toLowerCase().split('.').pop();
  const formatMap: Record<string, string> = {
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'webp': 'image/webp',
    'mp4': 'video/mp4',
    'pdf': 'application/pdf'
  };
  return formatMap[ext || ''] || 'application/octet-stream';
}

// CLI setup
const program = new Command();

program
  .name('c2pa-sign')
  .description('Sign content with C2PA manifest (C2PA v2.2 compliant)')
  .version('0.1.0')
  .requiredOption('-i, --input <file>', 'Input file to sign')
  .requiredOption('-o, --output <file>', 'Output file with C2PA manifest')
  .requiredOption('-c, --cert <file>', 'Certificate file (PEM format)')
  .requiredOption('-k, --key <file>', 'Private key file (PEM format)')
  .option('-m, --metadata <file>', 'Custom metadata JSON file')
  .option('-t, --title <string>', 'Content title')
  .option('-a, --author <string>', 'Content author')
  .option('--ai-generated', 'Mark content as AI-generated')
  .action(async (options) => {
    await signContent(options);
  });

program.parse(process.argv);
