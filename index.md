---
layout: home
title: Selected Projects
---

<section class="hero">
  <h1>Engineering for audio, AI, and product.</h1>
  <p class="lede">
    I build refined, dependable tools — from real-time C++/JUCE engines to applied-AI workflows and modern web platforms.
  </p>
  <div class="hero-cta">
    <a class="btn" href="{{ site.baseurl }}#projects">View Projects</a>
    <a class="btn ghost" href="{{ site.baseurl }}/about/">About</a>
  </div>
</section>

<section class="about-section">
  <h2>Senior Software Engineer</h2>
  <p>
    I'm Stephen Pearse, focused on <strong>audio technology</strong>, <strong>applied AI</strong>, and <strong>full-stack product development</strong>.
    I build dependable tools that make creative work faster — from real-time C++/JUCE engines and semantic audio search to modern web platforms.
  </p>
  <div class="focus-list">
    <div class="focus-item">
      <h4>Audio Development</h4>
      <ul>
        <li>C++/JUCE engines & DSP frameworks</li>
        <li>Cross-platform desktop apps</li>
        <li>Real-time audio processing</li>
      </ul>
    </div>
    <div class="focus-item">
      <h4>Applied AI</h4>
      <ul>
        <li>Semantic retrieval & embeddings</li>
        <li>Natural language control systems</li>
        <li>Audio ML model integration</li>
      </ul>
    </div>
    <div class="focus-item">
      <h4>Product Engineering</h4>
      <ul>
        <li>React/TypeScript & Node/NestJS</li>
        <li>Licensing & billing systems</li>
        <li>CI/CD & cloud infrastructure</li>
      </ul>
    </div>
  </div>
</section>

<hr class="rule" />

## Selected Projects {#projects}

<div class="cards">
  <a class="card" href="{{ site.baseurl }}/projects/01-Ableton-Copilot.html">
    <h3>Ableton Copilot</h3>
    <p>AI-powered music production platform integrating Google Gemini with Ableton Live. Features intelligent MIDI composition based on musical context, semantic audio search using natural language, and automated arrangement workflows. Built with Python remote scripts, PyQt5 desktop interface, and Vertex AI backend processing.</p>
    <ul class="tags"><li>Python</li><li>Gemini 2.0</li><li>Vertex AI</li><li>PyQt5</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/02-CLaMP3-Audio-Semantic-Search.html">
    <h3>CLaMP3 Audio Semantic Search</h3>
    <p>Production-ready semantic audio search engine using CLaMP3 multimodal embeddings and MERT features. Enables natural language queries like "warm atmospheric pad" with sub-second latency via FAISS indexing. Supports audio-to-audio, text-to-audio, and hybrid search modes with scalable GCP batch processing achieving 15-30x performance gains.</p>
    <ul class="tags"><li>FastAPI</li><li>FAISS</li><li>CLaMP3</li><li>MERT</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/03-Density-DAW.html">
    <h3>Density DAW</h3>
    <p>Specialized C++/JUCE Digital Audio Workstation for DJ workflows. Automatically imports CDJ recordings, extracts beat grids, and generates time-aligned multi-track projects. Features custom DSP effects including fractional delay with crossfade interpolation, LUFS loudness metering, and intelligent tempo automation from hardware event streams.</p>
    <ul class="tags"><li>C++</li><li>JUCE</li><li>DSP</li><li>Real-time Audio</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/04-Density-Pro---Full-Stack.html">
    <h3>Density Pro — Full Stack</h3>
    <p>Comprehensive subscription management platform with innovative Rent-to-Own payment system. Users acquire lifetime licenses through 14 monthly installments with immediate feature access. Built with React, NestJS, and PostgreSQL, integrating Chargebee for automated billing orchestration, webhook processing, and real-time payment progress tracking.</p>
    <ul class="tags"><li>React</li><li>NestJS</li><li>Chargebee</li><li>PostgreSQL</li></ul>
  </a>
</div>

<section class="strip">
  <div class="cols">
    <div>
      <h4>Focus</h4>
      <ul>
        <li>C++/JUCE engines & desktop tools</li>
        <li>Semantic audio search & embeddings</li>
        <li>Full-stack web, billing, analytics</li>
      </ul>
    </div>
    <div>
      <h4>Highlights</h4>
      <ul>
        <li>Real-time effects framework at Density One</li>
        <li>LUFS analysis pipeline & design system</li>
        <li>Teaching C++ audio software development</li>
      </ul>
    </div>
  </div>
</section>
