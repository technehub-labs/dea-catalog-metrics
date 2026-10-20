# dea:metric-data-completeness

Canonical Performance Metric record for **Data Completeness (DC)** in the OpenDEAM Metric catalog.

## 2. Definition

The ratio of populated records to expected records for a defined data entity, expressed as a percentage. Expected is the total population of records required by the data entity definition; Populated is the count of records with non-null required attributes. Higher values indicate greater data completeness.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** information_architecture
- **Purpose classification:** quality, compliance
- **Orientation:** diagnostic (concurrent; surfaces current-state issues)
- **Scope:** enterprise, business_domain
- **Directionality:** higher_is_better
- **Management significance:** operational, regulatory

## 7. Formula

```
DC = Populated / Expected * 100
```

## 12. Applicability (CR-MET-007 cross-domain binding)

- **Intended subjects:** `dea:DataEntity`, `dea:BusinessCapability`

## 13. Relationships

- **Related metrics:** complements `dea:metric-data-accuracy`

## 19. References

- DAMA Data Management Body of Knowledge (DMBOK2)
- ISO 8000 data quality standard
- CR-MET-007 (cross-domain applicability to DataEntity)