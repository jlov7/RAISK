#!/usr/bin/env node

/**
 * C2PA Content Verification CLI
 *
 * This tool verifies C2PA manifests and displays content provenance information.
 * Compliant with C2PA Technical Specification v2.2
 */

import { Command } from 'commander';
import { readFileSync, existsSync, writeFileSync } from 'fs';
import { createC2pa } from 'c2pa-node';
import chalk from 'chalk';

interface VerifyOptions {
  input: string;
  output?: string;
  detailed?: boolean;
}

async function verifyContent(options: VerifyOptions): Promise<void> {
  console.log(chalk.bold.blue('\nC2PA Content Verification Tool'));
  console.log(chalk.yellow('━'.repeat(60)));

  // Validate input
  if (!existsSync(options.input)) {
    console.error(chalk.red(`Error: Input file not found: ${options.input}`));
    process.exit(1);
  }

  try {
    const c2pa = createC2pa();

    console.log(chalk.cyan(`\nReading file: ${options.input}`));
    const inputBuffer = readFileSync(options.input);

    console.log(chalk.cyan('Verifying C2PA manifest...\n'));

    const manifestStore = await c2pa.read({
      buffer: inputBuffer,
      mimeType: getFormatFromFilename(options.input)
    });

    if (!manifestStore) {
      console.log(chalk.yellow('⚠ No C2PA manifest found in this file'));
      console.log(chalk.gray('  This file may not be signed with C2PA'));
      return;
    }

    // Display verification results
    displayVerificationResults(manifestStore, options.detailed);

    // Save to JSON if requested
    if (options.output) {
      const outputData = {
        file: options.input,
        verifiedAt: new Date().toISOString(),
        manifestStore,
        validationStatus: manifestStore.validation_status ?? []
      };

      writeFileSync(options.output, JSON.stringify(outputData, null, 2));
      console.log(chalk.green(`\n✓ Manifest data saved to: ${options.output}`));
    }

  } catch (error) {
    console.error(chalk.red('\n✗ Error verifying content:'));
    console.error(chalk.red((error as Error).message));
    if (process.env.DEBUG) {
      console.error(error);
    }
    process.exit(1);
  }
}

function displayVerificationResults(manifestStore: any, detailed?: boolean): void {
  const validationStatus = manifestStore?.validation_status ?? [];

  if (validationStatus.length > 0) {
    console.log(chalk.bold('Validation Status:'));
    validationStatus.forEach((status: any) => {
      const icon = status.code === 'valid' ? chalk.green('✓') : chalk.red('✗');
      console.log(`  ${icon} ${status.code}: ${status.explanation || 'No details'}`);
    });
    console.log();
  }

  const activeManifest = manifestStore?.active_manifest;

  if (!activeManifest) {
    console.log(chalk.yellow('⚠ No active manifest found'));
    return;
  }

  console.log(chalk.bold('Active Manifest:'));
  console.log(chalk.gray('  Label:'), activeManifest.label || 'Unknown');

  if (activeManifest.claim_generator) {
    console.log(chalk.gray('  Claim Generator:'), activeManifest.claim_generator);
  }

  if (activeManifest.title) {
    console.log(chalk.gray('  Title:'), activeManifest.title);
  }

  if (activeManifest.format) {
    console.log(chalk.gray('  Format:'), activeManifest.format);
  }

  // Signature info
  if (activeManifest.signature_info) {
    const signatureInfo = activeManifest.signature_info;
    console.log(chalk.gray('\n  Signature Algorithm:'), signatureInfo.alg || 'Unknown');
    if (signatureInfo.issuer) {
      console.log(chalk.gray('  Issuer:'), signatureInfo.issuer);
    }
    if (signatureInfo.time) {
      console.log(chalk.gray('  Signed At:'), new Date(signatureInfo.time).toLocaleString());
    }
  }

  // Assertions
  if (activeManifest.assertions && activeManifest.assertions.length > 0) {
    console.log(chalk.bold('\nAssertions:'));
    activeManifest.assertions.forEach((assertion: any, index: number) => {
      console.log(chalk.cyan(`  ${index + 1}. ${assertion.label}`));

      if (detailed && assertion.data) {
        console.log(chalk.gray('     Data:'), JSON.stringify(assertion.data, null, 6).split('\n').join('\n     '));
      }
    });
  }

  // Ingredients (for edited content)
  if (activeManifest.ingredients && activeManifest.ingredients.length > 0) {
    console.log(chalk.bold('\nIngredients (Content History):'));
    activeManifest.ingredients.forEach((ingredient: any, index: number) => {
      console.log(chalk.cyan(`  ${index + 1}. ${ingredient.title || ingredient.document_id || 'Unknown'}`));
      if (ingredient.format) {
        console.log(chalk.gray('     Format:'), ingredient.format);
      }
      if (ingredient.relationship) {
        console.log(chalk.gray('     Relationship:'), ingredient.relationship);
      }
    });
  }

  // AI Generation info
  const aiAssertion = activeManifest.assertions?.find(
    (a: any) => a.label?.includes('ai-generative') || a.label?.includes('c2pa.training')
  );

  if (aiAssertion) {
    console.log(chalk.bold.magenta('\n🤖 AI-Generated Content Detected'));
    if (aiAssertion.data?.['c2pa.training']) {
      console.log(chalk.gray('  Training Use:'), aiAssertion.data['c2pa.training']);
    }
    if (aiAssertion.data?.['c2pa.softwareAgent']) {
      const agent = aiAssertion.data['c2pa.softwareAgent'];
      console.log(chalk.gray('  AI Tool:'), `${agent.name || 'Unknown'} ${agent.version || ''}`);
    }
  }

  console.log(chalk.green('\n✓ Verification complete'));
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
  .name('c2pa-verify')
  .description('Verify C2PA manifest and display provenance information (C2PA v2.2 compliant)')
  .version('0.1.0')
  .requiredOption('-i, --input <file>', 'Input file to verify')
  .option('-o, --output <file>', 'Save manifest to JSON file')
  .option('-d, --detailed', 'Show detailed assertion data')
  .action(async (options) => {
    await verifyContent(options);
  });

program.parse(process.argv);
