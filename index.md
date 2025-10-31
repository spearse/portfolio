---
layout: home
title: Stephen Pearse — Portfolio
---

<section class="hero">
  <h1>Stephen Pearse</h1>
  <p class="subtitle">
    Senior Software Engineer specialising in audio technology, applied AI, and full-stack product development.
  </p>
  <p>
    I design and build creative tools that bridge engineering and music — from real-time audio engines and AI-assisted
    workflows to large-scale web platforms. Previously at <strong>Density One</strong>, where I led the real-time effects
    framework, LUFS analysis engine, and design system implementation.
  </p>
  <div class="hero-cta">
    <a class="btn" href="#projects">View Projects</a>
    <a class="btn btn-ghost" href="/about">About</a>
  </div>
</section>

## Featured Projects {#projects}

<div class="cards">

  <a class="card" href="projects/01-Ableton-Copilot.md">
    <h3>Ableton Copilot</h3>
    <p>AI-assisted music creation for Ableton Live — natural language control, semantic audio search, and generative workflows.</p>
    <ul class="tags"><li>Python</li><li>Ableton Live</li><li>Vertex AI</li></ul>
  </a>

  <a class="card" href="projects/02-CLaMP3-Audio-Semantic-Search.md">
    <h3>CLaMP3 Audio Semantic Search</h3>
    <p>Cross-modal embedding model for fast, meaningful sound retrieval. Powered by CLaMP3, MERT, and FAISS.</p>
    <ul class="tags"><li>FastAPI</li><li>FAISS</li><li>Audio AI</li></ul>
  </a>

  <a class="card" href="projects/03-Density-DAW.md">
    <h3>Density DAW</h3>
    <p>DJ-focused desktop workstation built in C++/JUCE — record, edit, and re-engineer live performances.</p>
    <ul class="tags"><li>C++</li><li>JUCE</li><li>Audio Engine</li></ul>
  </a>

  <a class="card" href="projects/04-Density-Pro-Full-Stack.md">
    <h3>Density Pro — Full Stack</h3>
    <p>Subscription and licensing platform with React, NestJS, and Chargebee integration for real-time product tracking.</p>
    <ul class="tags"><li>React</li><li>NestJS</li><li>Chargebee</li></ul>
  </a>

</div>

<section class="pitch">
  <h2>Expertise</h2>
  <ul>
    <li><strong>Audio Development:</strong> C++/JUCE engines, DSP frameworks, cross-platform desktop tools.</li>
    <li><strong>Applied AI:</strong> semantic audio search, embedding models, generative control interfaces.</li>
    <li><strong>Full-Stack Engineering:</strong> web architectures, licensing systems, analytics, and CI/CD pipelines.</li>
  </ul>
</section>

<style>
  :root { --fg:#0b1020; --muted:#5b647a; --bg:#f7f8fb; --card:#ffffff; --accent:#3b82f6; }
  .hero { padding: 2.8rem 0 1.6rem; max-width: 800px; }
  .hero h1 { margin: 0; font-size: 2.6rem; font-weight: 700; }
  .hero .subtitle { font-size: 1.25rem; color: var(--accent); margin: 0.3rem 0 1rem; font-weight: 500; }
  .hero p { color: var(--muted); line-height: 1.6; }
  .hero-cta { margin-top: 1.4rem; display:flex; gap:.8rem; }
  .btn { display:inline-block; padding:.7rem 1rem; border-radius:.75rem; background:var(--accent); color:#fff; text-decoration:none; font-weight:600; }
  .btn-ghost { background:transparent; color:var(--accent); border:1px solid var(--accent); }
  .cards {
    margin: 2rem 0 3rem;
    display:grid; grid-template-columns: repeat(auto-fit, minmax(270px,1fr)); gap: 1.1rem;
  }
  .card {
    display:block; background:var(--card); border:1px solid #e6e8f0; border-radius:1rem; padding:1.2rem;
    text-decoration:none; color:var(--fg); transition: transform .15s ease, box-shadow .15s ease, border-color .15s ease;
  }
  .card:hover { transform: translateY(-3px); box-shadow: 0 8px 24px rgba(16,24,40,.06); border-color:#d9dce6; }
  .card h3 { margin:.2rem 0 .4rem; }
  .card p { color:var(--muted); margin:0 0 .8rem; }
  .tags { display:flex; gap:.4rem; flex-wrap:wrap; list-style:none; padding:0; margin:0; }
  .tags li { font-size:.8rem; padding:.25rem .5rem; background:#eef2ff; border-radius:.6rem; }
  .pitch { background:var(--bg); border:1px solid #e6e8f0; border-radius:1rem; padding:1.2rem; max-width:800px; }
</style>
