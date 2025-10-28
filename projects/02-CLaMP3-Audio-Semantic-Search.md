---
layout: page
title: CLaMP3 Audio Semantic Search — Multimodal Audio Retrieval
---

# Project: CLaMP3 Audio Semantic Search System

## Summary

Developed a production-ready semantic audio search engine leveraging CLaMP3 multimodal embeddings and MERT audio features to enable intelligent, natural language-based audio retrieval. The system processes audio files through a two-stage pipeline: MERT feature extraction (768-dimensional acoustic representations) followed by CLaMP3 global embedding generation (multimodal semantic space aligned with text). Built a FastAPI web service with three search modes—audio-to-audio similarity, text-to-audio retrieval ("warm atmospheric pad"), and hybrid search with adjustable alpha blending—backed by FAISS vector indexing for millisecond-scale queries across thousands of files. Engineered scalable batch processing infrastructure supporting both memory-constrained Docker environments (sequential processing, ~8-12s/file) and high-performance GCP VMs (parallel processing with 16 workers, ~1-2s/file), achieving 15-30x performance improvements. Designed comprehensive tooling including resume-capable checkpointing, automated FAISS index rebuilding, and a modular configuration system. The platform enables creative professionals to search sound libraries using natural language descriptions, find perceptually similar sounds, or blend audio reference with text guidance, dramatically accelerating sound design workflows.

## CV Bullets

- Architected and deployed a semantic audio search system using CLaMP3 multimodal embeddings and MERT acoustic features, enabling natural language queries ("deep bass kick") to retrieve perceptually similar audio from large sound libraries with sub-second latency via FAISS vector indexing.

- Engineered scalable batch encoding pipeline with two optimization strategies: memory-safe sequential processing for Docker containers (8-12s/file) and parallel multiprocessing for high-performance VMs (1-2s/file with 16 workers), achieving 15-30x throughput improvements while processing 12,000+ audio files on Google Cloud Platform.

- Developed FastAPI REST service with hybrid search capabilities, combining audio reference files and text descriptions using alpha-weighted vector blending, providing interactive web interface and programmatic API access for audio-to-audio, text-to-audio, and multimodal similarity queries.

- Implemented production-grade features including resume-capable checkpointing, automated FAISS index rebuilding, modular YAML-based configuration management, and Docker containerization for reproducible deployment across local development and cloud environments.

- Integrated state-of-the-art audio AI models (MERT-v1-95M for acoustic feature extraction, CLaMP3-SAAS for multimodal semantic embeddings) into a two-stage processing pipeline that projects raw audio into a 768-dimensional semantic space aligned with natural language for cross-modal retrieval.

## Tagline

Semantic audio search engine combining CLaMP3 multimodal embeddings with FAISS indexing to enable millisecond-scale natural language queries across sound libraries—find "warm atmospheric pads" or blend audio reference with text guidance using hybrid alpha-weighted search.

## Architecture Overview

The system follows a three-layer architecture with clear separation between preprocessing, indexing, and retrieval. Audio files flow through a two-stage encoding pipeline: first, MERT-v1-95M extracts acoustic features (time-averaged 768-dim representations), then CLaMP3-SAAS projects these into a multimodal semantic space aligned with text embeddings. The preprocessing layer supports both sequential processing (for memory-constrained Docker containers) and parallel multiprocessing (utilizing 16+ workers on high-performance GCP VMs). Encoded embeddings are stored as NumPy arrays and indexed using FAISS for efficient similarity search. The API layer (FastAPI) handles three query modes: audio-to-audio uses direct embedding similarity, text-to-audio encodes natural language descriptions via CLaMP3's text encoder, and hybrid search performs alpha-weighted vector blending between audio and text embeddings. A static HTML frontend provides interactive search with real-time results and audio preview. The system uses YAML-based configuration for environment-agnostic deployment, with Docker Compose for local development and automated GCP deployment scripts for production-scale processing. All components communicate via file-based exchange (NPY embeddings, FAISS index, JSON path mappings), enabling modular scaling and easy integration with existing audio workflows.