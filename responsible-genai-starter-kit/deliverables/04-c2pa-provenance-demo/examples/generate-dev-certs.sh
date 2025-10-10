#!/bin/bash

###############################################################################
# C2PA Development Certificate Generator
#
# ⚠️  WARNING: DEVELOPMENT KEYS ONLY - DO NOT USE IN PRODUCTION ⚠️
#
# This script generates self-signed certificates for C2PA development and
# testing purposes ONLY. These certificates are NOT suitable for production use.
#
# For production:
# - Obtain certificates from a trusted Certificate Authority (CA)
# - Use proper key management and Hardware Security Modules (HSM)
# - Follow your organization's security policies
#
# Requirements: OpenSSL 1.1.1 or later
###############################################################################

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CERT_DIR="${SCRIPT_DIR}/certs"

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║       C2PA Development Certificate Generator                   ║"
echo "║                                                                ║"
echo "║  ⚠️  WARNING: DEVELOPMENT KEYS ONLY ⚠️                         ║"
echo "║  DO NOT USE THESE CERTIFICATES IN PRODUCTION                   ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo

# Check if OpenSSL is available
if ! command -v openssl &> /dev/null; then
    echo "❌ Error: OpenSSL is not installed"
    echo "Install OpenSSL to generate certificates"
    exit 1
fi

# Check OpenSSL version
OPENSSL_VERSION=$(openssl version | awk '{print $2}')
echo "✓ OpenSSL version: $OPENSSL_VERSION"
echo

# Create certificate directory
mkdir -p "$CERT_DIR"

echo "📁 Creating certificate directory: $CERT_DIR"
echo

# Generate private key
echo "🔑 Generating private key..."
openssl genrsa -out "$CERT_DIR/dev-private-key.pem" 2048
echo "✓ Private key generated: dev-private-key.pem"
echo

# Generate self-signed certificate
echo "📜 Generating self-signed certificate..."
openssl req -new -x509 \
    -key "$CERT_DIR/dev-private-key.pem" \
    -out "$CERT_DIR/dev-certificate.pem" \
    -days 365 \
    -subj "/C=US/ST=Development/L=DevCity/O=C2PA Demo/OU=Development/CN=c2pa-demo.local" \
    -addext "basicConstraints=CA:FALSE" \
    -addext "keyUsage=digitalSignature" \
    -addext "extendedKeyUsage=codeSigning"

echo "✓ Certificate generated: dev-certificate.pem"
echo

# Display certificate info
echo "📋 Certificate Information:"
echo "─────────────────────────────────────────────────────────────────"
openssl x509 -in "$CERT_DIR/dev-certificate.pem" -noout -text | grep -A 2 "Subject:"
openssl x509 -in "$CERT_DIR/dev-certificate.pem" -noout -text | grep -A 2 "Validity"
echo "─────────────────────────────────────────────────────────────────"
echo

# Create README with warnings
cat > "$CERT_DIR/README.txt" << 'EOF'
╔════════════════════════════════════════════════════════════════╗
║                     ⚠️  CRITICAL WARNING ⚠️                    ║
╚════════════════════════════════════════════════════════════════╝

DEVELOPMENT CERTIFICATES ONLY - DO NOT USE IN PRODUCTION

These certificates are self-signed and intended ONLY for:
- Local development
- Testing C2PA functionality
- Educational demonstrations

❌ DO NOT USE THESE CERTIFICATES FOR:
- Production applications
- Public-facing content
- Content that requires legal authenticity
- Any situation requiring trust validation

🔐 Production Certificate Requirements:
1. Obtain certificates from a trusted Certificate Authority (CA)
2. Use proper key management practices
3. Store private keys in Hardware Security Modules (HSM)
4. Implement key rotation policies
5. Follow organizational security standards
6. Comply with C2PA certification requirements

📚 Resources:
- C2PA Certification: https://c2pa.org/certification/
- Certificate Management Best Practices:
  https://c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html#_certificates

Generated: $(date)
EOF

echo "✅ Certificate generation complete!"
echo
echo "📂 Files created in: $CERT_DIR"
echo "   - dev-private-key.pem      (Private key - KEEP SECURE)"
echo "   - dev-certificate.pem      (Public certificate)"
echo "   - README.txt               (Important warnings)"
echo
echo "⚠️  SECURITY REMINDER:"
echo "   - These are DEVELOPMENT certificates only"
echo "   - Private key has NO password protection (for demo convenience)"
echo "   - NEVER commit these files to version control"
echo "   - NEVER use in production environments"
echo
echo "✓ You can now use these certificates with the C2PA signing tool"
echo
