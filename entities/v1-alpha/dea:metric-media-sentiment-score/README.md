# dea:metric-media-sentiment-score

Candidate Performance Metric record for **Media Sentiment Score** (MSS-C) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-media-sentiment-score`
- **Name:** Media Sentiment Score
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** MSS-C

## 2. Definition

A Corporate Communications & PR indicator, Media Sentiment Score (MSS-C) quantifies the engagement or satisfaction of the people involved. Its calculation is Weighted Average of Positive and Negative Tone across Coverage, measured in score (points). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Media sentiment score quantifies the tone of brand mentions across news, social, and broadcast coverage, typically on a positive-negative scale powered by NLP classifiers. Its value is directional and early-warning: sentiment shifts precede sales impact and give comms teams a window to respond before narratives harden. The honest read requires skepticism about both coverage and classification - sarcasm, context, and industry-specific language defeat naive models, so always sample raw classified mentions to validate the model on your own domain. Blended scores hide what matters: a slight negative shift driven by one high-authority outlet is categorically different from broad mild negativity. Read with share of voice, message pull-through, and sentiment by audience segment and reach-weighted by outlet authority.

## Formula

```
Weighted Average of Positive and Negative Tone across Coverage
```

## Unit

- **Unit reference:** `dea:unit-score`
- **Unit:** score
- **Unit label (as published):** score (points)

## Classification

- **Subject classification:** organization
- **Purpose classification:** engagement
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:BusinessProcess
- **Reputability tier:** industry_standard
- **Domain:** corporate_communications_pr

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 786 (batch 2)
