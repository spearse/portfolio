---
layout: default
title: Density Copilot
permalink: /projects/01-Density-Copilot.html
---

# Density Copilot - AI Music Production Assistant

Role: Lead Software Engineer / Design Lead (11 months, ongoing) • Scope: Natural-language to pro DJ arrangements; shipped VC demos; testing with pro DJs

## Overview
Joined to create an AI assistant that turns plain-English briefs into DJ-ready arrangements. Led architecture, language design, and integrations that made Copilot the centerpiece of fundraising demos and early pro-DJ testing.

## What I Built
- Desktop app (PyQt) with streaming LLM responses, live arrangement visualizer, and resilient DAW connections.
- DensityMark DSL plus streaming parser/validator so LLM output stays musically structured and recoverable mid-stream.
- Semantic audio search pipeline (MERT + Clamp3) delivered in <1 month; FAISS locally and Google Matching Engine in cloud.
- Ableton Live integration via socket protocol and Remote Script; multi-DAW strategy with Density DAW as next target.
- Intelligent palette curation that replaces fixed genre templates with LLM + semantic search for context-aware instruments.

## Impact
- Demos cited by VCs as a key differentiator; anchors fundraising conversations.
- Pro DJs using test builds report trusted arrangement quality and responsive UX (no “dead air” during generation).
- Semantic search indexes tens of thousands of samples; delivered from zero to production-ready in under a month.

## Technical Highlights
- Streaming parsing with incremental validation and partial recovery to keep UI live during LLM generation.
- Genre- and phrasing-aware prompts to enforce energy flow, bar alignment, and section structure.
- Connection resilience: health checks, auto-reconnect, graceful degradation when DAW is unavailable.
- Dual deployment for search: fast local FAISS for dev, managed Matching Engine for scale.

## Leadership
- Drove architecture across app, DSL, and search; aligned backend and ML teams on contracts and prompts.
- Established testing and docs for the multi-process app and pipelines to keep iteration safe under tight timelines.
