# dea:metric-customer-retention-rate

Canonical Performance Metric record for **Customer Retention Rate (CRR)** in the OpenDEAM Metric catalog.

Lives in `entities/v1-alpha/dea:metric-customer-retention-rate/`. Lands as part of CR-MET-009 (catalog-establishment, 5-Metric pilot).

## 1. Identity

- **Canonical id:** `dea:metric-customer-retention-rate`
- **Name:** Customer Retention Rate
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** admitted

## 2. Definition

The percentage of customers from a defined starting cohort that remain customers at the end of the reporting period, excluding new acquisitions during the period. Higher values indicate greater loyalty of the existing customer base.

## 3. Purpose

Track customer loyalty of an existing cohort over time. Use to evaluate retention initiatives, identify cohort-level churn risk, and inform customer-experience decisions.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** customer
- **Purpose classification:** performance, satisfaction
- **Orientation:** lagging (reports realized historical conditions)
- **Scope:** business_unit, business_domain
- **Directionality:** higher_is_better
- **Management significance:** managerial, executive

## 5. Measurement subject

The customer base of a defined cohort (e.g., retail segment Q1 2025 customers).

## 6. Unit or scale

- **Unit:** `dea:unit-ratio-percent` (CR-MET-005 binding)
- **Scale:** percentage scale (0..100)
- **Precision:** 2 significant figures
- **Decimal scale:** 1 (one decimal place)
- **Rounding rule:** half_up

## 7. Formula (CR-MET-005 binding formula_definition)

```
CRR = (E - N) / S * 100
```

Where:
- `E` = customer count at end of period (`dea:metric-customer-count-end`)
- `N` = new customer acquisitions during the period (`dea:metric-new-customer-acquisitions`)
- `S` = customer count at start of period (`dea:metric-customer-count-start`)

**Validation rules:**
- result >= 0
- result <= 100
- S > 0 (denominator must be positive)

## 8. Inputs

| Input | Metric ref | Nature |
|-------|-----------|--------|
| E (customers at end) | `dea:metric-customer-count-end` | numeric |
| N (new acquisitions) | `dea:metric-new-customer-acquisitions` | numeric |
| S (customers at start) | `dea:metric-customer-count-start` | numeric |

## 9. Source

Authoritative customer data warehouse; cohort definition per the reporting-period specification.

## 10. Frequency

Quarterly.

## 12. Applicability (CR-MET-007 cross-domain)

- **Intended subjects:** `dea:BusinessCapability`, `dea:BusinessProcess`, `dea:Outcome`
- **Excluded subjects:** `dea:ApplicationComponent`

## 13. Relationships

- **Designations** (CR-MET-008): `dea:designation-customer-retention-kpi-lagging`, `dea:designation-customer-retention-kri-leading`
- **Related metrics:** leads_to `dea:metric-customer-satisfaction`; complements `dea:metric-customer-acquisition-cost`

## 14. Quality

- **Validation:** The reporting period MUST be a calendar quarter (Q1..Q4) or fiscal equivalent.
- **Known limitations:** Does not capture voluntary vs involuntary churn distinction; does not capture revenue-weighted retention (separate metric).

## 15. Governance

- **Accountable owner:** Retail VP (per `dea:designation-customer-retention-kpi-lagging`)
- **Risk owner:** Risk Officer (per `dea:designation-customer-retention-kri-leading`)
- **Stewardship:** deferred to CR-MET-010

## 16. Examples

If a retail segment starts the quarter with 10,000 customers, ends with 9,500 customers, and acquired 500 new customers during the quarter:

```
CRR = (9500 - 500) / 10000 * 100 = 90.0%
```

## 17. Limitations

- Bounded by cohort definition. A changing cohort definition makes year-over-year comparisons invalid.
- Does not capture customer lifetime value (separate metric).

## 18. Version

- **v1.0.0** (2026-10-18): Initial catalog admission (CR-MET-009 pilot).

## 19. References

- APQC Customer Relationship Management framework
- Balanced Scorecard customer perspective
- OpenDEAM dea-metamodel CR-MET-001 / CR-MET-002 / CR-MET-005 / CR-MET-006 / CR-MET-008 bindings