---
layout: default
title: CLaMP3 Audio Semantic Search
permalink: /projects/04-CLaMP3-Audio-Semantic-Search.html
---

# CLaMP3 Audio Semantic Search
## Production ML Pipeline Built in < 1 Month

**Role:** Lead Software Engineer
**Duration:** < 1 month (intensive development)
**Context:** Infrastructure component for Density Copilot
**Technologies:** Python, PyTorch, MERT, CLaMP3, FAISS, Docker, FastAPI

---

<div class="highlight-box" markdown="1">

### 🎯 Key Achievements

- **Built in < 1 month** from research to production deployment with comprehensive features
- **15-30x performance optimization** through model reuse and batched inference strategies
- **Dual deployment strategy** supporting both local development (Docker) and cloud production (GCP)
- **Semantic understanding** enabling natural language queries like "punchy techno kick" to find matching audio
- **Sub-second queries** across tens of thousands of audio files using FAISS vector indexing
- **Production-grade quality** with error handling, resume-capable checkpointing, Docker containerization

</div>

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">&lt;1 Month</span>
    <span class="metric-label">Build Time<br>Research to Prod</span>
  </div>
  <div class="metric">
    <span class="metric-value">15-30×</span>
    <span class="metric-label">Performance<br>Speedup</span>
  </div>
  <div class="metric">
    <span class="metric-value">&lt;100ms</span>
    <span class="metric-label">Query Time<br>Typical</span>
  </div>
  <div class="metric">
    <span class="metric-value">10K+</span>
    <span class="metric-label">Audio Files<br>Indexed</span>
  </div>
</div>

## Overview

When building Density Copilot, we needed semantic audio search enabling the AI to find samples matching musical context. Traditional search (filename, tags) was insufficient—we needed "punchy techno kick" or "warm atmospheric pad" to retrieve sounds that match the description, not just keywords.

I built complete semantic audio search infrastructure in **under 1 month**, processing tens of thousands of files and enabling natural language queries with sub-second response times. This system replaced rigid genre templates with intelligent sample discovery, becoming critical to Copilot's palette curation.

---

## The Challenge

<div class="two-col">
  <div class="col-box" markdown="1">
    <h4>🎯 Search Requirements</h4>
    <ul>
      <li>Natural language descriptions ("punchy techno kick")</li>
      <li>Musical context matching (genre, style, palette)</li>
      <li>Audio similarity (find samples like this reference)</li>
      <li>Sub-second queries across tens of thousands of files</li>
    </ul>
  </div>
  <div class="col-box" markdown="1">
    <h4>⚡ Production Requirements</h4>
    <ul>
      <li>Reproducible deployment (Docker)</li>
      <li>Scalable to cloud (GCP)</li>
      <li>Easy Copilot integration</li>
      <li><strong>Timeline: &lt; 1 month</strong> from research to production</li>
    </ul>
  </div>
</div>

---

## Technical Implementation

### Two-Stage Embedding Pipeline

<div class="highlight-box" markdown="1">

**Stage 1: MERT Feature Extraction**
- Model: MERT-v1-95M (m-a-p/MERT-v1-95M)
- Output: 768-dimensional audio feature vectors
- Process: Time-averaged representations capturing musical characteristics

**Stage 2: CLaMP3 Global Embedding**
- Model: CLaMP3-SAAS (multimodal audio+text)
- Output: Global embeddings aligned with natural language
- Key: Text and audio embeddings in same space enabling cross-modal search

**Why Two Stages:** MERT provides robust acoustic features, CLaMP3 aligns with text descriptions

</div>

---

### Performance Optimization: 15-30x Speedup

**Initial Implementation:** ~12 seconds per file (naive approach)

**Optimized Implementation:** 1-2 seconds per file (production)

<div class="two-col">
  <div class="col-box" markdown="1">
    <h4>Sequential Processing</h4>
    <ul>
      <li><strong>Use case:</strong> Docker with limited memory</li>
      <li><strong>Performance:</strong> 8-12 seconds per file</li>
      <li>Process one file at a time</li>
      <li>Release GPU memory between files</li>
      <li>Runs on modest hardware</li>
    </ul>
  </div>
  <div class="col-box" markdown="1">
    <h4>Parallel Processing</h4>
    <ul>
      <li><strong>Use case:</strong> GCP VMs with GPUs</li>
      <li><strong>Performance:</strong> 1-2 seconds per file</li>
      <li>Batch multiple files simultaneously</li>
      <li>Model reuse (load once, process many)</li>
      <li>Worker pools for parallelization</li>
    </ul>
  </div>
</div>

**Critical Insight:** Loading models is expensive (seconds), inference is fast (milliseconds). Keep models in memory and batch process for 15-30x improvement.

---

### FAISS Vector Indexing

<div class="highlight-box" markdown="1">

**Index Structure:**
- Type: Flat L2 index for exact nearest neighbor search
- Dimension: 768 (CLaMP3 embedding size)
- Scale: Tens of thousands of audio files
- Query Time: Sub-second (typically <100ms)

**Search Modes:**
1. **Text-to-Audio:** "punchy techno kick" → matching samples
2. **Audio-to-Audio:** Reference sample → perceptually similar sounds
3. **Hybrid Search:** Blend text + audio queries with alpha weighting (e.g., 70% text, 30% audio)

</div>

---

### FastAPI Web Service

Built RESTful API for programmatic access:

```python
POST /search/text
{"query": "warm atmospheric pad", "top_k": 10}
→ Returns top 10 matching audio files with similarity scores

POST /search/audio
{"audio_path": "/path/to/reference.wav", "top_k": 10}
→ Returns similar-sounding audio files

POST /search/hybrid
{"query": "aggressive techno", "audio_path": "/path/to/ref.wav",
 "alpha": 0.7, "top_k": 10}
→ Returns blended search results (70% text, 30% audio)
```

---

### Docker Deployment

<div class="highlight-box" markdown="1">

**Containerization Features:**
- Python 3.8+ base image
- PyTorch with CPU optimization (production uses CPU inference)
- Hugging Face model auto-download
- Multi-stage build reducing image size
- Environment variable configuration

**Deployment Targets:**
- Local Development: Docker Compose for testing
- Production: Google Cloud Run (serverless) or GCP VMs
- CI/CD: Automated builds and deployments

</div>

---

## Key Technical Challenges Solved

<div class="two-col">
  <div class="col-box" markdown="1">
    <h4>Memory Constraints in Docker</h4>
    <p><strong>Problem:</strong> Loading MERT and CLaMP3 simultaneously exhausted container memory.</p>
    <p><strong>Solution:</strong> Sequential processing mode with aggressive cleanup, lazy model loading, dual deployment strategy.</p>
  </div>
  <div class="col-box" markdown="1">
    <h4>15-30x Performance Optimization</h4>
    <p><strong>Problem:</strong> Initial ~12s per file made batch processing impractical.</p>
    <p><strong>Solution:</strong> Model reuse, batch processing, worker pools, caching intermediate features. Result: 1-2s per file.</p>
  </div>
  <div class="col-box" markdown="1">
    <h4>Cross-Modal Alignment</h4>
    <p><strong>Problem:</strong> Text and audio in different spaces—how to search text queries against audio embeddings?</p>
    <p><strong>Solution:</strong> CLaMP3 model trained to align audio and text in shared semantic space enabling cross-modal search.</p>
  </div>
  <div class="col-box" markdown="1">
    <h4>Production Reliability</h4>
    <p><strong>Problem:</strong> ML pipelines can fail (OOM, corrupt files, missing data).</p>
    <p><strong>Solution:</strong> Resume-capable checkpointing, file validation, error logging, automated FAISS index rebuilding, health checks.</p>
  </div>
</div>

---

## Results & Impact

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">12s → 1-2s</span>
    <span class="metric-label">Processing Time<br>Per File</span>
  </div>
  <div class="metric">
    <span class="metric-value">&lt;100ms</span>
    <span class="metric-label">Query Time<br>Typical</span>
  </div>
  <div class="metric">
    <span class="metric-value">10K+</span>
    <span class="metric-label">Files<br>Processed</span>
  </div>
  <div class="metric">
    <span class="metric-value">✓</span>
    <span class="metric-label">DJ<br>Validated</span>
  </div>
</div>

### Integration Success

**Copilot Palette Curation:**
- Replaced rigid genre templates with flexible semantic discovery
- LLM determines needed instruments → Semantic search finds appropriate samples
- Context-aware matching (genre + user style + text description)
- Professional DJ validation confirmed quality

**Example Workflow:**
1. User requests: "warm melodic techno at 124 BPM"
2. Copilot LLM analyzes request, determines needed instruments
3. For each instrument, LLM generates semantic description
4. CLaMP3 search finds samples matching descriptions + musical context
5. Palette loaded with musically coherent samples

---

### Development Speed

<div class="highlight-box" markdown="1">

**Complete system delivered in < 1 month:**
- Week 1: Research, model selection, initial prototype
- Week 2: Batch processing pipeline, optimization
- Week 3: FastAPI service, Docker deployment
- Week 4: Production deployment, integration with Copilot

**Demonstrates:** Ability to rapidly acquire ML/AI domain knowledge and deliver production systems under tight deadlines.

</div>

---

## Technologies Used

**ML/AI:** PyTorch, Transformers (Hugging Face), MERT-v1-95M, CLaMP3-SAAS, FAISS, NumPy

**Backend:** FastAPI, Pydantic, Uvicorn, Python 3.8+

**Infrastructure:** Docker & Docker Compose, Google Cloud Platform, Google Cloud Run, GCP VMs, YAML configuration

---

## What Makes This Special

<div class="highlight-box" markdown="1">

**Rapid Execution:** Complete ML pipeline in < 1 month while maintaining production quality. Shows ability to learn new domains quickly.

**Performance Engineering:** 15-30x optimization through understanding bottlenecks and implementing model reuse, batching, parallel processing.

**Production-Grade Quality:** Comprehensive error handling, resume-capable checkpointing, Docker deployment, configuration management. Built for real use.

**Dual Deployment Strategy:** Sequential processing for resource-constrained environments, parallel processing for performance—one codebase, multiple optimization profiles.

**Practical ML Application:** Solves real problems for professional musicians. Semantic search enables workflows impossible with traditional keyword search.

</div>

---

## Career Significance

CLaMP3 Audio Semantic Search demonstrates:

- **ML/AI capability** - Rapid acquisition of new technical domains (embedding models, vector search, multimodal learning)
- **Performance optimization** - 15-30x speedup through systematic profiling
- **Production engineering** - Docker deployment, configuration management, error handling
- **Fast execution** - Complete pipeline in < 1 month under business pressure
- **Integration thinking** - Designed for easy integration with Copilot LLM workflows

This project bridges classical audio engineering with modern AI/ML, showing ability to stay at cutting edge of music technology.

---

**Related Projects:**
- [Density Copilot](01-Density-Copilot.html) - AI assistant using semantic search for intelligent palette curation
- [Density DAW](02-Density-DAW.html) - Professional DAW where discovered samples are ultimately used

**Technical Resources:**
- MERT: [Musical Expression Recognition Transfer](https://huggingface.co/m-a-p/MERT-v1-95M)
- CLaMP3: Contrastive Language-Audio Pretraining (multimodal embeddings)
- FAISS: [Facebook AI Similarity Search](https://github.com/facebookresearch/faiss)
