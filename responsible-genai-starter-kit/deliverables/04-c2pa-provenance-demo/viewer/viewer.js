import {
  createC2pa,
  selectGenerativeInfo,
  selectGenerativeSoftwareAgents,
  selectGenerativeType,
  selectDoNotTrain,
} from './vendor/c2pa.esm.min.js';

let c2paInstance = null;

async function ensureC2paInstance() {
  if (c2paInstance) {
    return c2paInstance;
  }

  c2paInstance = await createC2pa({
    wasmSrc: new URL('./vendor/toolkit_bg.wasm', import.meta.url).toString(),
    workerSrc: new URL('./vendor/c2pa.worker.min.js', import.meta.url).toString(),
  });
  return c2paInstance;
}

// UI Elements
const uploadBox = document.getElementById('uploadBox');
const fileInput = document.getElementById('fileInput');
const selectButton = document.getElementById('selectButton');
const previewSection = document.getElementById('previewSection');
const previewImage = document.getElementById('previewImage');
const resultsSection = document.getElementById('resultsSection');
const noManifest = document.getElementById('noManifest');
const errorSection = document.getElementById('errorSection');
const errorMessage = document.getElementById('errorMessage');
const summaryContent = document.getElementById('summaryContent');
const assertionsContent = document.getElementById('assertionsContent');
const signatureContent = document.getElementById('signatureContent');
const rawContent = document.getElementById('rawContent');

// Tab switching
const tabs = document.querySelectorAll('.tab');
const tabPanes = document.querySelectorAll('.tab-pane');

tabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const targetTab = tab.dataset.tab;

    tabs.forEach((t) => t.classList.remove('active'));
    tab.classList.add('active');

    tabPanes.forEach((pane) => pane.classList.remove('active'));
    document.getElementById(targetTab).classList.add('active');
  });
});

// File selection
selectButton.addEventListener('click', () => {
  fileInput.click();
});

fileInput.addEventListener('change', (event) => {
  const file = event.target.files?.[0];
  if (file) {
    void handleFile(file);
  }
});

// Drag and drop
uploadBox.addEventListener('dragover', (event) => {
  event.preventDefault();
  uploadBox.classList.add('dragover');
});

uploadBox.addEventListener('dragleave', () => {
  uploadBox.classList.remove('dragover');
});

uploadBox.addEventListener('drop', (event) => {
  event.preventDefault();
  uploadBox.classList.remove('dragover');

  const file = event.dataTransfer?.files?.[0];
  if (file && file.type.startsWith('image/')) {
    void handleFile(file);
  } else {
    showError('Please drop an image file (JPEG, PNG, or WebP)');
  }
});

async function handleFile(file) {
  hideAllSections();

  const reader = new FileReader();
  reader.onload = (event) => {
    previewImage.src = event.target?.result ?? '';
    previewSection.style.display = 'block';
  };
  reader.readAsDataURL(file);

  try {
    const c2pa = await ensureC2paInstance();
    const result = await c2pa.read(file);
    const manifestStore = result.manifestStore;

    if (!manifestStore || !manifestStore.activeManifest) {
      noManifest.style.display = 'block';
      return;
    }

    displayManifest(manifestStore, file);
  } catch (error) {
    console.error(error);
    showError(`Error verifying C2PA manifest: ${(error && error.message) || error}`);
  }
}

function displayManifest(manifestStore, file) {
  const manifest = manifestStore.activeManifest;
  resultsSection.style.display = 'block';

  summaryContent.innerHTML = buildSummary(manifestStore, manifest, file);
  assertionsContent.innerHTML = buildAssertions(manifest);
  signatureContent.innerHTML = buildSignature(manifest);

  const rawSnapshot = {
    validationStatus: manifestStore.validationStatus,
    manifest: {
      label: manifest.label,
      title: manifest.title,
      format: manifest.format,
      claimGenerator: manifest.claimGenerator,
      signatureInfo: manifest.signatureInfo,
      ingredients: manifest.ingredients,
      assertions: manifest.assertions.data,
    },
  };
  rawContent.textContent = JSON.stringify(rawSnapshot, null, 2);
}

function buildSummary(manifestStore, manifest, file) {
  const parts = [];
  parts.push(
    '<div class="info-box success"><h3>✓ C2PA Manifest Found</h3><p>This content contains verifiable provenance information.</p></div>'
  );

  parts.push('<div class="summary-grid">');
  parts.push(summaryRow('Filename', escapeHtml(file.name)));
  parts.push(summaryRow('Format', escapeHtml(manifest.format || file.type)));
  if (manifest.title) {
    parts.push(summaryRow('Title', escapeHtml(manifest.title)));
  }
  if (manifest.claimGenerator) {
    parts.push(summaryRow('Claim Generator', escapeHtml(manifest.claimGenerator)));
  }

  const validationItems = manifestStore.validationStatus?.map((status) => {
    const icon = status.code === 'valid' ? '✅' : status.code === 'skipped' ? '⚠️' : '❌';
    return `<li>${icon} ${escapeHtml(status.code)} – ${escapeHtml(status.explanation ?? 'See manifest for details')}</li>`;
  });
  if (validationItems?.length) {
    parts.push(
      `<div class="summary-row"><div class="data-label">Validation</div><div class="data-value"><ul class="unstyled">${validationItems.join(
        ''
      )}</ul></div></div>`
    );
  }

  const generativeInfo = selectGenerativeInfo(manifest) || [];
  if (generativeInfo.length) {
    const agents = selectGenerativeSoftwareAgents(generativeInfo).join(', ');
    const type = selectGenerativeType(generativeInfo);
    parts.push(
      summaryRow(
        'AI Generation',
        `${escapeHtml(type)}${agents ? `<br><small class="muted">${escapeHtml(agents)}</small>` : ''}`
      )
    );
  }

  if (selectDoNotTrain(manifest)) {
    parts.push(summaryRow('Training Restrictions', 'Do Not Train')); 
  }

  if (manifest.ingredients?.length) {
    const ingredientsHtml = manifest.ingredients
      .map((ingredient, index) => {
        const name = ingredient.title || ingredient.documentId || `Ingredient ${index + 1}`;
        return `<li>${escapeHtml(name)}${ingredient.format ? ` <span class="muted">(${escapeHtml(ingredient.format)})</span>` : ''}</li>`;
      })
      .join('');
    parts.push(
      `<div class="summary-row"><div class="data-label">Ingredients</div><div class="data-value"><ul class="unstyled">${ingredientsHtml}</ul></div></div>`
    );
  }

  parts.push('</div>');
  return parts.join('');
}

function buildAssertions(manifest) {
  const assertions = manifest.assertions?.data ?? [];
  if (!assertions.length) {
    return '<p class="muted">No assertions found in this manifest.</p>';
  }

  return assertions
    .map((assertion, index) => {
      const label = escapeHtml(assertion.label);
      const body = escapeHtml(JSON.stringify(assertion.data, null, 2));
      return `
        <details ${index === 0 ? 'open' : ''}>
          <summary>${label}</summary>
          <pre>${body}</pre>
        </details>
      `;
    })
    .join('');
}

function buildSignature(manifest) {
  const info = manifest.signatureInfo;
  if (!info) {
    return '<p class="muted">No signature information available.</p>';
  }

  const items = [];
  if (info.alg) {
    items.push(summaryRow('Algorithm', escapeHtml(info.alg)));
  }
  if (info.issuer) {
    items.push(summaryRow('Issuer', escapeHtml(info.issuer)));
  }
  if (info.time) {
    const formatted = new Date(info.time).toLocaleString();
    items.push(summaryRow('Signed At', escapeHtml(formatted)));
  }

  return `<div class="summary-grid">${items.join('')}</div>`;
}

function summaryRow(label, value) {
  return `
    <div class="summary-row">
      <div class="data-label">${escapeHtml(label)}</div>
      <div class="data-value">${value}</div>
    </div>
  `;
}

function hideAllSections() {
  previewSection.style.display = 'none';
  resultsSection.style.display = 'none';
  noManifest.style.display = 'none';
  errorSection.style.display = 'none';
}

function showError(message) {
  hideAllSections();
  errorMessage.textContent = message;
  errorSection.style.display = 'block';
}

function escapeHtml(value) {
  if (value === undefined || value === null) {
    return '';
  }
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}
