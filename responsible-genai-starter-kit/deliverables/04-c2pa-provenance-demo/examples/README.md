# C2PA Demo Examples

This directory contains example files, scripts, and templates for the C2PA Provenance Demo.

## Contents

### Certificate Generation

**`generate-dev-certs.sh`**
- Generates self-signed development certificates
- Creates `certs/` directory with certificate and private key
- **⚠ WARNING: Development use only - NOT for production**

Usage:
```bash
bash generate-dev-certs.sh
```

Output:
- `certs/dev-certificate.pem` - Public certificate
- `certs/dev-private-key.pem` - Private key (keep secure!)
- `certs/README.txt` - Security warnings

### Sample Image Creation

**`create-sample-image.sh`**
- Creates test images using ImageMagick
- Creates `images/` directory with sample content

Usage:
```bash
bash create-sample-image.sh
```

If ImageMagick is not installed, manually add images to `images/` directory.

### Metadata Templates

Three example metadata files demonstrate different use cases:

#### 1. **`metadata-simple.json`**
Basic content signing with minimal metadata:
- Title and author
- Creation timestamp
- Simple action history

Use case: Basic authentication of original content

Example:
```bash
npm run sign -- \
  -i examples/images/photo.jpg \
  -o examples/images/photo-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  -m examples/metadata-simple.json
```

#### 2. **`metadata-ai-generated.json`**
AI-generated content with full provenance:
- AI software agent information
- Training data restrictions (CAWG 1.1: `cawg.training-mining`)
- Generation parameters (prompt, seed, steps)
- Model information
- Compliance with NIST AI transparency requirements

**Note**: Uses CAWG 1.1 assertion (DIF-ratified, May 2025). C2PA v2.2 removed training/mining from core spec.

Use case: AI-generated images, synthetic media

Example:
```bash
npm run sign -- \
  -i examples/images/ai-image.png \
  -o examples/images/ai-image-signed.png \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  -m examples/metadata-ai-generated.json
```

#### 3. **`metadata-edited.json`**
Edited content with complete history:
- Multiple edit actions
- Edit parameters and software
- Original source (ingredients)
- EXIF camera metadata
- Chain of custody

Use case: Professional photo editing, content modifications

Example:
```bash
npm run sign -- \
  -i examples/images/edited-photo.jpg \
  -o examples/images/edited-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  -m examples/metadata-edited.json
```

## Creating Custom Metadata

You can create your own metadata JSON files following this structure:

```json
{
  "title": "Content Title",
  "claim_generator": "C2PA Provenance Demo v0.1.0",
  "format": "image/jpeg",
  "assertions": [
    {
      "label": "stds.schema-org.CreativeWork",
      "data": {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": "Your content name",
        "author": "Author name",
        "dateCreated": "2025-01-15T10:00:00Z"
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

### Common C2PA Assertion Labels

| Label | Purpose | C2PA v2.2 |
|-------|---------|-----------|
| `stds.schema-org.CreativeWork` | Dublin Core metadata (title, author, etc.) | ✅ |
| `c2pa.actions` | Edit/creation history | ✅ |
| `c2pa.ai-generative-training` | AI generation info | ✅ (New) |
| `c2pa.hash.data` | Content hash for integrity | ✅ |
| `stds.exif` | Camera/device EXIF data | ✅ |
| `c2pa.ingredient` | Source content references | ✅ |

### AI Content Assertions (C2PA v2.2)

For AI-generated content, include:

```json
{
  "label": "c2pa.ai-generative-training",
  "data": {
    "c2pa.training": "notAllowed",
    "c2pa.softwareAgent": {
      "name": "AI Generator Name",
      "version": "1.0.0"
    },
    "c2pa.model": {
      "name": "Model Name",
      "version": "1.0",
      "trainingDataSources": ["Description of training data"]
    }
  }
}
```

Values for `c2pa.training`:
- `allowed` - Content can be used for AI training
- `notAllowed` - Content cannot be used for training
- `constrained` - Content use is restricted (requires legal review)

## Directory Structure

```
examples/
├── README.md                    # This file
├── generate-dev-certs.sh        # Certificate generator
├── create-sample-image.sh       # Sample image creator
├── metadata-simple.json         # Basic metadata template
├── metadata-ai-generated.json   # AI content template
├── metadata-edited.json         # Edited content template
├── certs/                       # Development certificates (generated)
│   ├── dev-certificate.pem
│   ├── dev-private-key.pem
│   └── README.txt
└── images/                      # Sample images (user-provided)
    └── README.txt
```

## Security Reminders

1. **Development Certificates Only**
   - Self-signed certificates in `certs/` are for testing only
   - NOT trusted by production validators
   - Use proper CA-issued certificates for production

2. **Private Key Protection**
   - Never commit `*.pem` files to version control
   - Keep `dev-private-key.pem` secure
   - Use file permissions: `chmod 600 dev-private-key.pem`

3. **Production Requirements**
   - Obtain certificates from trusted CA
   - Use Hardware Security Modules (HSM)
   - Implement key rotation
   - Follow organizational security policies

See [WALKTHROUGH.md](../WALKTHROUGH.md#security-considerations) for complete security guidance.

## Testing

After generating certificates and images, test the complete workflow:

```bash
# 1. Generate certificates
bash examples/generate-dev-certs.sh

# 2. Create sample image (or add your own)
bash examples/create-sample-image.sh

# 3. Sign the image
npm run sign -- \
  -i examples/images/sample-unsigned.jpg \
  -o examples/images/sample-signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --title "Test Image" \
  --ai-generated

# 4. Verify the signature
npm run verify -- \
  -i examples/images/sample-signed.jpg \
  --detailed

# 5. View in browser
npm run viewer
# Open http://localhost:8080 and drag the signed image
```

## Resources

- [C2PA Specification v2.2](https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html)
- [Content Authenticity Initiative](https://contentauthenticity.org/)
- [NIST AI 600-1 (GenAI Profile)](https://doi.org/10.6028/NIST.AI.600-1)
- [Complete Walkthrough](../WALKTHROUGH.md)

---

**Need help?** See the main [WALKTHROUGH.md](../WALKTHROUGH.md) or [README.md](../README.md)
