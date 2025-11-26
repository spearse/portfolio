---
layout: default
title: Density Web Platform - Business Model Transformation
permalink: /projects/05-Density-Web-Platform.html
---

# Density Web Platform - Business Model Transformation

Role: Full-Stack Engineer (1 year; 2-month RTO build) • Context: Same company as Density DAW, supporting web platform team

## Overview
Partnered with the web platform team to pivot from subscriptions to perpetual and rent-to-own (RTO) licensing with hardware bundles, without breaking existing subscribers.

<div class="highlight-box" markdown="1">
Built and shipped rent-to-own/perpetual licensing in ~2 months: NestJS/TypeScript state machine, Chargebee webhooks with locking/idempotency, React flows for RTO progress and hardware checkout, and a discount engine covering promos/bundles/price floors.
</div>

## Impact
New purchase paths ($200 one-time, $15×14 RTO) launched with zero production billing issues; legacy subscribers remained intact; discount/bundle logic increased flexibility while preventing revenue leakage.

## How it works
- Lifecycle: RTO state machine handling 14 payments, early buyout, and backward-compatible subscriptions.
- Billing sync: Chargebee webhooks with database-backed locks to survive pod restarts and avoid races/duplicates.
- Frontend: React dashboards for RTO progress, hardware checkout with dynamic discounts, payment method management.
- Discounts: Engine covering RTO progress, promos, bundles, and price floors; unit/integration tested across combinations.
- Infra: GCP (Cloud Run, Secret Manager), Postgres/TypeORM, automated QA environments.

## Collaboration
Partnered with QA on scenario matrices (late payments, early buyout, promos, legacy migrations) and documented flows for support/finance with full auditability across billing events.
