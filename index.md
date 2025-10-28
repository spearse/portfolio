---
layout: none
title: Selected Projects
---

<style>
body {
  font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  background: #fafafa;
  color: #222;
  margin: 0;
  padding: 0;
}
header {
  text-align: center;
  padding: 3rem 1rem 2rem;
}
header h1 {
  font-size: 2.5rem;
  margin-bottom: 0.3rem;
}
header p {
  font-size: 1rem;
  color: #666;
  margin-top: 0;
}
.container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 1.5rem;
  padding: 2rem;
  max-width: 1100px;
  margin: auto;
}
.card {
  background: white;
  border-radius: 14px;
  padding: 1.5rem;
  box-shadow: 0 2px 10px rgba(0,0,0,0.08);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0,0,0,0.12);
}
.card h2 {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}
.card p {
  font-size: 0.95rem;
  line-height: 1.4;
  color: #444;
  margin-bottom: 1rem;
}
.card a {
  color: #007acc;
  font-weight: 600;
  text-decoration: none;
}
footer {
  text-align: center;
  padding: 2rem;
  color: #888;
  font-size: 0.9rem;
}
</style>

<header>
  <h1>Stephen Pearse</h1>
  <p>Audio • AI • Engineering</p>
</header>

<div class="container">
  <div class="card">
    <h2>Ableton Copilot</h2>
    <p>AI-powered composition and automation system linking Ableton Live with Google Gemini for generative MIDI, semantic audio search, and intelligent arrangement workflows.</p>
    <a href="projects/01-Ableton-Copilot.md">Read&nbsp;more&nbsp;→</a>
  </div>

  <div class="card">
    <h2>CLaMP3 Audio Semantic Search</h2>
    <p>Semantic audio retrieval engine using multimodal embeddings and FAISS indexing to search sound libraries via natural-language or hybrid similarity queries.</p>
    <a href="projects/02-CLaMP3-Audio-Semantic-Search.md">Read&nbsp;more&nbsp;→</a>
  </div>

  <div class="card">
    <h2>Density Audio Workstation</h2>
    <p>DJ-focused DAW built in C++/JUCE featuring automatic CDJ beat-grid extraction, advanced DSP effects, and intelligent track segmentation with tempo automation.</p>
    <a href="projects/03-Density-DAW.md">Read&nbsp;more&nbsp;→</a>
  </div>

  <div class="card">
    <h2>Density Pro — Full Stack</h2>
    <p>React + NestJS platform implementing a Rent-to-Own licensing system with real-time payment tracking, webhook orchestration, and seamless ownership conversion.</p>
    <a href="projects/04-Density-Pro-Full-Stack.md">Read&nbsp;more&nbsp;→</a>
  </div>
</div>

<footer>
  © {{ "now" | date: "%Y" }} Stephen Pearse — <a href="mailto:pearse.audio@gmail.com">pearse.audio@gmail.com</a>
</footer>
