---
layout: none
title: Selected Projects
---

<style>
/* --- Color system --- */
:root {
  --bg: #fafafa;
  --text: #222;
  --muted: #666;
  --card: #ffffff;
  --link: #0a7bd6;
  --shadow: 0 2px 10px rgba(0,0,0,0.08);
  --shadow-hover: 0 4px 16px rgba(0,0,0,0.12);
  --border: rgba(0,0,0,0.06);
}

@media (prefers-color-scheme: dark) {
  :root {
    --bg: #0e0f12;
    --text: #e7e7ea;
    --muted: #a2a2ad;
    --card: #15171c;
    --link: #6bb6ff;
    --shadow: 0 1px 0 rgba(255,255,255,0.06);
    --shadow-hover: 0 2px 0 rgba(255,255,255,0.08);
    --border: rgba(255,255,255,0.08);
  }
}

html, body {
  background: var(--bg);
  color: var(--text);
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

body { font-family: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; }

a { color: var(--link); text-decoration: none; }
a:hover { text-decoration: underline; }

header {
  text-align: center;
  padding: 3rem 1rem 2rem;
}
header h1 {
  font-size: 2.5rem;
  margin: 0 0 .3rem 0;
}
header p {
  font-size: 1rem;
  color: var(--muted);
  margin: 0;
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
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 14px;
  padding: 1.5rem;
  box-shadow: var(--shadow);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color .2s ease;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}
.card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow-hover);
  border-color: var(--link);
}
.card h2 {
  font-size: 1.2rem;
  margin: 0 0 .5rem 0;
}
.card p {
  font-size: .95rem;
  line-height: 1.45;
  color: var(--text);
  opacity: .92;
  margin: 0 0 1rem 0;
}
.card a {
  font-weight: 600;
}

footer {
  text-align: center;
  padding: 2rem 1rem 3rem;
  color: var(--muted);
  font-size: .95rem;
  border-top: 1px solid var(--border);
  margin-top: 1rem;
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
    <a href="{{ site.baseurl }}/projects/01-Ableton-Copilot.md">Read&nbsp;more&nbsp;→</a>
  </div>

  <div class="card">
    <h2>CLaMP3 Audio Semantic Search</h2>
    <p>Semantic audio retrieval engine using multimodal embeddings and FAISS indexing to search sound libraries via natural language or hybrid similarity queries.</p>
    <a href="{{ site.baseurl }}/projects/02-CLaMP3-Audio-Semantic-Search.md">Read&nbsp;more&nbsp;→</a>
  </div>

  <div class="card">
    <h2>Density Audio Workstation</h2>
    <p>DJ-focused DAW built in C++/JUCE featuring automatic CDJ beat-grid extraction, advanced DSP effects, and intelligent track segmentation with tempo automation.</p>
    <a href="{{ site.baseurl }}/projects/03-Density-DAW.md">Read&nbsp;more&nbsp;→</a>
  </div>

  <div class="card">
    <h2>Density Pro — Full Stack</h2>
    <p>React + NestJS platform implementing a Rent-to-Own licensing system with real-time payment tracking, webhook orchestration, and seamless ownership conversion.</p>
    <a href="{{ site.baseurl }}/projects/04-Density-Pro-Full-Stack.md">Read&nbsp;more&nbsp;→</a>
  </div>
</div>

<footer>
  © {{ "now" | date: "%Y" }} Stephen Pearse — <a href="mailto:pearse.audio@gmail.com">pearse.audio@gmail.com</a>
</footer>
