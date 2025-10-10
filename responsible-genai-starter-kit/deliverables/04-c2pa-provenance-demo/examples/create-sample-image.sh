#!/bin/bash

###############################################################################
# Sample Image Creator for C2PA Demo
#
# Creates a simple test image using ImageMagick (if available)
# or provides instructions for adding your own images
###############################################################################

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE_DIR="${SCRIPT_DIR}/images"

echo "Creating sample images directory..."
mkdir -p "$IMAGE_DIR"

# Check if ImageMagick is available
if command -v convert &> /dev/null; then
    echo "✓ ImageMagick found - generating sample image..."

    # Create a simple gradient image with text
    convert -size 800x600 \
        gradient:blue-lightblue \
        -pointsize 48 \
        -fill white \
        -gravity center \
        -annotate +0-50 "C2PA Demo Image" \
        -pointsize 24 \
        -annotate +0+0 "Sample image for content provenance testing" \
        -pointsize 18 \
        -annotate +0+50 "$(date '+%Y-%m-%d')" \
        "$IMAGE_DIR/sample-unsigned.jpg"

    echo "✓ Sample image created: images/sample-unsigned.jpg"
    echo
else
    echo "⚠ ImageMagick not found - cannot generate sample image"
    echo
    echo "To create sample images:"
    echo "1. Install ImageMagick: brew install imagemagick (macOS)"
    echo "2. Or manually add your own images to: $IMAGE_DIR"
    echo "3. Supported formats: JPEG, PNG, WebP"
    echo
fi

# Create README for images directory
cat > "$IMAGE_DIR/README.txt" << 'EOF'
Sample Images Directory
=======================

This directory contains sample images for C2PA signing and verification demos.

Usage:
1. Add your own images (JPEG, PNG, WebP) to this directory
2. Use the signing CLI to add C2PA manifests
3. Use the verification CLI to inspect manifests
4. Test the web viewer with signed images

Example:
  # Sign an image
  npm run sign -- \
    -i examples/images/sample-unsigned.jpg \
    -o examples/images/sample-signed.jpg \
    -c examples/certs/dev-certificate.pem \
    -k examples/certs/dev-private-key.pem \
    --title "My Test Image" \
    --author "Demo User"

  # Verify the signed image
  npm run verify -- \
    -i examples/images/sample-signed.jpg \
    --detailed

Note: Keep original unsigned versions for testing purposes.
EOF

echo "✓ Created images directory: $IMAGE_DIR"
echo "✓ See $IMAGE_DIR/README.txt for usage instructions"
echo
