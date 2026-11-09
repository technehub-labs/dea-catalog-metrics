# dea:metric-data-center-availability

Candidate Performance Metric record for **Data Center Availability** (DCA) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-data-center-availability`
- **Name:** Data Center Availability
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** DCA

## 2. Definition

Data Center Availability (DCA) measures the quality of outputs and outcomes in the Data Center & Cloud Operations domain. It is defined as Uptime across Redundancy Tier / Total Time; the result is stated in percent (%). In Technology & data centers, it is a recognized element of the standard performance toolkit. Its trend is watched by senior leadership as an early signal of structural performance shifts. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Data center availability measures facility uptime against design tiers - the Uptime Institute's Tier classification (Tier I at 99.671 percent to Tier IV at 99.995 percent) formalizes the availability-redundancy relationship - and it is the metric that prices the mission-criticality of everything hosted in the facility. The design-versus-operated distinction is the honest read: a Tier IV-designed facility can run at Tier II reliability with poor operational discipline, since availability is delivered by maintenance programs (generator testing, UPS battery management, change-control rigor) as much as architecture. Converged failure modes deserve attention: the industry's major outages (cloud region failures) have often been systemic - software, configuration, or process failures - rather than classical power or cooling failures. Read with concurrent-maintainability performance (maintenance performed without downtime), change-management failure rate, and the availability-experience from the customer workload perspective rather than facility-green perspective.

## Formula

```
DCA = Uptime across Redundancy Tier / Total Time
```

## Unit

- **Unit reference:** `dea:unit-ratio-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** quality
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
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1090 (batch 4)
