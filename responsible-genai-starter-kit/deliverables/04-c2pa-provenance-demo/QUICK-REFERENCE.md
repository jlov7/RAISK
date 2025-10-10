# C2PA Demo - Quick Reference Card

## Setup (One-Time)

```bash
npm install
npm run build
bash examples/generate-dev-certs.sh
bash examples/create-sample-image.sh
```

## Common Commands

### Sign an Image

```bash
npm run sign -- \
  -i input.jpg \
  -o output.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --title "My Image" \
  --author "Your Name"
```

### Sign AI-Generated Content

```bash
npm run sign -- \
  -i ai-image.png \
  -o ai-signed.png \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  --ai-generated \
  --title "AI Landscape"
```

### Sign with Custom Metadata

```bash
npm run sign -- \
  -i image.jpg \
  -o signed.jpg \
  -c examples/certs/dev-certificate.pem \
  -k examples/certs/dev-private-key.pem \
  -m examples/metadata-ai-generated.json
```

### Verify Signed Image

```bash
npm run verify -- -i signed-image.jpg
```

### Verify with Details

```bash
npm run verify -- -i signed-image.jpg --detailed
```

### Verify and Export

```bash
npm run verify -- \
  -i signed-image.jpg \
  -o manifest.json \
  --detailed
```

### Start Web Viewer

```bash
npm run viewer
# Open http://localhost:8080
```

## CLI Options

### Sign Tool

| Option | Description |
|--------|-------------|
| `-i, --input <file>` | Input file to sign |
| `-o, --output <file>` | Output file |
| `-c, --cert <file>` | Certificate PEM |
| `-k, --key <file>` | Private key PEM |
| `-m, --metadata <file>` | Metadata JSON |
| `-t, --title <string>` | Content title |
| `-a, --author <string>` | Author name |
| `--ai-generated` | Mark as AI content |

### Verify Tool

| Option | Description |
|--------|-------------|
| `-i, --input <file>` | File to verify |
| `-o, --output <file>` | Export manifest JSON |
| `-d, --detailed` | Show all assertions |

## Metadata Templates

| File | Use Case |
|------|----------|
| `metadata-simple.json` | Basic signing |
| `metadata-ai-generated.json` | AI content |
| `metadata-edited.json` | Edited photos |

## File Locations

| Path | Contents |
|------|----------|
| `examples/certs/` | Development certificates |
| `examples/images/` | Sample images |
| `examples/metadata-*.json` | Metadata templates |
| `viewer/` | Web viewer files |
| `src/` | TypeScript source |
| `dist/` | Compiled JavaScript |

## Supported Formats

- JPEG (`.jpg`, `.jpeg`)
- PNG (`.png`)
- WebP (`.webp`)

## Common Tasks

### Test Everything

```bash
npm test
```

### Rebuild After Changes

```bash
npm run clean
npm run build
```

### View Certificate Info

```bash
openssl x509 -in examples/certs/dev-certificate.pem -text -noout
```

### Check File Has Manifest

```bash
npm run verify -- -i file.jpg
```

## Security Warnings

- Development certificates ONLY
- DO NOT use in production
- Private keys are unencrypted
- Self-signed = not trusted

## Getting Help

- Full docs: `WALKTHROUGH.md`
- Quick start: `README.md`
- Examples: `examples/README.md`
- C2PA Spec: https://c2pa.org/specifications/

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `tsc: command not found` | `npm install` |
| No certificates | `bash examples/generate-dev-certs.sh` |
| `c2pa-node` error | Check platform compatibility |
| Web viewer not working | `npm run viewer` on port 8080 |
| Verification fails | Development certs aren't trusted |

---

**Remember:** Development demo only - not for production!
