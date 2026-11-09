# dea:metric-ransomware-recovery-readiness-score

Candidate Performance Metric record for **Ransomware Recovery Readiness Score** (RRRS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-ransomware-recovery-readiness-score`
- **Name:** Ransomware Recovery Readiness Score
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** RRRS

## 2. Definition

Ransomware Recovery Readiness Score (RRRS) captures exposure to adverse outcomes for organizations tracking cybersecurity. It is computed as Weighted Index of Backups, Segmentation, Response Plans, expressed in index (0-100 or normalized). It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Higher values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

A composite assessment of the organization's ability to recover from a ransomware event - typically combining backup integrity and isolation, restore-time testing, incident playbooks, and the rehearsed decision capacity to rebuild rather than pay. Its strategic significance is the shift in the ransomware threat model from encryption to exfiltration-plus-encryption: backups that once solved the problem no longer do when the attacker also threatens data release, so readiness now includes the legal, communications, and extortion-response dimensions that pure recovery metrics miss. The score only carries weight when grounded in tested restores - the difference between a backup and a recovery is a rehearsal, which is why mature assessments time actual restore exercises rather than inventory backup jobs. Boards increasingly ask for it alongside cyber insurance terms, since insurers price coverage against exactly this readiness.

## Formula

```
RRRS = Weighted Index of Backups, Segmentation, Response Plans
```

## Unit

- **Unit reference:** `dea:unit-index`
- **Unit:** index
- **Unit label (as published):** index (0-100 or normalized)

## Classification

- **Subject classification:** governance
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** cybersecurity

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 331 (batch 1)
