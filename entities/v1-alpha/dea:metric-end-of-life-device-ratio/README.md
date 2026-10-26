# dea:metric-end-of-life-device-ratio

Candidate Performance Metric record for **End-of-Life Device Ratio** (EOLDR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-end-of-life-device-ratio`
- **Name:** End-of-Life Device Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** EOLDR

## 2. Definition

End-of-Life Device Ratio (EOLDR) measures exposure to adverse outcomes in the Network Change & Configuration Management domain. Its calculation is Devices Past Vendor EOL / Devices, measured in percent (%). It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Lower values are better; each reduction is an improvement. Its use is not sector-specific; it appears in cross-industry performance frameworks.

## 3. Context

Measures the share of network devices past their support or end-of-life dates. EoL devices no longer receive patches: they are permanent vulnerabilities. Ratios that exclude devices 'scheduled for replacement' preserve the risk while improving the number. Read with technical debt remediation progress and firmware currency compliance.

## Formula

```
Devices Past Vendor EOL / Devices
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** risk
- **Scope classification:** organizational_unit
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** network_change_configuration_management

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 3374 (batch 7)
