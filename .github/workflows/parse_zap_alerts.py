#!/usr/bin/env python3
"""Simple parser that converts ZAP JSON alerts into a GitHub-friendly Markdown vulnerability report.
Usage: python parse_zap_alerts.py zap_report.json output.md
"""
import json
import sys
from collections import defaultdict


SEVERITY_ORDER = ["High", "Medium", "Low", "Informational"]
def load_alerts(path):
return findings




def group_by_risk(findings):
grouped = defaultdict(list)
for f in findings:
grouped[f['risk']].append(f)
return grouped




if __name__ == '__main__':
if len(sys.argv) < 3:
print('Usage: parse_zap_alerts.py zap_report.json output.md')
sys.exit(2)
src = sys.argv[1]
dst = sys.argv[2]
sites = load_alerts(src)
findings = extract_alerts(sites)
grouped = group_by_risk(findings)


with open(dst, 'w', encoding='utf-8') as out:
out.write('# VULNERABILITY REPORT\n\n')
out.write('Automatically generated from ZAP JSON output.\n\n')
for sev in SEVERITY_ORDER:
items = grouped.get(sev, [])
out.write(f'## {sev} ({len(items)})\n\n')
for i, f in enumerate(items, 1):
out.write(f'### {i}. {f["name"]}\n')
out.write(f'- **Risk**: {f["risk"]}\n')
out.write(f'- **Confidence**: {f["confidence"]}\n')
out.write(f'- **URL / Instance**: {f["url"]}\n')
if f['param']:
out.write(f'- **Parameter**: {f["param"]}\n')
if f['evidence']:
out.write(f'- **Evidence**: {f["evidence"]}\n')
out.write('\n**Description**\n\n')
out.write(f'{f["description"]}\n\n')
out.write('**Proposed Remediation**\n\n')
out.write(f'{f["solution"] or "See references"}\n\n')
if f['reference']:
out.write('**References**\n\n')
out.write(f'{f["reference"]}\n\n')
out.write('\n')


print(f'Wrote report to {dst}')
