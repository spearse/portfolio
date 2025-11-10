---
layout: default
title: Compose with Sounds v2
permalink: /projects/03-Compose-with-Sounds.html
---

# Compose with Sounds v2
## EU Commission-Funded Educational DAW

**Role:** Sole Developer
**Duration:** 7 years (2013-2020)
**Funding:** EU Commission Grant
**Scale:** European schools deployment, 10 language translations

---

<div class="highlight-box">

### 🎯 Key Achievements

- **Solo development over 7 years** building complete DAW from scratch alongside academic role
- **EU Commission-funded** competitive grant supporting European-wide deployment
- **10 language translations** enabling deployment across multiple European countries
- **Custom audio engine (FSOM)** designed specifically for pedagogical sound object manipulation
- **Cross-platform deployment** (macOS, Windows, Linux) supporting diverse school environments
- **Published research** with ADC 2019 talk and SMC conference paper

</div>

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">7 Years</span>
    <span class="metric-label">Solo<br>Development</span>
  </div>
  <div class="metric">
    <span class="metric-value">10</span>
    <span class="metric-label">Language<br>Translations</span>
  </div>
  <div class="metric">
    <span class="metric-value">3</span>
    <span class="metric-label">Platforms<br>(Mac/Win/Linux)</span>
  </div>
  <div class="metric">
    <span class="metric-value">1,500</span>
    <span class="metric-label">Development<br>Hours</span>
  </div>
</div>

## Overview

Compose with Sounds is a pedagogical digital audio workstation designed specifically for teaching experimental and electroacoustic music composition. Unlike traditional DAWs focused on note-based music, it enables students to work with sound objects as the primary musical unit—embracing musique concrète and acousmatic music principles.

As sole developer over 7 years alongside academic responsibilities as Senior Lecturer, I built this from the ground up: custom C++ audio engine, Qt-based cross-platform GUI, 3D visualizations, and internationalization for European deployment.

---

## The Educational Challenge

<div class="two-col">
  <div class="col-box">
    <h4>🎓 Pedagogical Needs</h4>
    <ul>
      <li>Intuitive sound manipulation without notation literacy</li>
      <li>Visualizations beyond traditional waveforms</li>
      <li>Workflows aligned with curriculum needs</li>
      <li>Balance power with simplicity for learners</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>🌍 Deployment Requirements</h4>
    <ul>
      <li>Accessible across languages and educational systems</li>
      <li>Support for experimental music pedagogy</li>
      <li>Cross-platform (Mac, Windows, Linux)</li>
      <li>Professional DAWs not designed for education</li>
    </ul>
  </div>
</div>

**Gap:** Existing DAWs (Ableton, Logic, Pro Tools) assumed prior knowledge and didn't support object-oriented compositional approaches needed for experimental music pedagogy.

---

## Technical Architecture

### Custom Audio Engine (FSOM)

<div class="highlight-box">

Built **Free Sound Object Mixer (FSOM)** in C++ from scratch:

- **Object-oriented audio processing** - Sounds as discrete manipulable objects
- **Real-time playback and mixing** with low-latency audio I/O
- **Non-destructive editing workflow** preserving original files
- **Multiple format support** - WAV, AIFF, MP3, FLAC
- **Pedagogical design** - Matching educational goals vs. note-based paradigms

</div>

### Cross-Platform Qt Application

**GUI Framework:**
- C++ with Qt 4.x/5.x for native performance
- Custom widgets for sound object visualization
- Drag-and-drop interface for sound manipulation
- 3D animated representations making abstract concepts concrete

### Internationalization at Scale

**10 Languages:** English, French, German, Spanish, Italian, Portuguese, Dutch, Polish, Czech, and others

**Implementation:**
- Qt internationalization framework
- Coordinated with educators across countries for terminology
- Region-specific formatting (dates, numbers)
- Cultural adaptation beyond literal translation

---

## Development Process

<div class="two-col">
  <div class="col-box">
    <h4>📅 Part-Time Development</h4>
    <ul>
      <li>~4 hours per week over 7 years</li>
      <li>~1,500 hours total investment</li>
      <li>Balanced with full-time academic duties</li>
      <li>Careful project management and prioritization</li>
    </ul>
  </div>
  <div class="col-box">
    <h4>👥 User-Centered Design</h4>
    <ul>
      <li>Regular visits to schools across Europe</li>
      <li>Observing students in classroom settings</li>
      <li>Feedback from teachers on effectiveness</li>
      <li>Iterating based on educational outcomes</li>
    </ul>
  </div>
</div>

**Collaborative Development:**
- Worked with music educators to define requirements
- Coordinated with curriculum developers (Leigh Landy, Duncan Chapman, David Holland, Mihai Eniu)
- Ensured software aligned with pedagogical theory and practice

---

## Key Features

<div class="highlight-box">

**Sound Object Manipulation:**
- Import, edit, and arrange sound objects
- Non-destructive processing
- Visual representation of sound materials
- Layering and mixing interface

**Educational Tools:**
- Guided workflows for compositional techniques
- Progressive complexity (beginner → advanced)
- Examples and templates
- Integration with learning materials

**Technical Capabilities:**
- Multi-track mixing and basic effects processing
- Audio analysis and visualization
- Real-time playback with section-based organization
- Project management and export for assessment

</div>

---

## Impact & Deployment

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">Multiple</span>
    <span class="metric-label">European<br>Countries</span>
  </div>
  <div class="metric">
    <span class="metric-value">10</span>
    <span class="metric-label">Language<br>Support</span>
  </div>
  <div class="metric">
    <span class="metric-value">2</span>
    <span class="metric-label">Conference<br>Publications</span>
  </div>
  <div class="metric">
    <span class="metric-value">EU</span>
    <span class="metric-label">Commission<br>Funded</span>
  </div>
</div>

### European Educational Impact

- **Curriculum Integration:** Complete pedagogical materials and teacher training
- **Assessment frameworks** aligned with software capabilities
- **Learning outcomes** validated through classroom use
- **Supported by competitive EU Commission grant**

### Academic Dissemination

**Conference Presentations:**
- **ADC 2019 (Audio Developer Conference, London)** - Talk on architecture and design
  - [Watch on YouTube](https://www.youtube.com/watch?v=kyALim8FSew)
- **SMC 2019 (Sound and Music Computing, Málaga)** - Paper on pedagogical DAW design

---

## Key Challenges Solved

<div class="two-col">
  <div class="col-box">
    <h4>Long-Term Solo Maintenance</h4>
    <p><strong>Problem:</strong> Maintaining complex C++ codebase part-time over 7 years while fulfilling academic duties.</p>
    <p><strong>Solution:</strong> Clean architecture, well-documented code, modular design, careful version control, prioritized stability.</p>
  </div>
  <div class="col-box">
    <h4>Cross-Platform Audio</h4>
    <p><strong>Problem:</strong> Consistent audio behavior across macOS, Windows, Linux with different drivers and APIs.</p>
    <p><strong>Solution:</strong> Platform abstraction layer, Qt's cross-platform capabilities, extensive testing, fallback strategies.</p>
  </div>
  <div class="col-box">
    <h4>Educational vs. Professional Balance</h4>
    <p><strong>Problem:</strong> Software powerful enough for genuine composition but accessible to learners.</p>
    <p><strong>Solution:</strong> Progressive disclosure, carefully designed defaults, guided workflows, visual feedback making processes visible.</p>
  </div>
  <div class="col-box">
    <h4>Internationalization at Scale</h4>
    <p><strong>Problem:</strong> Supporting 10 languages across different educational systems.</p>
    <p><strong>Solution:</strong> Qt i18n framework, collaboration with native speakers, cultural adaptation, testing with local educators.</p>
  </div>
</div>

---

## Technologies Used

**Core:** C++ (Qt framework), Custom audio engine (FSOM), Qt GUI framework, Cross-platform development

**Audio Processing:** Real-time audio I/O, DSP for sound object manipulation, Multi-track mixing

**Deployment:** Application bundling for multiple platforms, Installer creation, Multi-language support

---

## What I Learned

<div class="highlight-box">

**Building for Education is Different:**
- Discoverability over power-user efficiency
- Visual feedback over abstract representations
- Guided learning without constraining creativity
- Stability over cutting-edge features

**Long-Term Solo Projects Require Discipline:**
- Clean, self-documenting code
- Modular architecture
- Ruthless prioritization
- Iterative, user-centered development

**Research and Practice Inform Each Other:**
- Classroom observation informed software design
- Software enabled new pedagogical approaches
- Research into music cognition influenced interface design

</div>

---

## Career Significance

Compose with Sounds represented transition from pure research to research-through-making, demonstrating ability to:

- **Build complete production systems** independently
- **Sustain long-term complex projects** over years
- **Deploy at international scale** across educational systems
- **Bridge research and practice** effectively
- **Work with diverse stakeholders** (educators, students, funders)

This foundation prepared for industry transition, where these skills translated directly to building professional tools for Density (commercial DAWs, AI systems, web platforms).

---

**Related Projects:**
- [Density DAW](02-Density-DAW.html) - Professional C++/JUCE application building on audio expertise
- [Density Copilot](01-Density-Copilot.html) - PyQt5 desktop app leveraging Qt framework experience

**External Links:**
- [ADC 2019 Talk (YouTube)](https://www.youtube.com/watch?v=kyALim8FSew)
- [University of Portsmouth Research Portal](https://researchportal.port.ac.uk/en/publications/composing-with-sounds-designing-an-object-oriented-daw-for-the-te)
