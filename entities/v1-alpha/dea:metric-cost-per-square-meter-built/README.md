# dea:metric-cost-per-square-meter-built

Candidate Performance Metric record for **Cost per Square Meter Built** (CSMB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-cost-per-square-meter-built`
- **Name:** Cost per Square Meter Built
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** CSMB

## 2. Definition

Cost per Square Meter Built (CSMB) addresses how efficiently resources are converted into outputs and is a fixture of construction & engineering reporting. It is computed as Total Construction Cost / Gross Floor Area, expressed in currency per unit. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Lower values are better; each reduction is an improvement. Its use is concentrated in Construction & engineering.

## 3. Context

Construction cost divided by delivered area - the unit-cost metric that anchors the entire development feasibility arithmetic: land cost plus build cost against sale or rent value is the residual calculation every project is judged by, and construction cost per square metre is its largest variable. Its strategic significance is benchmark honesty: cost per square metre varies several-fold by building type (a warehouse and a hospital differ by an order of magnitude on mechanical systems alone), so the metric is only meaningful within building-class and quality-specification bands - the comparison error being the most common misuse in the industry. The honest read separates structure from finish from services, since each moves for different reasons (structure with commodity prices, services with design complexity, finish with specification choices) and the remediation levers differ. Read with the time dimension: cost inflation between tender and completion is the industry's chronic erosion mechanism, and the metric trended in real terms is what procurement strategies actually target.

## Formula

```
Total Construction Cost / Gross Floor Area
```

## Unit

- **Unit reference:** `dea:unit-currency`
- **Unit:** currency
- **Unit label (as published):** currency per unit

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:OrganizationalUnit
- **Reputability tier:** industry_standard
- **Domain:** construction_engineering
- **Sector:** construction_engineering

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 676 (batch 2)
