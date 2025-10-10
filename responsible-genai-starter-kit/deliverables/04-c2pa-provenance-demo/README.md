# C2PA Content Provenance Demo

> **Compliant with C2PA Technical Specification v2.2**

A complete demonstration of C2PA (Coalition for Content Provenance and Authenticity) content signing and verification for AI-generated content and digital media.

## What is C2PA?

C2PA provides a standard for establishing the provenance and authenticity of digital content. It enables creators, editors, and consumers to trace the origin and history of digital media, including:

- **Who** created or edited the content
- **When** it was created or modified
- **How** it was created (e.g., AI-generated, photographed, edited)
- **What** tools and processes were used

This is critical for:
- Combating misinformation and deepfakes
- Protecting intellectual property
- Establishing content authenticity
- Meeting regulatory requirements (e.g., AI transparency)

## Features

- **CLI Signing Tool**: Sign images with C2PA manifests
- **CLI Verification Tool**: Verify and inspect C2PA manifests
- **Web Viewer**: Browser-based manifest inspection powered by the CAI c2pa SDK
- **AI Content Support**: C2PA v2.2 AI assertions for generative content
- **Example Metadata**: Pre-built templates for common use cases
- **Development Certificates**: Quick-start certificate generation
- **Comprehensive Tests**: Automated test suite

## Quick Start

```bash
# Install dependencies
npm install

# Build TypeScript
npm run build

# Generate development certificates
bash examples/generate-dev-certs.sh

# Sign an image
npm run sign -- \
  -i examples/images/photo.jpg \
  -o examples/images/photo-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --title "My Photo" \
  --ai-generated

# Verify the signed image
npm run verify -- -i examples/images/photo-signed.jpg --detailed

# Open web viewer
npm run viewer
```

> **Note:** `npm install` automatically copies the CAI browser SDK (wasm + worker) into `viewer/vendor/` so the manifest viewer can verify real C2PA metadata offline.

## Documentation

See **[WALKTHROUGH.md](./WALKTHROUGH.md)** for complete documentation including:
- Installation and setup
- Detailed usage examples
- C2PA v2.2 compliance details
- Security considerations
- Production deployment guide
- Troubleshooting

## Security Warning

**⚠ DEVELOPMENT DEMO ONLY ⚠**

This demo uses self-signed development certificates that are **NOT suitable for production use**.

For production deployments:
- Obtain certificates from a trusted Certificate Authority
- Use Hardware Security Modules (HSM) for key storage
- Implement proper key management and rotation
- Follow organizational security policies

See [WALKTHROUGH.md - Security Considerations](./WALKTHROUGH.md#security-considerations) for details.

## Project Structure

```
04-c2pa-provenance-demo/
├── src/                    # TypeScript source files
│   ├── cli-sign.ts         # Signing CLI
│   └── cli-verify.ts       # Verification CLI
├── viewer/                 # Web-based manifest viewer
│   ├── index.html
│   ├── styles.css
│   └── viewer.js
├── examples/               # Example files and scripts
│   ├── generate-dev-certs.sh
│   ├── metadata-*.json
│   └── certs/             # Generated certificates
└── test/                  # Test suite
```

## Requirements

- Node.js 18.0.0+
- OpenSSL 1.1.1+ (for certificate generation)
- npm or yarn

## Scripts

| Command | Description |
|---------|-------------|
| `npm run build` | Compile TypeScript to JavaScript |
| `npm run clean` | Remove compiled files |
| `npm run sign` | Run the signing CLI |
| `npm run verify` | Run the verification CLI |
| `npm run viewer` | Start the web viewer (port 8080) |
| `npm test` | Run the test suite |

## C2PA v2.2 Compliance

This implementation supports:
- ✅ Manifest signing with PS256 (RSA-PSS + SHA-256)
- ✅ Hard bindings to JPEG, PNG, WebP
- ✅ AI generation assertions (`c2pa.ai-generative-training`)
- ✅ Action history tracking (`c2pa.actions`)
- ✅ Schema.org CreativeWork metadata
- ✅ EXIF metadata preservation
- ✅ Content ingredient tracking

## Use Cases

### AI-Generated Content
Mark AI-generated images with:
- Training data usage restrictions
- Model information
- Generation parameters
- Software agent details

### Edited Photography
Track editing history with:
- Original source (ingredients)
- Edit actions and parameters
- Software used
- EXIF metadata

### Content Authentication
Sign any digital content to establish:
- Authorship
- Creation date
- Content integrity
- Chain of custody

## Related Resources

- [C2PA Specification v2.2](https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html)
- [Content Authenticity Initiative](https://contentauthenticity.org/)
- [c2pa-node Library](https://www.npmjs.com/package/c2pa-node)
- [NIST AI 600-1 (GenAI Profile)](https://doi.org/10.6028/NIST.AI.600-1) - Information Integrity

## Part of Responsible GenAI Starter Kit

This demo is **Deliverable 4** of the [Responsible GenAI Starter Kit](../../README.md), which provides:

1. Risk & Control Checklist
2. Evaluation Harness
3. CI/CD Security Pipeline
4. **C2PA Provenance Demo** (this deliverable)
5. ISO 42001 Bridge
6. Educator Toolkit

All aligned with NIST AI RMF and secure-by-design principles.

## License

MIT License - See the main project for details.

---

**Questions?** See [WALKTHROUGH.md](./WALKTHROUGH.md) or the main Responsible GenAI Starter Kit documentation.
