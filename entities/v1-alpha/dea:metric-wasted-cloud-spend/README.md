# dea:metric-wasted-cloud-spend

Candidate Performance Metric record for **Wasted Cloud Spend** (WCS) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-wasted-cloud-spend`
- **Name:** Wasted Cloud Spend
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** WCS

## 2. Definition

Wasted Cloud Spend (WCS) addresses how efficiently resources are converted into outputs and is a fixture of data center & cloud operations reporting. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. Its calculation is Unattached or Under-Used Resource Spend / Total Cloud Spend, measured in percent (%). It should be driven down, since lower readings signal healthier performance. It originates from and is most used in Technology & data centers practice.

## 3. Context

Wasted cloud spend measures spend that delivers no value - idle resources, over-provisioned instances, orphaned storage, forgotten development environments, rightsizing misses - and it is the FinOps movement's founding metric: industry surveys consistently estimate substantial fractions of cloud spend as waste, which is margin available without any performance cost. The waste taxonomy matters for action: idle-but-running resources (stopped but storage persists, dev environments on nights and weekends), over-provisioned (sized for peak always-on), and abandoned (orphaned volumes, unattached IPs) each have different fixes. The measurement challenge is definitional honesty - the honest version requires utilization telemetry on every resource class, and the deeper waste is architectural (inefficient designs that scale costs superlinearly) rather than operational. Read with utilization-percentile distributions by resource type, commitment-discount coverage (savings plans and reserved instances shift price, not usage), and cost-per-unit-of-work which aligns spend with business output.

## Formula

```
Unattached or Under-Used Resource Spend / Total Cloud Spend
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1092 (batch 4)
