"""CR-MET-009 Gate 6: check_dual_anchor.py.

CR-MET-009 Q14 binding disposition: BOTH anchors are required for
admitted records. Anchor 1 = measurable_entity_kind (one of the 16
CR-MET-007 cross-domain subject types). Anchor 2 = reputability_tier
(5-value enum). For candidate records the anchors are informational.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _catalog import load_metrics  # noqa: E402


BASE = Path(__file__).parent.parent
ENTITIES_DIR = BASE / "entities"

MEASURABLE_KINDS = {
    "dea:BusinessCapability", "dea:BusinessProcess", "dea:BusinessService",
    "dea:Outcome", "dea:StrategicObjective", "dea:ValueStream",
    "dea:OrganizationalUnit", "dea:DataEntity", "dea:Service",
    "dea:ApplicationComponent", "dea:AssessmentDimension", "dea:Control",
    "dea:Policy", "dea:Risk", "dea:MaturityModel", "dea:AIMLModel",
}
REPUTABILITY_TIERS = {
    "industry_standard", "framework_derived", "sectoral_standard",
    "internal_custom", "emerging",
}


def main():
    findings = []
    for mid, m in load_metrics():
        if m.get("lifecycle_status") != "admitted":
            continue
        kind = m.get("measurable_entity_kind")
        if kind not in MEASURABLE_KINDS:
            findings.append(f"{mid}: measurable_entity_kind {kind!r} not in CR-MET-007 16-type set")
        tier = m.get("reputability_tier")
        if tier not in REPUTABILITY_TIERS:
            findings.append(f"{mid}: reputability_tier {tier!r} not in 5-value enum")
    if findings:
        print("FAIL: check_dual_anchor.py")
        for f in findings:
            print(f"  {f}")
        sys.exit(1)
    n = sum(1 for _, m in load_metrics() if m.get("lifecycle_status") == "admitted")
    print(f"PASS: check_dual_anchor.py ({n} admitted metrics, 0 dual-anchor findings)")


if __name__ == "__main__":
    main()