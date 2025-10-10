#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

const projectRoot = path.resolve(__dirname, '..');
const vendorDir = path.join(projectRoot, 'viewer', 'vendor');
const moduleRoot = path.join(projectRoot, 'node_modules', 'c2pa', 'dist');

const assets = [
  { source: path.join(moduleRoot, 'c2pa.esm.min.js'), target: path.join(vendorDir, 'c2pa.esm.min.js') },
  { source: path.join(moduleRoot, 'c2pa.worker.min.js'), target: path.join(vendorDir, 'c2pa.worker.min.js') },
  { source: path.join(moduleRoot, 'assets', 'wasm', 'toolkit_bg.wasm'), target: path.join(vendorDir, 'toolkit_bg.wasm') },
];

function copyAsset({ source, target }) {
  if (!fs.existsSync(source)) {
    throw new Error(`Expected asset not found: ${source}`);
  }

  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.copyFileSync(source, target);
}

function main() {
  try {
    assets.forEach(copyAsset);
    console.log('[c2pa-viewer] Copied browser assets to viewer/vendor');
  } catch (error) {
    console.error('[c2pa-viewer] Failed to copy viewer assets:', error.message);
    process.exit(1);
  }
}

main();
