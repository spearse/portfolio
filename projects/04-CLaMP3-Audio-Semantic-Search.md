---
layout: default
title: CLaMP3 Audio Semantic Search
permalink: /projects/04-CLaMP3-Audio-Semantic-Search.html
---

# CLaMP3 Audio Semantic Search
Role: Lead Software Engineer (intensive 1-month build) • Context: Semantic search infra for Density Copilot • Tech: Python, PyTorch, MERT, CLaMP3, FAISS, FastAPI, Docker

## Overview
Built a semantic audio search pipeline in under a month so Copilot can find samples via natural language (e.g., “punchy techno kick”) and audio references. Replaced rigid genre templates with intelligent palette curation and shipped production-ready infra for tens of thousands of files.

## What I Built
- Two-stage embeddings: MERT features → CLaMP3 multimodal embeddings aligned with text/audio.
- Performance engine: Model reuse + batching for 15–30× speedup (naive 12s/file → 1–2s/file).
- FAISS index + FastAPI: Text, audio, and hybrid search with sub-100ms queries.
- Deployment: Dockerized service; sequential mode for constrained boxes, parallel mode for GCP GPUs.
- Resilience: Resume-capable checkpointing, file validation, health checks, automated index rebuilds.

## Impact
- Delivered research-to-prod pipeline in <1 month.
- Sub-100ms queries across 10K+ files; enabled Copilot’s palette curation.
- Replaced genre templates with context-aware discovery; validated by pro DJ testers.

## Key Technical Highlights
- Hybrid search (text+audio blend) in shared embedding space.
- Batch pipelines with worker pools and cached models to avoid reload costs.
- Dual deployment profiles from one codebase (resource-constrained vs. GPU-accelerated).
- Clear API contracts for Copilot integration; easy local vs. cloud swaps.

## Challenges & Solutions
- Memory limits in Docker: Sequential mode, lazy loading, aggressive cleanup.
- Cross-modal alignment: CLaMP3 embeddings to keep text/audio in one space.
- Production reliability: Idempotent checkpoints, validation, and health checks to survive bad files/ooms.
