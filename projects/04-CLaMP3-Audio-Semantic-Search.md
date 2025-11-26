---
layout: default
title: CLaMP3 Audio Semantic Search
permalink: /projects/04-CLaMP3-Audio-Semantic-Search.html
---

# CLaMP3 Audio Semantic Search
Role: Lead Software Engineer (intensive 1-month build) • Context: Semantic search infra for Density Copilot • Tech: Python, PyTorch, MERT, CLaMP3, FAISS, FastAPI, Docker

## Overview
Built a semantic audio search pipeline in under a month so Copilot can find samples via natural language (e.g., “punchy techno kick”) and audio references. Replaced rigid genre templates with intelligent palette curation and shipped production-ready infra for tens of thousands of files.

<div class="highlight-box" markdown="1">
Delivered a text/audio semantic search pipeline in under a month: MERT→CLaMP3 embeddings, FAISS index with FastAPI, and dual deployment (local vs. GCP GPU) with 15–30× speedup from batching/model reuse. Built resilience with checkpoints, validation, and automated index rebuilds.
</div>

## Impact
Research-to-prod in <1 month; sub-100ms queries across 10K+ files; Copilot palette curation shifted from rigid templates to context-aware discovery validated by pro DJs.

## How it works
- Two-stage embeddings: MERT features feeding CLaMP3 multimodal embeddings aligned with text/audio.
- Performance: Model reuse + batching (12s/file naive → 1–2s/file); worker pools tuned per deployment profile.
- Search/API: FAISS index with FastAPI endpoints for text, audio, and hybrid queries.
- Deployment: Dockerized; sequential mode for constrained boxes, parallel mode for GCP GPUs.
- Resilience: Resume-capable checkpointing, file validation, health checks, automated index rebuilds.

## Challenges
- Memory limits in Docker → sequential mode, lazy loading, aggressive cleanup.
- Cross-modal alignment → CLaMP3 to keep text/audio in one embedding space.
- Production reliability → idempotent checkpoints and validation to survive bad files/OOMs.
