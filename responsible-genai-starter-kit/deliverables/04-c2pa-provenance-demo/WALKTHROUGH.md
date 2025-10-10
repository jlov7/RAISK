# C2PA Content Provenance Demo - Complete Walkthrough

## Overview

This demo provides a complete implementation of C2PA (Coalition for Content Provenance and Authenticity) content signing and verification, compliant with the **C2PA Technical Specification v2.2**.

The toolkit includes:
- TypeScript CLI tools for signing and verifying content
- Web-based manifest viewer
- Example metadata for various use cases
- Development certificate generation
- Comprehensive testing suite

**IMPORTANT SECURITY NOTICE:**
> This demo uses **DEVELOPMENT CERTIFICATES ONLY**. These are self-signed and suitable only for testing and learning. **NEVER use these certificates in production environments.** Production deployments must use certificates from trusted Certificate Authorities (CAs).

---

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Detailed Usage](#detailed-usage)
4. [C2PA v2.2 Compliance](#c2pa-v22-compliance)
5. [Security Considerations](#security-considerations)
6. [Troubleshooting](#troubleshooting)
7. [Production Deployment](#production-deployment)
8. [References](#references)

---

## Installation

### Prerequisites

- **Node.js** 18.0.0 or later
- **npm** or **yarn**
- **OpenSSL** 1.1.1+ (for certificate generation)
- **ImageMagick** (optional, for creating sample images)

### Step 1: Install Dependencies

```bash
cd deliverables/04-c2pa-provenance-demo
npm install
```

### Step 2: Build TypeScript Files

```bash
npm run build
```

This compiles the TypeScript source files in `src/` to JavaScript in `dist/`.

### Step 3: Generate Development Certificates

**WARNING:** These certificates are for development only!

```bash
bash examples/generate-dev-certs.sh
```

This creates:
- `examples/certs/dev-certificate.pem` - Public certificate
- `examples/certs/dev-private-key.pem` - Private key (KEEP SECURE)
- `examples/certs/README.txt` - Security warnings

### Step 4: Create Sample Images (Optional)

```bash
bash examples/create-sample-image.sh
```

Or add your own images to `examples/images/`.

### Step 5: Run Tests

```bash
npm test
```

This validates that all components are working correctly.

---

## Quick Start

### Sign an Image

```bash
npm run sign -- \
  -i examples/images/sample-unsigned.jpg \
  -o examples/images/sample-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --title "My Test Image" \
  --author "Demo User" \
  --ai-generated
```

### Verify a Signed Image

```bash
npm run verify -- \
  -i examples/images/sample-signed.jpg \
  --detailed
```

### View in Browser

```bash
npm run viewer
```

Then open `http://localhost:8080` and drag-and-drop your signed image.

---

## Detailed Usage

### CLI Signing Tool

The signing tool (`cli-sign.ts`) adds C2PA manifests to content files.

#### Basic Signing

```bash
node dist/cli-sign.js \
  --input <input-file> \
  --output <output-file> \
  --cert <certificate.pem> \
  --key <private-key.pem>
```

#### Options

| Option | Description | Required |
|--------|-------------|----------|
| `-i, --input <file>` | Input file to sign | Yes |
| `-o, --output <file>` | Output file with C2PA manifest | Yes |
| `-c, --cert <file>` | Certificate file (PEM format) | Yes |
| `-k, --key <file>` | Private key file (PEM format) | Yes |
| `-m, --metadata <file>` | Custom metadata JSON file | No |
| `-t, --title <string>` | Content title | No |
| `-a, --author <string>` | Content author | No |
| `--ai-generated` | Mark content as AI-generated | No |

#### Examples

**Sign with basic metadata:**
```bash
npm run sign -- \
  -i photo.jpg \
  -o photo-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --title "Sunset Photo" \
  --author "Jane Smith"
```

**Sign AI-generated content:**
```bash
npm run sign -- \
  -i ai-image.png \
  -o ai-image-signed.png \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --ai-generated \
  --title "AI-Generated Landscape" \
  --author "AI Generator v2.0"
```

**Sign with custom metadata:**
```bash
npm run sign -- \
  -i image.jpg \
  -o image-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  -m examples/metadata-ai-generated.json
```

### CLI Verification Tool

The verification tool (`cli-verify.ts`) reads and validates C2PA manifests.

#### Basic Verification

```bash
node dist/cli-verify.js \
  --input <signed-file>
```

#### Options

| Option | Description | Required |
|--------|-------------|----------|
| `-i, --input <file>` | Input file to verify | Yes |
| `-o, --output <file>` | Save manifest to JSON file | No |
| `-d, --detailed` | Show detailed assertion data | No |

#### Examples

**Verify and display summary:**
```bash
npm run verify -- -i photo-signed.jpg
```

**Verify with detailed output:**
```bash
npm run verify -- -i photo-signed.jpg --detailed
```

**Verify and save manifest:**
```bash
npm run verify -- \
  -i photo-signed.jpg \
  -o manifest-output.json \
  --detailed
```

### Web Viewer

The web viewer provides a browser-based interface for inspecting C2PA manifests.

#### Start the Viewer

```bash
npm run viewer
```

Opens a local server at `http://localhost:8080`.

#### Using the Viewer

1. Open `http://localhost:8080` in your browser
2. Drag and drop a signed image, or click to select a file
3. View the manifest information across four tabs:
   - **Summary**: Key metadata and validation status
   - **Assertions**: Detailed claims about the content
   - **Signature**: Certificate and signing information
   - **Raw JSON**: Complete manifest data structure

#### Viewer Features

- Drag-and-drop file upload
- Visual display of content with manifest
- Detection of AI-generated content
- Formatted display of assertions and metadata
- Export manifest data to JSON
- Offline operation (no external dependencies)

### Custom Metadata Files

Three example metadata files are provided in `examples/`:

#### 1. Simple Metadata (`metadata-simple.json`)

Basic signing with minimal metadata:
- Title and author
- Creation timestamp
- Simple action assertion

Use case: Basic content authentication

#### 2. AI-Generated Metadata (`metadata-ai-generated.json`)

Comprehensive AI content metadata:
- AI software agent information
- Training data restrictions (CAWG `cawg.ai_generative_training: notAllowed`)
- Generation parameters (prompt, seed, steps)
- Model information

Use case: AI-generated images, compliant with C2PA v2.2 + CAWG 1.1 assertions

**Note**: C2PA v2.2 removed the training/mining assertion from core spec. The Creator Assertions Working Group (CAWG) 1.1 specification (May 2025, DIF-ratified) defines the replacement `cawg.training-mining` assertion with `cawg.*` entry keys.

#### 3. Edited Content Metadata (`metadata-edited.json`)

Content with edit history:
- Multiple actions (opened, adjusted, filtered)
- EXIF camera metadata
- Ingredients (original source files)
- Edit parameters

Use case: Photographs edited with professional tools

#### Creating Custom Metadata

Create a JSON file with the following structure:

```json
{
  "title": "Your Content Title",
  "claim_generator": "C2PA Provenance Demo v0.1.0",
  "format": "image/jpeg",
  "assertions": [
    {
      "label": "stds.schema-org.CreativeWork",
      "data": {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": "Your content name",
        "author": "Author name"
      }
    },
    {
      "label": "c2pa.actions",
      "data": {
        "actions": [
          {
            "action": "c2pa.created",
            "when": "2025-01-15T10:00:00Z"
          }
        ]
      }
    }
  ]
}
```

Then sign with:
```bash
npm run sign -- -i input.jpg -o output.jpg -c cert.pem -k key.pem -m custom-metadata.json
```

---

## C2PA v2.2 Compliance

This implementation follows the [C2PA Technical Specification v2.2](https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html).

### Key Compliance Features

#### 1. Manifest Structure
- ✅ JUMBF-based manifest store
- ✅ Claim generator identification
- ✅ Content binding with hashes
- ✅ Signature validation

#### 2. Assertions (C2PA v2.2)
- ✅ `stds.schema-org.CreativeWork` - Dublin Core metadata
- ✅ `c2pa.actions` - Content history and edits
- ✅ `c2pa.hash.data` - Content integrity
- ✅ `stds.exif` - Camera/device metadata

#### 3. AI Content Assertions (CAWG 1.1, May 2025)
- ✅ `cawg.training-mining` assertion with entry keys:
  - `cawg.ai_generative_training` (`allowed`, `notAllowed`, `constrained`)
  - `cawg.ai_training` - AI model training permissions
  - `cawg.data_mining` - Data mining permissions
  - `cawg.ai_inference` - AI inference permissions
- ✅ Software agent identification
- ✅ Model information
- ✅ Generation parameters

**Important**: C2PA v2.2 (May 2025) removed the training/mining assertion from core spec. CAWG 1.1 is the DIF-ratified replacement defined by the Creator Assertions Working Group.

#### 4. Signature Requirements
- ✅ PS256 (RSA-PSS with SHA-256) algorithm
- ✅ X.509 certificate embedding
- ✅ Timestamping support
- ✅ Hard binding to content

#### 5. Supported Formats
- ✅ JPEG (`image/jpeg`)
- ✅ PNG (`image/png`)
- ✅ WebP (`image/webp`)
- ⚠️ MP4, PDF (supported by c2pa-node library)

### Specification Sections Implemented

| Section | Feature | Status |
|---------|---------|--------|
| 5.2 | Manifest Store | ✅ Implemented |
| 5.3 | Claims | ✅ Implemented |
| 5.4 | Assertions | ✅ Implemented |
| 5.5 | Ingredients | ✅ Supported |
| 6.1 | Signature Validation | ✅ Implemented |
| 7.2 | AI Assertions | ✅ Implemented (v2.2) |
| 8.1 | Hard Bindings | ✅ Implemented |

---

## Security Considerations

### Development vs. Production

#### Development Certificates (This Demo)
- ✅ Self-signed
- ✅ No password protection
- ✅ 1-year validity
- ✅ Suitable for testing only
- ❌ **NOT trusted by validators**
- ❌ **NOT suitable for production**

#### Production Certificates (Required for Real Use)
- Certificate from trusted CA (e.g., DigiCert, GlobalSign)
- Hardware Security Module (HSM) for key storage
- Password-protected private keys
- Key rotation policies
- Certificate revocation support
- Extended validation (EV) certificates recommended

### Key Management Best Practices

1. **Never commit private keys to version control**
   - Add `*.pem` to `.gitignore`
   - Use environment variables or secrets management
   - Rotate keys regularly

2. **Protect private keys**
   - Use file permissions (`chmod 600`)
   - Encrypt at rest
   - Store in HSM for production

3. **Certificate validation**
   - Verify certificate chain
   - Check revocation status (CRL/OCSP)
   - Validate expiration dates

4. **Audit and monitoring**
   - Log all signing operations
   - Monitor for unauthorized access
   - Implement key usage policies

### Threat Model

This demo implementation does NOT protect against:
- ❌ Certificate authority compromise
- ❌ Private key theft (keys are unencrypted)
- ❌ Time-of-check to time-of-use attacks
- ❌ Malicious certificate issuance
- ❌ Advanced persistent threats (APTs)

Production systems should implement:
- ✅ HSM-backed key storage
- ✅ Multi-signature requirements
- ✅ Certificate pinning
- ✅ Regular security audits
- ✅ Incident response procedures

---

## Troubleshooting

### Build Issues

**Error: `tsc: command not found`**
```bash
npm install
npm run build
```

**Error: TypeScript compilation errors**
- Check Node.js version: `node --version` (requires 18+)
- Clean and rebuild: `npm run clean && npm run build`

### Certificate Issues

**Error: `Certificate file not found`**
```bash
bash examples/generate-dev-certs.sh
```

**Error: `OpenSSL not found`**
- macOS: `brew install openssl`
- Linux: `apt-get install openssl` or `yum install openssl`
- Windows: Install from [OpenSSL website](https://www.openssl.org/)

### Signing Issues

**Error: `c2pa-node module not found`**
```bash
npm install c2pa-node
```

**Note:** `c2pa-node` has platform-specific binaries. Some platforms may require additional setup or may not be supported. Check the [c2pa-node documentation](https://www.npmjs.com/package/c2pa-node).

**Error: `Invalid manifest format`**
- Validate JSON syntax: `node -e "console.log(JSON.parse(require('fs').readFileSync('metadata.json')))"`
- Check assertion labels match C2PA spec
- Ensure required fields are present

### Verification Issues

**Warning: `No C2PA manifest found`**
- File may not be signed
- File may have been re-encoded (strips manifest)
- File format may not support C2PA

**Error: `Signature validation failed`**
- Development certificates are not trusted by default
- Certificate may be expired
- Manifest may be corrupted

### Web Viewer Issues

**Error: `Cannot access localhost:8080`**
- Check if port is in use: `lsof -i :8080`
- Try different port: `npx serve viewer -p 8081`

**Error: Manifest not displaying**
- Check browser console for errors
- Ensure file is properly signed
- Try with a known-good test file

---

## Production Deployment

### Obtaining Production Certificates

1. **Choose a Certificate Authority**
   - C2PA Certified CAs (see [c2pa.org/certification](https://c2pa.org/certification/))
   - Standard code signing CAs (DigiCert, GlobalSign, etc.)

2. **Generate Certificate Signing Request (CSR)**
   ```bash
   openssl req -new -newkey rsa:2048 -nodes \
     -keyout production-key.pem \
     -out production-csr.pem \
     -subj "/C=US/ST=State/L=City/O=Company/CN=signing.example.com"
   ```

3. **Submit CSR to CA**
   - Complete identity verification
   - Receive signed certificate
   - Configure certificate chain

4. **Store Keys Securely**
   - Use HSM (AWS CloudHSM, Azure Key Vault, etc.)
   - Implement access controls
   - Enable audit logging

### Integration Checklist

- [ ] Replace development certificates with production certificates
- [ ] Implement HSM-backed key storage
- [ ] Configure certificate chain validation
- [ ] Set up certificate revocation checking (OCSP/CRL)
- [ ] Implement key rotation procedures
- [ ] Add audit logging for all signing operations
- [ ] Set up monitoring and alerting
- [ ] Conduct security review and penetration testing
- [ ] Document incident response procedures
- [ ] Train operators on security procedures

### Recommended Architecture

```
┌─────────────────┐
│   Application   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  C2PA Signing   │
│     Service     │ ← API Gateway
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Key Management │
│   Service (HSM) │ ← Hardware Security
└─────────────────┘
         │
         ▼
┌─────────────────┐
│   Audit Logs    │
└─────────────────┘
```

### Performance Considerations

- **Signing time**: ~100-500ms per image (depends on size and complexity)
- **File size increase**: ~1-10KB for manifest data
- **Batch signing**: Process multiple files in parallel
- **Caching**: Cache certificate chains and validation results

---

## References

### C2PA Specifications

- **C2PA Technical Specification v2.2**
  https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html

- **C2PA Specification PDF**
  https://spec.c2pa.org/specifications/specifications/2.2/specs/_attachments/C2PA_Specification.pdf

### SDKs and Tools

- **c2pa-node** (Node.js library)
  https://www.npmjs.com/package/c2pa-node

- **Content Authenticity Initiative (CAI) JavaScript SDK**
  https://opensource.contentauthenticity.org/docs/js-sdk/getting-started/overview/

- **C2PA Open Source Tools**
  https://github.com/contentauth

### Standards

- **ISO/IEC 21320-1:2015** - JUMBF (JPEG Universal Metadata Box Format)
- **ISO/IEC 14496-12** - ISO Base Media File Format
- **IETF RFC 5652** - Cryptographic Message Syntax (CMS)

### Community

- **C2PA Official Website**
  https://c2pa.org/

- **C2PA Certification Program**
  https://c2pa.org/certification/

- **Content Authenticity Initiative**
  https://contentauthenticity.org/

---

## Appendix: File Structure

```
04-c2pa-provenance-demo/
├── package.json                 # Dependencies and scripts
├── tsconfig.json               # TypeScript configuration
├── WALKTHROUGH.md              # This file
├── src/
│   ├── cli-sign.ts             # Signing CLI tool
│   └── cli-verify.ts           # Verification CLI tool
├── dist/                       # Compiled JavaScript (generated)
│   ├── cli-sign.js
│   └── cli-verify.js
├── viewer/
│   ├── index.html              # Web viewer interface
│   ├── styles.css              # Viewer styles
│   └── viewer.js               # Viewer logic
├── examples/
│   ├── generate-dev-certs.sh   # Certificate generation script
│   ├── create-sample-image.sh  # Sample image creation
│   ├── metadata-simple.json    # Example: Simple metadata
│   ├── metadata-ai-generated.json  # Example: AI content
│   ├── metadata-edited.json    # Example: Edited content
│   ├── certs/                  # Development certificates (generated)
│   │   ├── dev-certificate.pem
│   │   ├── dev-private-key.pem
│   │   └── README.txt
│   └── images/                 # Sample images
│       └── README.txt
└── test/
    ├── test.js                 # Test suite
    └── fixtures/               # Test files (generated)
```

---

## License

This demo is part of the Responsible GenAI Starter Kit.

**Libraries Used:**
- `c2pa-node` - Apache 2.0 License
- `commander` - MIT License
- `chalk` - MIT License
- `typescript` - Apache 2.0 License

---

## Support

For questions or issues:
1. Review this walkthrough
2. Check the [C2PA specification](https://c2pa.org/specifications/)
3. Consult the [c2pa-node documentation](https://www.npmjs.com/package/c2pa-node)
4. Review the Responsible GenAI Starter Kit documentation

---

**Document Version:** 0.1.0
**Last Updated:** January 2025
**C2PA Specification Version:** 2.2
**Compliant with:** NIST AI 600-1 (Information Integrity)
