# dea:metric-mean-time-to-recovery

Canonical Performance Metric record for **Mean Time to Recovery (MTTR)** in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-mean-time-to-recovery`
- **Name:** Mean Time to Recovery
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** admitted

## 2. Definition

The arithmetic mean of recovery times across n incidents, expressed in minutes. Recovery time is measured from incident-detection to service-restoration. Lower values indicate faster recovery.

## 3. Purpose

Track service-restoration performance over time. Use to evaluate incident-management effectiveness, identify trends in recovery time, and inform operational-improvement decisions.

## 4. Classification (CR-MET-002 binding 6 axes)

- **Subject classification:** technology_architecture
- **Purpose classification:** performance, health
- **Orientation:** lagging
- **Scope:** system_or_component, service
- **Directionality:** lower_is_better
- **Management significance:** operational, managerial

## 6. Unit or scale

- **Unit:** `dea:unit-minute` (CR-MET-005 binding; time dimensionality)
- **Precision:** 3 significant figures
- **Decimal scale:** 1
- **Rounding rule:** half_up

## 7. Formula (CR-MET-005 binding)

```
MTTR = (sum_i RecoveryTime_i) / n
```

Where `RecoveryTime_i` is the recovery time of incident i in minutes, and n is the total number of incidents.

## 10. Frequency

Monthly.

## 12. Applicability (CR-MET-007 cross-domain)

- **Intended subjects:** `dea:ApplicationComponent`, `dea:BusinessService`, `dea:Service`
- **Excluded subjects:** `dea:Outcome`

## 13. Relationships

- **Designations (CR-MET-008):** `dea:designation-incident-frequency-operational`
- **Related metrics:** complements `dea:metric-system-availability`

## 14. Quality

- **Validation:** Recovery time MUST be measured from incident-detection to service-restoration.
- **Known limitations:** Detection latency is not captured (separate metric: Time to Detect).

## 19. References

- ITIL 4 incident management practice
- SRE workbook MTTR definitions
- OpenDEAM dea-metamodel CR-MET-001 / CR-MET-005 / CR-MET-007 bindings