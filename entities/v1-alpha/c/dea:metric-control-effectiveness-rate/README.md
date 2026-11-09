# dea:metric-control-effectiveness-rate

Canonical Performance Metric record for **Control Effectiveness Rate (CER)** in the OpenDEAM Metric catalog.

## 2. Definition

The ratio of effective control operations to total control operations, expressed as a percentage. Effective is the count of control operations where the control operated as designed; Total is the count of all control operations evaluated. Higher values indicate greater control effectiveness.

## 4. Classification

- **Subject classification:** governance
- **Purpose classification:** compliance, effectiveness
- **Orientation:** lagging
- **Scope:** enterprise, process
- **Directionality:** higher_is_better
- **Management significance:** operational, regulatory, external_disclosure

## 7. Formula

```
CER = Effective / Total * 100
```

## 12. Applicability

- **Intended subjects:** `dea:Control`, `dea:Policy`, `dea:BusinessProcess`

## 13. Relationships

- **Designations (CR-MET-008 KCI):** `dea:designation-control-effectiveness-kci`
- **Related metrics:** complements `dea:metric-risk-exposure-index`

## 19. References

- COSO Internal Control Integrated Framework
- SOX 404 control testing standards
- CR-MET-008 §5.3 (KCI designation requirements)
- CR-MET-007 (cross-domain applicability to Control)