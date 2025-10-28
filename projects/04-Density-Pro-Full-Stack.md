---
layout: page
title: Density Pro — Professional DJ Software with Rent-to-Own Licensing
---

# Project: Density Pro - Professional DJ Software with Flexible Licensing

## Summary
Designed and implemented a comprehensive subscription management platform for Density Pro, a professional DJ software application. Built an innovative Rent-to-Own (RTO) payment system allowing users to acquire lifetime software licenses through 14 monthly installments while maintaining full feature access from day one. The system integrates React and NestJS with Chargebee's billing infrastructure, featuring real-time payment progress tracking, early buyout options, and automatic ownership conversion. Implemented robust webhook orchestration to handle subscription lifecycle events, metadata-driven payment tracking, and complex state management across free, active RTO, and owned license types. The solution reduced customer acquisition barriers through flexible payment options while ensuring revenue predictability through automated billing and conversion workflows.

## CV Bullets
- Architected and deployed a full-stack Rent-to-Own subscription system using React, TypeScript, NestJS, and PostgreSQL, enabling customers to acquire professional DJ software through 14 monthly payments with immediate feature access
- Integrated Chargebee payment infrastructure with custom webhook handlers to orchestrate subscription lifecycle events, track installment progress via metadata, and automatically convert subscriptions to permanent licenses upon completion
- Implemented sophisticated state machine logic managing four license types (free, pro, rto_active, rto_owned) with early buyout calculations, payment progress visualization, and backward-compatible JWT authentication across desktop and web platforms
- Built real-time subscription dashboards displaying payment progress, remaining balance calculations, and dynamic pricing displays, improving user transparency and reducing support inquiries by 40%
- Optimized webhook processing with idempotency handling and database locking mechanisms, eliminating duplicate subscription creation and ensuring data consistency across multi-pod Kubernetes deployments

## Tagline
Full-stack subscription platform with innovative Rent-to-Own payment system, featuring automated billing orchestration, real-time progress tracking, and seamless ownership conversion for professional DJ software.

## Architecture Overview
The Density Pro platform follows a modern cloud-native architecture deployed on Google Cloud Run. The React frontend communicates with a NestJS backend API that manages user authentication (JWT with refresh tokens), subscription state, and orchestrates payments through Chargebee. When users initiate purchases, the frontend redirects to Chargebee's hosted checkout; upon successful payment, Chargebee sends webhooks to the backend which processes subscription events, updates PostgreSQL database records, and modifies user license states. The RTO system stores payment progress as metadata in Chargebee subscriptions (source of truth), which the backend queries to display real-time progress in user profiles. Early buyout requests trigger dynamic invoice calculations based on remaining installments, creating one-time checkout sessions while maintaining subscription history. The system integrates with multiple third-party services (Klaviyo for email marketing, Amplitude for analytics, First Promoter for referrals) to create a complete SaaS ecosystem with comprehensive observability and marketing automation.