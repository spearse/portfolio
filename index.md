---
layout: home
---

<section class="hero">
  <h1>Music Computing Researcher → Production Systems Engineer</h1>
  <p class="lede">
    PhD + 13 years building tools for music creators — from EU-funded educational software to AI systems driving VC investment.
    I bridge academic research and production engineering across audio, AI/ML, and full-stack development.
  </p>
  <div class="hero-cta">
    <a class="btn" href="{{ site.baseurl }}#projects">View Projects</a>
    <a class="btn ghost" href="{{ site.baseurl }}/about/">About</a>
  </div>
</section>

<section class="about-section">
  <h2>Senior Software Engineer — Music Computing & AI/ML</h2>
  <p>
    I'm Stephen Pearse, a music computing researcher with <strong>PhD + 13 years experience</strong> bridging academia and industry.
    I've led development of production systems used by thousands — from educational DAWs deployed across Europe to AI music assistants generating VC investment interest.
  </p>
  <p>
    After 9 years as <strong>Senior Lecturer</strong> at University of Portsmouth (leading research, directing programs, building EU-funded software),
    I transitioned to industry to create tools for professional artists. At Density, I progressed from engineer to <strong>tech lead</strong> to <strong>AI design lead</strong>,
    building systems used at major festivals worldwide and demonstrating to venture capital firms.
  </p>
  <div class="focus-list">
    <div class="focus-item">
      <h4>Audio & DSP (11+ years)</h4>
      <ul>
        <li>Real-time C++/JUCE engines (<10ms latency)</li>
        <li>Cross-platform desktop apps (Mac/Windows/Linux)</li>
        <li>Professional DSP (LUFS, filters, effects)</li>
        <li>Hardware integration (CDJ, professional audio)</li>
      </ul>
    </div>
    <div class="focus-item">
      <h4>AI/ML Systems (Recent)</h4>
      <ul>
        <li>LLM integration (Gemini, streaming responses)</li>
        <li>Audio embeddings (MERT, Clamp3, FAISS)</li>
        <li>Semantic search at scale (tens of thousands of files)</li>
        <li>Custom DSL design for music representation</li>
      </ul>
    </div>
    <div class="focus-item">
      <h4>Leadership & Product (10+ years)</h4>
      <ul>
        <li>Research group leader (9 years)</li>
        <li>Tech lead / Design lead (industry)</li>
        <li>Full-stack development (React/TypeScript/NestJS)</li>
        <li>CI/CD, testing, production engineering</li>
      </ul>
    </div>
  </div>
</section>

<hr class="rule" />

## Selected Projects {#projects}

<div class="cards">
  <a class="card" href="{{ site.baseurl }}/projects/01-Density-Copilot.html">
    <h3>Density Copilot ⭐ FLAGSHIP</h3>
    <p><strong>Driving VC Investment</strong> — AI music production assistant generating professional arrangements from natural language. Led design of PyQt5 desktop app integrating Google Gemini LLM, custom DSL (DensityMark) with streaming parser, and semantic audio search (MERT/Clamp3/FAISS) processing tens of thousands of samples. Shipped demos to multiple VCs generating significant investment interest. 11 months development, 100+ tests, professional DJ validation.</p>
    <ul class="tags"><li>Python</li><li>PyQt5</li><li>Gemini</li><li>FAISS</li><li>Design Lead</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/02-Density-DAW.html">
    <h3>Density DAW</h3>
    <p><strong>Tech Lead, 3 Years</strong> — Professional C++/JUCE DAW used at major festivals (Burning Man, EDC) with 2,500 daily active users. Led cross-platform transformation (Mac→Windows), built complete CI/CD infrastructure, reduced crashes 40%, accelerated releases 6x. Real-time audio (<10ms), DSP effects, CDJ hardware integration, filter modeling matching Pioneer profiles. Lead technical interviewer, onboarded engineers into audio.</p>
    <ul class="tags"><li>C++</li><li>JUCE</li><li>DSP</li><li>Tech Lead</li><li>CI/CD</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/03-Compose-with-Sounds.html">
    <h3>Compose with Sounds v2</h3>
    <p><strong>Sole Developer, 7 Years</strong> — EU Commission-funded educational DAW for experimental music, deployed across European schools. Built custom C++/Qt audio engine (FSOM) with object-oriented composition, 3D visualizations, and 10 language translations. Developed alongside comprehensive curriculum for sound-based music education. Presented at ADC 2019 and SMC 2019. University of Portsmouth, 2013-2020.</p>
    <ul class="tags"><li>C++</li><li>Qt</li><li>Audio DSP</li><li>Education</li><li>EU-Funded</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/04-CLaMP3-Audio-Semantic-Search.html">
    <h3>CLaMP3 Audio Semantic Search</h3>
    <p><strong>Built in < 1 Month</strong> — Production ML pipeline for semantic audio search using MERT→Clamp3 embeddings. Natural language queries ("punchy techno kick") with sub-second FAISS search. Audio-to-audio, text-to-audio, and hybrid modes. Docker deployment with 15-30x optimization through model reuse batching. Integrated with Copilot for context-aware palette curation, replacing deterministic genre templates with intelligent discovery.</p>
    <ul class="tags"><li>Python</li><li>PyTorch</li><li>FAISS</li><li>Docker</li><li>FastAPI</li></ul>
  </a>

  <a class="card" href="{{ site.baseurl }}/projects/05-Density-Web-Platform.html">
    <h3>Density Web Platform</h3>
    <p><strong>2 Months, Zero Billing Errors</strong> — Full-stack rent-to-own payment system enabling business model transformation. React/NestJS/PostgreSQL with Chargebee integration. Complex 14-month RTO tracking, hardware bundle discount calculations, webhook idempotency, and backward compatibility for existing subscribers. Financial correctness essential—built complete QA environment testing all edge cases before production.</p>
    <ul class="tags"><li>TypeScript</li><li>NestJS</li><li>React</li><li>Chargebee</li><li>PostgreSQL</li></ul>
  </a>
</div>

<section class="strip">
  <div class="cols">
    <div>
      <h4>Experience</h4>
      <ul>
        <li>PhD in Music Computing</li>
        <li>9 years Senior Lecturer (University of Portsmouth)</li>
        <li>4 years industry (Engineer → Tech Lead → Design Lead)</li>
        <li>13+ years total professional experience</li>
      </ul>
    </div>
    <div>
      <h4>Impact</h4>
      <ul>
        <li>AI system driving VC investment (Copilot)</li>
        <li>Tools used at major festivals (Burning Man, EDC)</li>
        <li>Educational software deployed across Europe</li>
        <li>2,500+ daily active users on production systems</li>
      </ul>
    </div>
  </div>
</section>
