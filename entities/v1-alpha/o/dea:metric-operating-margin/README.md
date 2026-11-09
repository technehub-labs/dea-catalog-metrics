# dea:metric-operating-margin

Canonical Performance Metric record for **Operating Margin (OM)** in the OpenDEAM Metric catalog.

## 2. Definition

The ratio of operating income to revenue, expressed as a percentage. Operating income excludes non-operating items (interest, taxes, extraordinary items). Higher values indicate greater operational efficiency.

## 3. Purpose

Track operational efficiency over time. Use to evaluate segment profitability, identify cost-structure issues, and inform strategic decisions about pricing and operational investment.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** financial
- **Purpose classification:** performance, value_delivery
- **Orientation:** lagging
- **Scope:** enterprise, business_unit
- **Directionality:** higher_is_better
- **Management significance:** strategic, external_disclosure, executive

## 7. Formula (CR-MET-005 binding)

```
OM = OperatingIncome / Revenue * 100
```

**Aggregation across segments** (CR-MET-005 §3.3 binding):
- Use `WEIGHTED_MEAN` operator with `weight_basis: numerator_denominator`.
- DO NOT average the segment percentages directly (CR-MET-005 binding: ratios MUST NOT be automatically averaged).

## 12. Applicability

- **Intended subjects:** `dea:Outcome`, `dea:StrategicObjective`, `dea:BusinessCapability`

## 13. Relationships

- **Designations:** `dea:designation-revenue-recognition-lagging`
- **Related metrics:** `dea:metric-ebit`, `dea:metric-revenue`

## 19. References

- IFRS 15 revenue recognition
- GAAP income statement structure
- CR-MET-005 §3.3 (ratio aggregation rule)
- CR-MET-007 (cross-domain applicability to Outcome)