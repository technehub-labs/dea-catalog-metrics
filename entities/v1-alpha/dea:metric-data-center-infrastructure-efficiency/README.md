# dea:metric-data-center-infrastructure-efficiency

Candidate Performance Metric record for **Data Center Infrastructure Efficiency** (DCIE) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-center-infrastructure-efficiency`
- **Name:** Data Center Infrastructure Efficiency
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** DCIE

## 2. Definition

Data Center Infrastructure Efficiency (DCIE) captures how efficiently resources are converted into outputs for organizations tracking data center & cloud operations. Its calculation is IT Equipment Power / Total Facility Power, measured in percent (%). It originates from and is most used in Technology & data centers practice. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Data center infrastructure efficiency (PUE, power usage effectiveness) measures total facility power divided by IT equipment power - the fraction of energy that actually reaches computing - and it is the energy-efficiency metric of the data-center industry, where hyperscale operators now run at PUE of 1.1 or better while legacy facilities sit at 2.0 or worse. The gap is money and carbon: every tenth of PUE improvement across a large facility saves megawatt-hours, which is why PUE became the industry's universal benchmark (formalized by The Green Grid and adopted by the U.S. EPA Energy Star program). The gaming vector is definitional: partial PUE (measuring one room or pod), IT-load manipulation (meter placement choices), and running at low utilization all flatter the number without real efficiency. Read with IT utilization (PUE at low utilization wastes as much as poor design), carbon intensity of the power source (efficiency and cleanliness differ), and WUE and CUE companion metrics.

## Formula

```
IT Equipment Power / Total Facility Power
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** data_center_cloud_operations
- **Sector:** technology_data_centers

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1089 (batch 4)
