---
layout: default
title: Density Web Platform
permalink: /projects/05-Density-Web-Platform.html
---

# Density Web Platform - Business Model Transformation

Role: Full-Stack Engineer (1 year; 2-month RTO build) • Context: Same company as Density DAW, supporting web platform team

## Overview
Partnered with the web platform team to pivot from subscriptions to perpetual and rent-to-own (RTO) licensing with hardware bundles, without breaking existing subscribers.

## What I Built
- RTO state machine (NestJS/TypeScript) handling 14-payment lifecycle, early buyout, and backward-compatible subscriptions.
- Chargebee webhook pipeline with locking/idempotency to keep billing state and database in sync.
- React frontend: RTO progress dashboard, hardware checkout with dynamic discounts, payment method management.
- Discount engine covering RTO progress, promos, bundles, and price floors; tested against combinatorial edge cases.
- Database-backed subscription locks to survive pod restarts and prevent race conditions.

## Impact
- Delivered the RTO system in ~2 months with zero production billing issues.
- Enabled new purchase paths ($200 one-time, $15×14 RTO) while keeping legacy subscribers intact.
- Hardware bundling/discount logic increased flexibility and prevented revenue leakage from discount stacking.

## Technical Highlights
- Precedence rules and minimum price floors enforced via unit/integration tests for discount combinations.
- Webhook retries/duplicates handled safely; race-free via database locks instead of in-memory caches.
- Deployed on GCP (Cloud Run, Secret Manager) with Postgres/TypeORM and automated QA environments.

## Collaboration & Quality
- Partnered with QA on scenario matrices (late payments, early buyout, promos, legacy migrations).
- Documented flows for support/finance and ensured auditability across billing events.
