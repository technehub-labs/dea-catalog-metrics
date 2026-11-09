# dea:metric-average-turns-to-resolution

Candidate Performance Metric record for **Average Turns to Resolution** (ATTR) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-average-turns-to-resolution`
- **Name:** Average Turns to Resolution
- **Type:** Metric
- **Version:** 1.1.0
- **Lifecycle:** candidate
- **Short form:** ATTR

## 2. Definition

Average Turns to Resolution (ATTR) addresses how efficiently resources are converted into outputs and is a fixture of conversational ai & chatbots reporting. It is defined as Conversation Turns before Resolution / Resolved Conversations; the result is stated in ratio (x:1 or x). It is applied across virtually every sector. It is a working-level control: thresholds trigger immediate operational response. Reduction is the goal, and sustained decreases indicate successful intervention.

## Formula

```
ATTR = Conversation Turns before Resolution / Resolved Conversations
```

## Unit

- **Unit reference:** `dea:unit-ratio`
- **Unit:** ratio
- **Unit label (as published):** ratio (x:1 or x)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** lower_is_better
- **Management significance:** operational
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** conversational_ai_chatbots

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1484 (batch 5)
