# dea:metric-outcome-disparity-ratio

Canonical Performance Metric record for **Outcome Disparity Ratio (ODR)** in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-outcome-disparity-ratio`
- **Name:** Outcome Disparity Ratio
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate

## 2. Definition

Outcome Disparity Ratio (ODR) expresses how evenly a chosen outcome rate is distributed across documented affected groups - the highest group rate divided by the lowest group rate for that outcome, reported as a ratio where 1.0 indicates parity. It makes distributional effects visible so aggregate averages cannot hide which groups bear adverse outcomes; group definitions, attribute provenance, and small-cell suppression rules are part of any reported value. Lower values are better; gains are read as improvement and losses as deterioration. Its use is not sector-specific; it supports fairness, risk, and scope-expansion reviews.

## 3. Purpose

Make between-group outcome differences visible and governed. Use in fairness, risk, and scope-expansion reviews to test whether automated or delegated processes distribute outcomes and failures unevenly across affected groups.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** governance
- **Purpose classification:** governance, risk
- **Scope:** product_or_service
- **Directionality:** lower_is_better
- **Management significance:** managerial, regulatory

## 6. Unit or scale

- **Unit:** `dea:unit-ratio` (highest group rate / lowest group rate; 1.0 = parity)

## 7. Formula (CR-MET-005 binding)

```
ODR = max_g Rate_g / min_h Rate_h
```

Where `Rate_g` is the chosen outcome rate for affected group g, over the documented groups. The outcome measure and its orientation are recorded with the value; groups below the minimum cell volume are suppressed before the ratio is computed.

## 10. Frequency

Quarterly, and at every scope-expansion decision.

## 12. Applicability (CR-MET-007 cross-domain)

- **Intended subjects:** `dea:Outcome`, `dea:BusinessProcess`, `dea:Service`
- **Excluded subjects:** none

## 13. Relationships

- **External references:** broadens `mama-metrics:card/distributional-effects` (the card's headline disparity construct as a standalone record; see `external_references` in the record YAML)
- **Related records:** complements `dea:metric-control-effectiveness-rate` (control performance vs outcome distribution) and `dea:metric-customer-retention-rate` (an outcome rate ODR may be computed over)

## 14. Quality

- **Validation:** The outcome measure, its orientation, and group definitions with attribute provenance MUST be recorded with every value; below-minimum groups MUST be suppressed and the suppression stated.
- **Known limitations:** Parity at a uniformly poor level still reads 1.0; unchosen segment axes are invisible; legal constraints on group attributes vary by jurisdiction.

## 19. References

- MAMA (Measuring Automation & Measuring Autonomy) mama-metrics metric library v0.1.1 (CC-BY-4.0), card `distributional-effects`
- OpenDEAM dea-metamodel CR-MET-001 / CR-MET-005 / CR-MET-007 bindings
