#!/usr/bin/env bash
# Helper to run advanced ZAP scans (authenticated, OpenAPI import, full active scan)
# Usage examples:
# ./zap_scan.sh --target https://staging.example.com --openapi ./openapi.json --auth-type none


set -euo pipefail
TARGET="${TARGET:-}" # override via env or args
OPENAPI=""
AUTH_TYPE="none"
REPORT_DIR="./zap-output"
mkdir -p "$REPORT_DIR"


while [[ $# -gt 0 ]]; do
case $1 in
--target) TARGET="$2"; shift 2;;
--openapi) OPENAPI="$2"; shift 2;;
--auth-type) AUTH_TYPE="$2"; shift 2;;
--report-dir) REPORT_DIR="$2"; shift 2;;
*) echo "Unknown arg: $1"; exit 1;;
esac
done


if [[ -z "$TARGET" ]]; then
echo "TARGET is required. Use --target or set TARGET environment variable."; exit 2
fi


if [[ -n "$OPENAPI" ]]; then
echo "Running ZAP API scan (OpenAPI): $OPENAPI"
docker run --rm -v ${PWD}:/zap/wrk/:rw owasp/zap2docker-stable \
zap-api-scan.py -t "$OPENAPI" -f openapi -r "$REPORT_DIR/zap_api_report.html" -J "$REPORT_DIR/zap_api_report.json"
else
echo "Running ZAP full scan against $TARGET"
docker run --rm -v ${PWD}:/zap/wrk/:rw owasp/zap2docker-stable \
zap-full-scan.py -t "$TARGET" -r "$REPORT_DIR/zap_full_report.html" -J "$REPORT_DIR/zap_full_report.json"
fi


echo "Reports saved to $REPORT_DIR"
