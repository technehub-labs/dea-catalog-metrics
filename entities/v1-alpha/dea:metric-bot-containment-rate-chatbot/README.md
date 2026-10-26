# dea:metric-bot-containment-rate-chatbot

Candidate Performance Metric record for **Bot Containment Rate (Chatbot)** (BCR-CB) in the OpenDEAM Metric catalog.

## 1. Identity

- **Canonical id:** `dea:metric-bot-containment-rate-chatbot`
- **Name:** Bot Containment Rate (Chatbot)
- **Type:** Metric
- **Version:** 1.0.0
- **Lifecycle:** candidate
- **Short form:** BCR-CB

## 2. Definition

Bot Containment Rate (Chatbot) (BCR-CB) captures how efficiently resources are converted into outputs for organizations tracking conversational ai & chatbots. Its calculation is Conversations Resolved without Human Agent / Conversations, measured in percent (%). It is applied across virtually every sector. It informs long-horizon decisions and is typically tracked on enterprise dashboards rather than team boards. It should be maximized within the limits of cost and quality trade-offs.

## 3. Context

Measures the share of chat sessions the bot closes without human escalation. It is the headline efficiency metric for conversational AI, but containment quality is the difference between cost saving and customer abuse: bad containment deflects contact, drives channel-shifting calls, and damages brand. Always pair with post-chat satisfaction, repeat-contact rates, and intent-level breakdowns. Read with escalation reasons and containment versus resolution distinction.

## Formula

```
Conversations Resolved without Human Agent / Conversations
```

## Unit

- **Unit reference:** `dea:unit-percent`
- **Unit:** percent
- **Unit label (as published):** percent (%)

## Classification

- **Subject classification:** technology_architecture
- **Purpose classification:** efficiency
- **Scope classification:** capability
- **Directionality:** higher_is_better
- **Management significance:** strategic
- **Measurable entity kind:** dea:ApplicationComponent
- **Reputability tier:** industry_standard
- **Domain:** conversational_ai_chatbots

## Attribution

- **Source credit:** Public domain - no attribution required

## Provenance

- **Established by:** CR-MET-016 on 2026-10-26
- **Seed workbook:** `seeds/open-deam-candidate-metrics-seed.xlsx`, sheet `Candidate Metrics`, row 1480 (batch 5)
