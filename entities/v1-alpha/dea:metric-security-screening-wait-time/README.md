# dea:metric-security-screening-wait-time

Candidate Performance Metric record for **Security Screening Wait Time** (SSWT) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-security-screening-wait-time`
- **Name:** Security Screening Wait Time
- **Type:** Metric
- **Version:** 1.0.1
- **Lifecycle:** candidate
- **Short form:** SSWT

## 2. Definition

A Airport Operations indicator, Security Screening Wait Time (SSWT) quantifies the quality of outputs and outcomes. It is computed as Median Passenger Wait at Checkpoint, expressed in minutes. Its use is concentrated in Airports. It is a headline indicator: movement in it prompts leadership questions about strategy and resourcing. Reduction is the goal, and sustained decreases indicate successful intervention.

## 3. Context

Security screening wait time measures queue length from joining to clearing the checkpoint, and it is the gate-flow constraint of airport operations - checkpoints are the passenger-journey bottleneck whose throughput caps effective terminal capacity, and wait-time experience shapes passenger perception of the entire airport. The trade-off structure is direct: staffing and lane capacity against demand peaks, where conservative processing rules (pat-downs, additional screening) reduce throughput. The measurement sophistication is queue-modeling: airports increasingly use real-time queue analytics to predict and manage waits rather than merely report them. Wait time is also a security metric inversely - rushed checkpoints invite procedural shortcuts. Read with throughput per lane-hour, checkpoint utilization versus capacity, passenger satisfaction correlation, and pre-check or trusted-traveler share which structurally lifts throughput.

## Formula

```
Median Passenger Wait at Checkpoint
```

## Unit

- **Unit reference:** `dea:unit-minute`
- **Unit:** minute
- **Unit label (as published):** minutes

## Classification

- **Subject classification:** business_architecture
- **Purpose classification:** quality
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** airport_operations
- **Sector:** airports

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1177 (batch 4)
