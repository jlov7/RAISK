#!/bin/bash

# Workflow Validation Script
# SSDF Practice: PW.1.1 - Define and maintain secure build processes
#
# This script validates GitHub Actions workflows for:
# - YAML syntax correctness
# - Pinned action versions (commit SHAs)
# - Required permissions
# - SSDF practice annotations

set -e

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Counters
TOTAL_CHECKS=0
PASSED_CHECKS=0
FAILED_CHECKS=0
WARNING_CHECKS=0

# Tool availability detection
HAS_YQ=0
HAS_PYYAML=0
if command -v yq >/dev/null 2>&1; then
    HAS_YQ=1
elif command -v python3 >/dev/null 2>&1; then
    if python3 -c "import yaml" >/dev/null 2>&1; then
        HAS_PYYAML=1
    fi
fi

echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}  SSDF Workflow Validation Tool${NC}"
echo -e "${BLUE}  NIST SP 800-218A Compliance Checker${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""

# Determine workflow directory
if [ -d "workflows" ]; then
    WORKFLOW_DIR="workflows"
elif [ -d ".github/workflows" ]; then
    WORKFLOW_DIR=".github/workflows"
else
    echo -e "${RED}ERROR: No workflow directory found${NC}"
    echo "Expected: ./workflows or ./.github/workflows"
    exit 1
fi

echo -e "${GREEN}Found workflows in: $WORKFLOW_DIR${NC}"
echo ""

# Function to increment counters
check_passed() {
    ((TOTAL_CHECKS++))
    ((PASSED_CHECKS++))
    echo -e "${GREEN}✓${NC} $1"
}

check_failed() {
    ((TOTAL_CHECKS++))
    ((FAILED_CHECKS++))
    echo -e "${RED}✗${NC} $1"
}

check_warning() {
    ((TOTAL_CHECKS++))
    ((WARNING_CHECKS++))
    echo -e "${YELLOW}⚠${NC} $1"
}

# 1. YAML Syntax Validation
echo -e "${BLUE}[1] Validating YAML Syntax${NC}"
echo "-----------------------------------"

for workflow in "$WORKFLOW_DIR"/*.yml; do
    if [ -f "$workflow" ]; then
        filename=$(basename "$workflow")

        if [ "$HAS_YQ" -eq 1 ]; then
            if yq eval '.' "$workflow" > /dev/null 2>&1; then
                check_passed "$filename: Valid YAML syntax"
            else
                check_failed "$filename: Invalid YAML syntax"
            fi
        elif [ "$HAS_PYYAML" -eq 1 ]; then
            if python3 - "$workflow" <<'PY' > /dev/null 2>&1
import sys
import yaml

with open(sys.argv[1], 'r', encoding='utf-8') as handle:
    yaml.safe_load(handle)
PY
            then
                check_passed "$filename: Valid YAML syntax"
            else
                check_failed "$filename: Invalid YAML syntax"
            fi
        else
            check_warning "$filename: Cannot validate YAML (install yq or PyYAML)"
        fi
    fi
done

echo ""

# 2. Action Version Pinning
echo -e "${BLUE}[2] Checking Action Version Pinning${NC}"
echo "-----------------------------------"

for workflow in "$WORKFLOW_DIR"/*.yml; do
    if [ -f "$workflow" ]; then
        filename=$(basename "$workflow")

        # Find all 'uses:' lines
        unpinned=$(grep -E "uses:\s+[^@]+@v[0-9]" "$workflow" || true)

        if [ -z "$unpinned" ]; then
            check_passed "$filename: All actions pinned to commit SHAs"
        else
            check_failed "$filename: Found unpinned actions (using tags instead of SHAs)"
            echo "  Unpinned: $(echo "$unpinned" | wc -l) actions"
            echo "$unpinned" | sed 's/^/    /'
        fi
    fi
done

echo ""

# 3. Required Permissions Check
echo -e "${BLUE}[3] Validating Least-Privilege Permissions${NC}"
echo "-----------------------------------"

for workflow in "$WORKFLOW_DIR"/*.yml; do
    if [ -f "$workflow" ]; then
        filename=$(basename "$workflow")

        # Check if permissions are defined
        if grep -q "permissions:" "$workflow"; then
            check_passed "$filename: Permissions explicitly defined"

            # Check for overly permissive settings
            if grep -E "permissions:\s+(write-all|.*:\s+write-all)" "$workflow"; then
                check_failed "$filename: Found write-all permissions (violates least privilege)"
            fi
        else
            check_warning "$filename: No explicit permissions (defaults to read-all)"
        fi
    fi
done

echo ""

# 4. SSDF Practice Annotations
echo -e "${BLUE}[4] Checking SSDF Practice Documentation${NC}"
echo "-----------------------------------"

for workflow in "$WORKFLOW_DIR"/*.yml; do
    if [ -f "$workflow" ]; then
        filename=$(basename "$workflow")

        # Check for SSDF practice comments
        ssdf_refs=$(grep -c "SSDF" "$workflow" || echo "0")

        if [ "$ssdf_refs" -gt 0 ]; then
            check_passed "$filename: Contains $ssdf_refs SSDF practice references"
        else
            check_failed "$filename: No SSDF practice annotations found"
        fi
    fi
done

echo ""

# 5. Security Best Practices
echo -e "${BLUE}[5] Security Best Practices${NC}"
echo "-----------------------------------"

for workflow in "$WORKFLOW_DIR"/*.yml; do
    if [ -f "$workflow" ]; then
        filename=$(basename "$workflow")

        # Check for timeout settings (prevent resource exhaustion)
        if grep -q "timeout-minutes:" "$workflow"; then
            check_passed "$filename: Timeout configured"
        else
            check_warning "$filename: No timeout configured (resource exhaustion risk)"
        fi

        # Check for hardcoded secrets
        if grep -E "(password|secret|token|key):\s*['\"][^$]" "$workflow" | grep -v -E "(#|uses:|name:)" > /dev/null; then
            check_failed "$filename: Potential hardcoded secrets detected"
        else
            check_passed "$filename: No hardcoded secrets detected"
        fi

        # Check for shell injection risks (unquoted variables)
        if grep -E '\$\{\{\s*github\.event\.[^}]+\}\}' "$workflow" | grep -v "\"" > /dev/null; then
            check_warning "$filename: Potential shell injection risk (unquoted user input)"
        fi
    fi
done

echo ""

# 6. Workflow Triggers
echo -e "${BLUE}[6] Validating Workflow Triggers${NC}"
echo "-----------------------------------"

for workflow in "$WORKFLOW_DIR"/*.yml; do
    if [ -f "$workflow" ]; then
        filename=$(basename "$workflow")

        # Check for workflow_dispatch (manual trigger)
        if grep -q "workflow_dispatch:" "$workflow"; then
            check_passed "$filename: Manual trigger enabled"
        else
            check_warning "$filename: No manual trigger (workflow_dispatch)"
        fi

        # Check for scheduled workflows
        if grep -q "schedule:" "$workflow"; then
            cron=$(grep -A 1 "schedule:" "$workflow" | grep "cron:" | sed 's/.*cron://' | tr -d "'\"")
            check_passed "$filename: Scheduled trigger configured"
        fi
    fi
done

echo ""

# 7. SBOM and Attestation Checks (for relevant workflows)
echo -e "${BLUE}[7] SBOM and Attestation Validation${NC}"
echo "-----------------------------------"

if [ -f "$WORKFLOW_DIR/sbom.yml" ]; then
    if grep -q "anchore/sbom-action" "$WORKFLOW_DIR/sbom.yml"; then
        check_passed "sbom.yml: SBOM generation configured"
    else
        check_failed "sbom.yml: No SBOM generation action found"
    fi

    if grep -q "actions/attest-sbom" "$WORKFLOW_DIR/sbom.yml"; then
        check_passed "sbom.yml: SBOM attestation configured"
    else
        check_warning "sbom.yml: No SBOM attestation action found"
    fi
fi

if [ -f "$WORKFLOW_DIR/provenance.yml" ]; then
    if grep -q "actions/attest-build-provenance" "$WORKFLOW_DIR/provenance.yml"; then
        check_passed "provenance.yml: Build provenance attestation configured"
    else
        check_failed "provenance.yml: No build provenance attestation found"
    fi

    if grep -q "sigstore/cosign-installer" "$WORKFLOW_DIR/provenance.yml"; then
        check_passed "provenance.yml: Sigstore signing configured"
    else
        check_warning "provenance.yml: No Sigstore signing found"
    fi
fi

echo ""

# 8. Configuration File Validation
echo -e "${BLUE}[8] Configuration Files${NC}"
echo "-----------------------------------"

if [ -f ".syft.yaml" ]; then
    check_passed "Found .syft.yaml SBOM configuration"
else
    check_warning "Missing .syft.yaml (SBOM generation will use defaults)"
fi

if [ -f "SSDF-mapping.md" ]; then
    check_passed "Found SSDF-mapping.md documentation"
else
    check_failed "Missing SSDF-mapping.md documentation"
fi

if [ -f "SETUP.md" ]; then
    check_passed "Found SETUP.md setup guide"
else
    check_failed "Missing SETUP.md setup guide"
fi

echo ""

# 9. Required Files Check
echo -e "${BLUE}[9] Required Workflow Files${NC}"
echo "-----------------------------------"

required_workflows=("security.yml" "sbom.yml" "provenance.yml" "scorecard.yml")

for workflow_file in "${required_workflows[@]}"; do
    if [ -f "$WORKFLOW_DIR/$workflow_file" ]; then
        check_passed "Found $workflow_file"
    else
        check_failed "Missing $workflow_file"
    fi
done

echo ""

# Summary
echo -e "${BLUE}================================================${NC}"
echo -e "${BLUE}  Validation Summary${NC}"
echo -e "${BLUE}================================================${NC}"
echo ""
echo "Total Checks:   $TOTAL_CHECKS"
echo -e "${GREEN}Passed:         $PASSED_CHECKS${NC}"
echo -e "${RED}Failed:         $FAILED_CHECKS${NC}"
echo -e "${YELLOW}Warnings:       $WARNING_CHECKS${NC}"
echo ""

# Calculate pass rate
pass_rate=$(awk "BEGIN {printf \"%.1f\", ($PASSED_CHECKS / $TOTAL_CHECKS) * 100}")
echo "Pass Rate:      $pass_rate%"

echo ""

# SSDF Practice Coverage Assessment
if [ "$FAILED_CHECKS" -eq 0 ]; then
    echo -e "${GREEN}✓ SSDF Practice Mapping: COMPLETE${NC}"
    echo "  All critical checks passed. Workflows implement mapped SP 800-218A tasks."
    echo "  See SSDF-mapping.md for detailed practice coverage."
    exit 0
elif [ "$FAILED_CHECKS" -le 2 ]; then
    echo -e "${YELLOW}⚠ SSDF Practice Mapping: PARTIAL${NC}"
    echo "  Minor issues detected. Review failed checks above."
    exit 1
else
    echo -e "${RED}✗ SSDF Practice Mapping: INCOMPLETE${NC}"
    echo "  Critical issues detected. Fix failed checks before deployment."
    exit 1
fi
