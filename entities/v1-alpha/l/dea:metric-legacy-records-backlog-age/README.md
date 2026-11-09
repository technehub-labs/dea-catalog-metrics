# dea:metric-legacy-records-backlog-age

Candidate Performance Metric record for **Legacy Records Backlog Age** (LRBA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-legacy-records-backlog-age`
- **Name:** Legacy Records Backlog Age
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** LRBA

## 2. Definition

Legacy Records Backlog Age (LRBA) measures how efficiently resources are converted into outputs in the Records & Information Management domain. The formula is Average Age of Unprocessed Legacy Records - reported in days. It guides mid-horizon planning: portfolio, program, and function owners act on it between review cycles. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## Formula

```
LRBA = Average Age of Unprocessed Legacy Records
```

## Unit

- **Unit reference:** `dea:unit-day`
- **Unit:** day
- **Unit label (as published):** days

## Classification

- **Subject classification:** information_architecture
- **Purpose classification:** efficiency
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** managerial
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** records_information_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3694 (batch 8)
