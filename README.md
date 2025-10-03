
# Vulnerability Report


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
