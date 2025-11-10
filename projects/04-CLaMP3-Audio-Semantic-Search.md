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
**Scope:** Complete ML pipeline from encoding to production deployment
**Technologies:** Python, PyTorch, MERT, CLaMP3, FAISS, Docker, FastAPI

---

## Overview

When building Density Copilot, we needed a way for the AI assistant to find appropriate audio samples matching musical context. Traditional search (filename, tags) was insufficient—we needed semantic understanding: "punchy techno kick" or "warm atmospheric pad" should retrieve samples that *sound* like the description, not just match keywords.

I built a complete semantic audio search infrastructure in **under 1 month**, processing tens of thousands of audio files and enabling natural language queries with sub-second response times. This system replaced rigid genre templates with intelligent sample discovery, becoming a critical component of Copilot's palette curation.

**Key Achievement:** Delivered production-ready ML pipeline with 15-30x performance optimization through batched inference, deployed to both local development (Docker) and cloud production (Google Cloud Platform).

---

## The Challenge

**Problem:** Copilot needed to find audio samples matching:
1. **Natural language descriptions** ("punchy techno kick", "deep atmospheric bass")
2. **Musical context** (genre, style, existing palette)
3. **Audio similarity** (find samples like this reference)

**Requirements:**
- **Fast queries:** Sub-second search across tens of thousands of files
- **Semantic understanding:** "warm pad" should match sounds, not just filenames
- **Multiple search modes:** Text-to-audio, audio-to-audio, hybrid
- **Production deployment:** Reproducible, scalable, maintainable
- **Integration:** Easy to integrate with Copilot's LLM-driven palette curation

**Timeline:** < 1 month from research to production deployment

---

## Technical Implementation

### Two-Stage Embedding Pipeline

Designed a pipeline converting audio into searchable semantic vectors:

**Stage 1: MERT Feature Extraction**
- **Model:** MERT-v1-95M (m-a-p/MERT-v1-95M from Hugging Face)
- **Purpose:** Extract acoustic features from raw audio
- **Output:** 768-dimensional audio feature vectors
- **Process:** Time-averaged representations capturing musical characteristics

**Stage 2: CLaMP3 Global Embedding**
- **Model:** CLaMP3-SAAS (multimodal audio+text model)
- **Purpose:** Project audio features into shared semantic space with text
- **Output:** Global embeddings aligned with natural language
- **Key Feature:** Text and audio embeddings exist in same space, enabling cross-modal search

**Why Two Stages:**
- MERT provides robust acoustic features
- CLaMP3 aligns those features with text descriptions
- Separation allows optimization and caching strategies

---

### Batch Processing Infrastructure

Built scalable encoding system with two optimization strategies:

**Sequential Processing (Memory-Safe):**
- **Use case:** Docker containers with limited memory
- **Performance:** 8-12 seconds per file
- **Strategy:** Process one file at a time, release GPU memory between files
- **Benefit:** Runs on modest hardware without OOM errors

**Parallel Processing (High-Performance):**
- **Use case:** Google Cloud VMs with multiple GPUs
- **Performance:** 1-2 seconds per file (with 16 workers)
- **Strategy:** Batch multiple files through model simultaneously
- **Optimization:** 15-30x speedup through model reuse and batching

**Model Reuse Optimization:**

Critical insight: Loading models is expensive (seconds), inference is fast (milliseconds). By keeping models in memory and batching:
```python
# Inefficient: Load model for each file
for audio_file in files:
    model = load_model()  # Expensive!
    embedding = model.encode(audio_file)
    # ~12s per file

# Optimized: Load once, batch process
model = load_model()  # Once
for batch in batched(files, batch_size=16):
    embeddings = model.encode_batch(batch)  # Fast!
    # ~1-2s per file (15-30x faster)
```

---

### FAISS Vector Indexing

Implemented fast similarity search using Facebook's FAISS library:

**Index Structure:**
- **Type:** Flat L2 index for exact nearest neighbor search
- **Dimension:** 768 (CLaMP3 embedding size)
- **Scale:** Tens of thousands of audio files
- **Query Time:** Sub-second (milliseconds for most queries)

**Index Building:**
- Automated scripts collecting all .npy embedding files
- Rebuild index when new samples added
- Validation ensuring embeddings match file paths

**Search Modes:**

1. **Text-to-Audio:**
   - User query: "punchy techno kick"
   - Encode text via CLaMP3 text encoder
   - Search FAISS index for nearest audio embeddings
   - Return matching audio files

2. **Audio-to-Audio:**
   - User provides reference audio file
   - Encode audio via MERT + CLaMP3 pipeline
   - Search for perceptually similar sounds
   - Return audio files with similar characteristics

3. **Hybrid Search:**
   - Combine text description + audio reference
   - Alpha-weighted blending: `embedding = α × text_emb + (1-α) × audio_emb`
   - User controls blend ratio (e.g., 70% text, 30% audio)
   - Search combined embedding vector
   - Enables "sounds like this but more aggressive" queries

---

### FastAPI Web Service

Built RESTful API for programmatic and interactive access:

**Endpoints:**

```python
POST /search/text
{
  "query": "warm atmospheric pad",
  "top_k": 10
}
→ Returns top 10 matching audio files with similarity scores

POST /search/audio
{
  "audio_path": "/path/to/reference.wav",
  "top_k": 10
}
→ Returns similar-sounding audio files

POST /search/hybrid
{
  "query": "aggressive techno",
  "audio_path": "/path/to/reference.wav",
  "alpha": 0.7,  // 70% text, 30% audio
  "top_k": 10
}
→ Returns blended search results
```

**Features:**
- JSON API for programmatic access
- CORS enabled for web frontend
- File serving for audio playback
- Error handling and validation

---

### Docker Deployment

Containerized for reproducible deployment:

**Dockerfile Features:**
- Python 3.8+ base image
- PyTorch with CPU optimization (production uses CPU inference)
- Hugging Face model auto-download
- Multi-stage build reducing image size
- Environment variable configuration

**Docker Compose:**
```yaml
services:
  clamp3-search:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./embeddings:/app/embeddings
      - ./audio:/app/audio
    environment:
      - MODEL_CACHE_DIR=/app/models
      - FAISS_INDEX_PATH=/app/embeddings/index.faiss
```

**Deployment Targets:**
- **Local Development:** Docker Compose for testing
- **Production:** Google Cloud Run (serverless) or GCP VMs
- **CI/CD:** Automated builds and deployments

---

### Configuration Management

YAML-based configuration for environment-agnostic deployment:

```yaml
# config.yaml
processing:
  batch_size: 16
  num_workers: 4
  device: "cuda"  # or "cpu"

models:
  mert_model: "m-a-p/MERT-v1-95M"
  clamp3_model: "microsoft/clap-saas-latest"
  cache_dir: "/app/models"

paths:
  audio_dir: "/data/audio"
  embeddings_dir: "/data/embeddings"
  index_path: "/data/index.faiss"

search:
  default_top_k: 10
  max_top_k: 100
```

Allows easy configuration for different environments without code changes.

---

## Technical Challenges Solved

### 1. Memory Constraints in Docker

**Problem:** Loading both MERT and CLaMP3 models simultaneously exhausted memory in Docker containers.

**Solution:**
- Sequential processing mode with aggressive memory cleanup
- Lazy model loading (load only when needed)
- Chunk-based processing with explicit garbage collection
- Dual deployment strategy: Docker (sequential) for dev, GCP VMs (parallel) for production

---

### 2. 15-30x Performance Optimization

**Problem:** Initial implementation took ~12 seconds per file, making batch processing of thousands of files impractical.

**Solution:**
- Model reuse: Load once, process many files
- Batch processing: Process multiple files simultaneously
- Worker pools: Parallelize across CPU cores
- Caching: Store intermediate MERT features
- Result: 1-2 seconds per file on optimized hardware

---

### 3. Cross-Modal Alignment

**Problem:** Text descriptions and audio features exist in different spaces—how to search text queries against audio embeddings?

**Solution:**
- CLaMP3 model trained to align audio and text in shared semantic space
- Same embedding dimension for both modalities
- Cosine similarity works across text-audio pairs
- Enables "find audio matching this text" without complex translation

---

### 4. Production Reliability

**Problem:** ML pipelines can fail (OOM, corrupt files, missing data), need graceful handling.

**Solution:**
- Resume-capable checkpointing: Save progress, resume from failure point
- File validation before processing (check duration, sample rate, channels)
- Error logging with file-level granularity
- Automated FAISS index rebuilding with validation
- Health check endpoints for monitoring

---

### 5. Integration with Copilot

**Problem:** Copilot LLM needs to query search system, interpret results, and select appropriate samples.

**Solution:**
- Simple JSON API easy for LLM-generated code to call
- Return similarity scores enabling LLM to filter results
- File path mapping allowing direct sample loading
- Metadata (BPM, key, genre) included for musical filtering
- Context-aware search: LLM describes desired characteristics, search finds matches

---

## Results & Impact

### Performance Metrics

**Processing Speed:**
- **Initial:** ~12 seconds per file (naive implementation)
- **Optimized:** 1-2 seconds per file on GCP VMs with 16 workers
- **Improvement:** 15-30x speedup

**Search Performance:**
- **Query Time:** Sub-second (typically <100ms)
- **Index Size:** Tens of thousands of audio files
- **Accuracy:** High-quality semantic matches validated by professional DJs

**Scale:**
- Processed tens of thousands of audio files
- Production-ready deployment on Google Cloud Platform
- Docker containerization for reproducible local development

---

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
6. User can immediately start creating

---

### Development Speed

**Timeline:** Complete system delivered in **< 1 month**:
- Week 1: Research, model selection, initial prototype
- Week 2: Batch processing pipeline, optimization
- Week 3: FastAPI service, Docker deployment
- Week 4: Production deployment, integration with Copilot

**Demonstrates:** Ability to rapidly acquire ML/AI domain knowledge and deliver production systems under tight deadlines.

---

## Technologies Used

**ML/AI:**
- PyTorch - Deep learning framework
- Transformers (Hugging Face) - Model loading and inference
- MERT-v1-95M - Audio feature extraction model
- CLaMP3-SAAS - Multimodal audio+text embedding model
- FAISS - Facebook AI Similarity Search for vector indexing
- NumPy - Numerical computing and embedding storage

**Backend:**
- FastAPI - Modern Python web framework
- Pydantic - Data validation
- Uvicorn - ASGI server
- Python 3.8+ - Core language

**Infrastructure:**
- Docker & Docker Compose - Containerization
- Google Cloud Platform - Production deployment
- Google Cloud Run - Serverless API hosting
- GCP VMs - High-performance batch processing
- YAML - Configuration management

**Development:**
- Git - Version control
- pytest - Testing
- Black - Code formatting
- Comprehensive logging for debugging

---

## What Makes This Special

**1. Rapid Execution**
Built complete ML pipeline in < 1 month while maintaining production quality. Shows ability to learn new domains (audio ML, embedding models, vector search) and deliver quickly.

**2. Performance Engineering**
15-30x optimization through understanding bottlenecks and implementing model reuse, batching, and parallel processing. Not just "make it work"—make it fast.

**3. Production-Grade Quality**
Comprehensive error handling, resume-capable checkpointing, Docker deployment, configuration management. Built for real use, not just demos.

**4. Dual Deployment Strategy**
Sequential processing for resource-constrained environments, parallel processing for performance—one codebase, multiple optimization profiles.

**5. Practical ML Application**
Not academic research—this system solves real problems for professional musicians. Semantic search enables workflows impossible with traditional keyword search.

**6. Cross-Modal Understanding**
Leveraging state-of-the-art multimodal models (CLaMP3) to bridge text and audio—enabling natural language queries for audio content.

---

## Career Significance

CLaMP3 Audio Semantic Search demonstrates:

- **ML/AI capability:** Rapid acquisition of new technical domains (embedding models, vector search, multimodal learning)
- **Performance optimization:** 15-30x speedup through systematic profiling and optimization
- **Production engineering:** Docker deployment, configuration management, error handling
- **Fast execution:** Complete pipeline in < 1 month under business pressure
- **Integration thinking:** Designed for easy integration with Copilot LLM workflows

This project bridges classical audio engineering (my academic background) with modern AI/ML (industry evolution), showing ability to stay at cutting edge of music technology.

---

**Related Projects:**
- [Density Copilot](01-Density-Copilot.html) - AI assistant using this semantic search for intelligent palette curation
- [Density DAW](02-Density-DAW.html) - Professional DAW where discovered samples are ultimately used

**Technical Resources:**
- MERT: [Musical Expression Recognition Transfer](https://huggingface.co/m-a-p/MERT-v1-95M)
- CLaMP3: Contrastive Language-Audio Pretraining (multimodal embeddings)
- FAISS: [Facebook AI Similarity Search](https://github.com/facebookresearch/faiss)
