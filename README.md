COMPANY: CODTECH IT SOLUTIONS

NAME: OMIKA JENA

INTERN ID: CT04DY2062

DOMAIN: AUTOMATION TESTING

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH

# DAST Automation with OWASP ZAP


This repo provides a ready-to-run configuration for automating OWASP ZAP scans in GitHub Actions and producing a machine-readable and human-readable vulnerability report.


## What you get
- GitHub Actions workflow to run ZAP baseline on PRs or on-demand
- `zap_rules.yaml` for tuning false positives / alert filters
- `zap_scan.sh` helper for running more advanced scans (auth, OpenAPI import)
- `parse_zap_alerts.py` script to convert ZAP JSON to a GitHub-friendly Markdown vulnerability report
- `VULNERABILITY_REPORT_TEMPLATE.md` — a publishable report template


## How to use
1. Update the `target` URL in `.github/workflows/dast-zap.yml` or set `TARGET_URL` as an Actions secret.
2. Add any authentication tokens or credentials to GitHub Secrets and reference them in the workflow.
3. Open a PR or run the workflow manually — results/artifacts will include the ZAP report and parsed vulnerability report.


**Important:** Only scan assets you own or are authorized to test. Use a staging environment for CI scans.

## .github/workflows/dast-zap.yml


```yaml
name: DAST - OWASP ZAP Baseline


on:
pull_request:
workflow_dispatch:


jobs:
zap-baseline:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4


- name: Run ZAP baseline (Docker)
env:
TARGET_URL: ${{ secrets.TARGET_URL }}
run: |
#!/bin/bash
set -euo pipefail
mkdir -p ./zap-output
docker run --rm -v ${PWD}:/zap/wrk/:rw owasp/zap2docker-stable \
zap-baseline.py -t "$TARGET_URL" -r ./zap-output/zap_report.html -J ./zap-output/zap_report.json -d


- name: Upload ZAP report artifact
uses: actions/upload-artifact@v4
with:
name: zap-output
path: ./zap-output


- name: Parse ZAP JSON to Markdown report
uses: actions/setup-python@v4
with:
python-version: '3.x'
- name: Install requirements
run: |
python -m pip install --upgrade pip
pip install -r requirements.txt || true
- name: Generate VULNERABILITY_REPORT.md
run: |
python parse_zap_alerts.py ./zap-output/zap_report.json ./zap-output/VULNERABILITY_REPORT.md
- name: Upload vulnerability report
uses: actions/upload-artifact@v4
with:
name: vulnerability-report
path: ./zap-output/VULNERABILITY_REPORT.md


- name: Create GitHub issue for critical findings (optional)
if: always()
run: |
# This step is left as a placeholder: use zaproxy/action-baseline or GH REST API to create issues

echo "Consider using

*Vulnerability Report*


**Application:** [APP NAME]
**Environment:** [staging / test]
**Scan date:** [YYYY-MM-DD]
**Scanner:** OWASP ZAP (baseline/full)
**Scan coordinator:** [name / team]


---


## Executive summary
- Total findings: [TOTAL]
- High: [n]
- Medium: [n]
- Low: [n]
- Informational: [n]


## Scope
- Target URL(s):
- https://staging.example.com
- Excluded paths: /health, /metrics


## Methodology
- Tool: OWASP ZAP (docker)
- Scan type: baseline / full / API (OpenAPI)
- Auth: none / form-based / OAuth2 / API key
- Notes: run from GitHub Actions runner located in [region]


## Findings (by severity)


### High


#### 1) [Finding title]
- **Location:** [URL or endpoint]
- **CWE:** [CWE-xxx]
- **Description:** [Detailed description with reproduction steps]
- **Evidence:** [HTTP request/response excerpt or screenshot reference]
- **Impact:** [Business/technical impact]
- **Remediation:** [Step-by-step fix and code/configuration example]
- **References:** [OWASP / CVE / vendor docs]
- **Status:** Open / In progress / Remediated


(Repeat for each finding)
## Remediation summary & timeline
- Critical / High fixes to be addressed within [X] days.
- Medium within [Y] days.
- Low/Informational tracked for next milestone.


## Appendix
- Raw ZAP reports: `zap_report.json`, `zap_report.html`
- ZAP rules used: `zap_rules.yaml`
- CI workflow: `.github/workflows/dast-zap.yml`
*Legal & Ethics Reminder*
Only scan applications and infrastructure for which you have explicit authorization. Unauthorized scanning may violate law and service agreements.
