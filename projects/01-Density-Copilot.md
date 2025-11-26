---
layout: default
title: Density Copilot
permalink: /projects/01-Density-Copilot.html
---

# Density Copilot - AI Music Production Assistant

Role: Lead Software Engineer / Design Lead (11 months, ongoing) • Scope: Natural-language to pro DJ arrangements; shipped VC demos; testing with pro DJs

## Overview
Joined to create an AI assistant that turns plain-English briefs into DJ-ready arrangements. Led architecture, language design, and integrations that made Copilot the centerpiece of fundraising demos and early pro-DJ testing.

<div class="highlight-box" markdown="1">
Built a PyQt desktop app with streaming LLM responses and a custom DensityMark DSL so arrangements stay musically structured while generating. Added semantic audio search (MERT→CLaMP3, FAISS) in under a month, multi-DAW integration, and resilient connections for pro DJs.
</div>

## Impact
Demos cited by VCs as the key differentiator; pro DJs report trusted arrangement quality with no “dead air” during generation; semantic search indexes tens of thousands of samples delivered from zero to production-ready in under a month.

## How it works
- Desktop app: Streaming LLM UX with live arrangement visualizer and robust DAW connections.
- Language/structure: DensityMark DSL with streaming parser/validator to keep output musically valid and recoverable mid-stream.
- Search: MERT + CLaMP3 embeddings with FAISS (local) and Matching Engine (cloud) for text/audio/hybrid queries.
- DAW integration: Socket protocol + Remote Script for Ableton; strategy extends to Density DAW.
- Palette curation: LLM + semantic search replacing fixed genre templates with context-aware instruments.

## Leadership
Drove architecture across app, DSL, and search; aligned backend and ML teams on contracts and prompts; established testing and docs to keep iteration safe under tight timelines.
