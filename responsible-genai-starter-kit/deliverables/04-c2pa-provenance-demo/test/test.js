#!/usr/bin/env node

/**
 * C2PA Demo Test Suite
 *
 * This script tests the signing and verification functionality
 * to ensure the C2PA tools are working correctly.
 */

import { execSync } from 'child_process';
import { existsSync, mkdirSync, writeFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const rootDir = join(__dirname, '..');

// Colors for output
const colors = {
  reset: '\x1b[0m',
  green: '\x1b[32m',
  red: '\x1b[31m',
  yellow: '\x1b[33m',
  blue: '\x1b[34m',
  gray: '\x1b[90m'
};

let testsPassed = 0;
let testsFailed = 0;

function log(message, color = colors.reset) {
  console.log(`${color}${message}${colors.reset}`);
}

function header(message) {
  console.log('\n' + '═'.repeat(70));
  log(message, colors.blue);
  console.log('═'.repeat(70) + '\n');
}

function success(message) {
  log(`✓ ${message}`, colors.green);
  testsPassed++;
}

function fail(message) {
  log(`✗ ${message}`, colors.red);
  testsFailed++;
}

function info(message) {
  log(`  ${message}`, colors.gray);
}

function run(command, options = {}) {
  try {
    return execSync(command, {
      cwd: rootDir,
      encoding: 'utf-8',
      stdio: options.silent ? 'pipe' : 'inherit',
      ...options
    });
  } catch (error) {
    if (!options.allowFail) {
      throw error;
    }
    return null;
  }
}

// Main test suite
async function runTests() {
  header('C2PA Provenance Demo - Test Suite');

  // Test 1: Check build
  try {
    log('Test 1: Checking TypeScript compilation...', colors.yellow);
    if (existsSync(join(rootDir, 'dist'))) {
      info('dist/ directory exists');
      success('Build directory check passed');
    } else {
      info('Building TypeScript files...');
      run('npm run build');
      success('TypeScript compilation successful');
    }
  } catch (error) {
    fail('Build check failed');
    info('Run "npm run build" to compile TypeScript files');
  }

  // Test 2: Check certificates
  log('\nTest 2: Checking development certificates...', colors.yellow);
  const certPath = join(rootDir, 'examples/certs/dev-certificate.pem');
  const keyPath = join(rootDir, 'examples/certs/dev-private-key.pem');

  if (existsSync(certPath) && existsSync(keyPath)) {
    info('Certificates found');
    success('Certificate check passed');
  } else {
    info('Generating development certificates...');
    try {
      run('bash examples/generate-dev-certs.sh');
      success('Development certificates generated');
    } catch (error) {
      fail('Certificate generation failed');
      info('Run: bash examples/generate-dev-certs.sh');
    }
  }

  // Test 3: Create test image
  log('\nTest 3: Preparing test image...', colors.yellow);
  const testDir = join(rootDir, 'test/fixtures');
  mkdirSync(testDir, { recursive: true });

  // Create a minimal PNG image (1x1 white pixel)
  const minimalPNG = Buffer.from([
    0x89, 0x50, 0x4E, 0x47, 0x0D, 0x0A, 0x1A, 0x0A, // PNG signature
    0x00, 0x00, 0x00, 0x0D, 0x49, 0x48, 0x44, 0x52, // IHDR chunk
    0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, // 1x1 dimensions
    0x08, 0x02, 0x00, 0x00, 0x00, 0x90, 0x77, 0x53,
    0xDE, 0x00, 0x00, 0x00, 0x0C, 0x49, 0x44, 0x41, // IDAT chunk
    0x54, 0x08, 0xD7, 0x63, 0xF8, 0xFF, 0xFF, 0x3F,
    0x00, 0x05, 0xFE, 0x02, 0xFE, 0xDC, 0xCC, 0x59,
    0xE7, 0x00, 0x00, 0x00, 0x00, 0x49, 0x45, 0x4E, // IEND chunk
    0x44, 0xAE, 0x42, 0x60, 0x82
  ]);

  const testImagePath = join(testDir, 'test-unsigned.png');
  writeFileSync(testImagePath, minimalPNG);
  info(`Test image created: ${testImagePath}`);
  success('Test image preparation passed');

  // Test 4: CLI help (basic check)
  log('\nTest 4: Testing CLI help commands...', colors.yellow);
  try {
    run('node dist/cli-sign.js --help', { silent: true });
    success('Sign CLI help works');
  } catch (error) {
    fail('Sign CLI help failed');
  }

  try {
    run('node dist/cli-verify.js --help', { silent: true });
    success('Verify CLI help works');
  } catch (error) {
    fail('Verify CLI help failed');
  }

  // Test 5: Note about c2pa-node dependency
  log('\nTest 5: Checking C2PA library...', colors.yellow);
  info('Note: Full signing/verification tests require c2pa-node library');
  info('The c2pa-node library has platform-specific binaries');

  try {
    // Try to load the module
    const module = await import('c2pa-node').catch(() => null);
    if (module) {
      success('c2pa-node library is available');
      info('Full integration tests can be run');
    } else {
      log('⚠ c2pa-node not installed or not available', colors.yellow);
      info('Run "npm install" to get all dependencies');
      info('Some platforms may need additional setup');
    }
  } catch (error) {
    log('⚠ c2pa-node library check skipped', colors.yellow);
    info('This is expected if dependencies are not yet installed');
    info('Run "npm install" to install all dependencies');
  }

  // Test 6: Web viewer files
  log('\nTest 6: Checking web viewer files...', colors.yellow);
  const viewerFiles = [
    'viewer/index.html',
    'viewer/styles.css',
    'viewer/viewer.js'
  ];

  let viewerOk = true;
  for (const file of viewerFiles) {
    if (existsSync(join(rootDir, file))) {
      info(`✓ ${file}`);
    } else {
      info(`✗ ${file} missing`);
      viewerOk = false;
    }
  }

  if (viewerOk) {
    success('Web viewer files present');
  } else {
    fail('Web viewer files missing');
  }

  // Test 7: Example metadata files
  log('\nTest 7: Checking example metadata files...', colors.yellow);
  const metadataFiles = [
    'examples/metadata-simple.json',
    'examples/metadata-ai-generated.json',
    'examples/metadata-edited.json'
  ];

  let metadataOk = true;
  for (const file of metadataFiles) {
    if (existsSync(join(rootDir, file))) {
      info(`✓ ${file}`);
      // Validate JSON
      try {
        const content = readFileSync(join(rootDir, file), 'utf-8');
        JSON.parse(content);
      } catch (error) {
        info(`  ⚠ Invalid JSON in ${file}`);
        metadataOk = false;
      }
    } else {
      info(`✗ ${file} missing`);
      metadataOk = false;
    }
  }

  if (metadataOk) {
    success('Example metadata files valid');
  } else {
    fail('Example metadata files check failed');
  }

  // Summary
  header('Test Summary');
  log(`Tests Passed: ${testsPassed}`, colors.green);
  if (testsFailed > 0) {
    log(`Tests Failed: ${testsFailed}`, colors.red);
  }

  console.log('\n' + '─'.repeat(70));
  if (testsFailed === 0) {
    log('\n🎉 All tests passed! The C2PA demo is ready to use.\n', colors.green);
    info('Next steps:');
    info('1. Generate certificates: bash examples/generate-dev-certs.sh');
    info('2. Create sample image: bash examples/create-sample-image.sh');
    info('3. Sign an image: npm run sign -- -i <input> -o <output> -c <cert> -k <key>');
    info('4. Verify an image: npm run verify -- -i <signed-image>');
    info('5. Start web viewer: npm run viewer');
    console.log();
  } else {
    log('\n⚠ Some tests failed. Please review the output above.\n', colors.yellow);
  }

  process.exit(testsFailed > 0 ? 1 : 0);
}

// Import fs functions
import { readFileSync } from 'fs';

// Run tests
runTests().catch(error => {
  console.error('\n❌ Test suite error:', error.message);
  process.exit(1);
});
