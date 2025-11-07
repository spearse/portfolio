---
layout: default
title: Compose with Sounds v2
permalink: /projects/03-Compose-with-Sounds.html
---

# Compose with Sounds v2
## EU Commission-Funded Educational DAW

**Role:** Sole Developer
**Duration:** 7 years (2013-2020)
**Organization:** University of Portsmouth
**Funding:** EU Commission Grant
**Scale:** Deployed across European schools, 10 language translations

---

## Overview

Compose with Sounds is a pedagogical digital audio workstation designed specifically for teaching experimental and electroacoustic music composition. Unlike traditional DAWs that focus on note-based music, Compose with Sounds enables students to work with sound objects as the primary musical unit—embracing the principles of musique concrète and acousmatic music.

As sole developer over 7 years (alongside academic responsibilities as Senior Lecturer), I built this from the ground up: custom C++ audio engine, Qt-based cross-platform GUI, 3D visualizations for educational engagement, and internationalization for European deployment.

---

## The Educational Challenge

Traditional music education centers on notation, but experimental music composition works with recorded and synthesized sounds directly. Students needed a tool that:

- **Made sound manipulation intuitive** without requiring notation literacy
- **Visualized sound in engaging ways** beyond traditional waveforms
- **Supported pedagogical workflows** aligned with curriculum needs
- **Was accessible** across different languages and educational systems
- **Balanced power with simplicity** for learners at various levels

Existing DAWs (Ableton, Logic, Pro Tools) were designed for professional production, not education. They assumed prior knowledge and didn't support the object-oriented compositional approach needed for experimental music pedagogy.

---

## Technical Architecture

### Custom Audio Engine (FSOM)

Built **Free Sound Object Mixer (FSOM)** in C++ from scratch:

**Core Features:**
- Object-oriented audio processing (sounds as discrete manipulable objects)
- Real-time playback and mixing
- Non-destructive editing workflow
- Support for multiple audio formats (WAV, AIFF, MP3, FLAC)
- Low-latency audio I/O across platforms

**Why Custom Engine:**
Standard audio libraries assumed note-based or timeline-based paradigms. FSOM was designed specifically for sound object manipulation matching pedagogical goals.

### Cross-Platform Qt Application

**GUI Framework:**
- C++ with Qt 4.x/5.x for native performance
- Cross-platform: macOS, Windows, Linux support
- Custom widgets for sound object visualization
- Drag-and-drop interface for sound manipulation

**Educational Visualizations:**
- 3D animated representations of sound objects
- Visual feedback for audio processing
- Dynamic models showing compositional structure
- Designed to make abstract concepts concrete for students

### Internationalization

**10 Language Support:**
Full translation into multiple European languages to support EU-wide deployment:
- English, French, German, Spanish, Italian, Portuguese, Dutch, Polish, Czech, and others

**Implementation:**
- Qt internationalization framework
- Translatable UI strings throughout
- Region-specific formatting (dates, numbers)
- Coordinated with educators across countries for terminology

---

## Development Process

### Solo Development Alongside Academic Role

**Part-Time Development:**
- ~4 hours per week over 7 years (approximately 1,500 hours total)
- Balanced with full-time academic responsibilities (teaching, research, administration)
- Required careful project management and prioritization

**Iterative Process:**
1. Initial prototype and proof of concept
2. Regular user testing in schools across EU
3. Feedback incorporation from educators and students
4. Incremental feature additions
5. Continuous refinement based on classroom use

### User-Centered Design

**Field Testing:**
- Regular visits to schools across Europe with prototypes
- Observing students using the software in real classroom settings
- Gathering feedback from teachers on pedagogical effectiveness
- Iterating based on actual educational outcomes

**Collaborative Development:**
- Worked with music educators to define requirements
- Coordinated with curriculum developers (Leigh Landy, Duncan Chapman, David Holland, Mihai Eniu)
- Ensured software aligned with pedagogical theory and practice

---

## Key Features

### Sound Object Manipulation
- Import, edit, and arrange sound objects
- Non-destructive processing
- Visual representation of sound materials
- Layering and mixing interface

### Educational Tools
- Guided workflows for compositional techniques
- Examples and templates
- Progressive complexity (beginner → advanced)
- Integration with learning materials

### Compositional Support
- Multiple timeline views
- Section-based organization
- Export for performance and assessment
- Project management for students

### Technical Capabilities
- Multi-track mixing
- Basic effects processing
- Audio analysis and visualization
- Real-time playback

---

## Impact & Deployment

### European Educational Impact

**Deployment Scale:**
- Used in music programs across multiple European countries
- Integrated into curricula for experimental music composition
- Supported by EU Commission funding (competitive grant)

**Curriculum Integration:**
- Complete pedagogical materials developed alongside software
- Teacher training and documentation
- Assessment frameworks aligned with software capabilities
- Learning outcomes validated through classroom use

### Academic Dissemination

**Conference Presentations:**
- **ADC 2019 (Audio Developer Conference, London):** Talk on Compose with Sounds architecture and design
  - [Watch on YouTube](https://www.youtube.com/watch?v=kyALim8FSew)
- **SMC 2019 (Sound and Music Computing Conference, Málaga):** Paper on pedagogical DAW design
  - "Composing with Sounds: Designing an Object-Oriented DAW for the Teaching of Sound-Based Composition"

**Research Contributions:**
- Demonstrated viability of purpose-built educational audio software
- Informed pedagogical approaches to sound-based composition
- Contributed to discourse on music technology in education

---

## Technical Challenges Solved

### Long-Term Solo Maintenance

**Challenge:** Maintaining complex C++ codebase part-time over 7 years while fulfilling academic duties.

**Solution:**
- Clean architecture and well-documented code
- Modular design allowing incremental updates
- Careful version control and testing
- Prioritization of stability over feature bloat

### Cross-Platform Audio

**Challenge:** Consistent audio behavior across macOS, Windows, Linux with different audio drivers and APIs.

**Solution:**
- Platform abstraction layer
- Qt's cross-platform capabilities
- Extensive testing on all target platforms
- Fallback strategies for platform-specific issues

### Educational vs. Professional Balance

**Challenge:** Creating software powerful enough for genuine composition but accessible to learners.

**Solution:**
- Progressive disclosure of complexity
- Carefully designed defaults
- Guided workflows without restricting creativity
- Visual feedback making invisible processes visible

### Internationalization at Scale

**Challenge:** Supporting 10 languages across different educational systems.

**Solution:**
- Qt internationalization framework
- Collaboration with native speakers for translation quality
- Cultural adaptation beyond literal translation
- Testing with educators in each target country

---

## Technologies Used

**Core:**
- C++ (Qt framework)
- Custom audio engine (FSOM)
- Qt GUI framework
- Cross-platform development (Mac, Windows, Linux)

**Audio Processing:**
- Real-time audio I/O
- DSP for sound object manipulation
- Multi-track mixing
- Audio file format support

**Deployment:**
- Application bundling for multiple platforms
- Installer creation
- Update distribution
- Multi-language support

---

## What I Learned

### Building for Education is Different

Educational software requires different priorities than professional tools:
- **Discoverability** over power-user efficiency
- **Visual feedback** over abstract representations
- **Guided learning** without constraining creativity
- **Stability** over cutting-edge features

### Long-Term Solo Projects Require Discipline

Maintaining a project part-time over 7 years taught me:
- Importance of clean, self-documenting code
- Value of modular architecture
- Need for ruthless prioritization
- Power of iterative, user-centered development

### Internationalization is More Than Translation

Supporting 10 languages meant:
- Understanding cultural differences in music education
- Adapting terminology for different educational traditions
- Testing with native speakers and educators
- Building flexibility into UI for varying text lengths

### Research and Practice Inform Each Other

Working simultaneously as academic and developer created valuable feedback loop:
- Classroom observation informed software design
- Software capabilities enabled new pedagogical approaches
- Research into music cognition influenced interface design
- Practical development challenged theoretical assumptions

---

## Career Significance

Compose with Sounds represented my transition from pure research to research-through-making. It demonstrated that I could:

- **Build complete production systems** independently
- **Sustain long-term complex projects** over years
- **Deploy at international scale** across educational systems
- **Bridge research and practice** effectively
- **Work with diverse stakeholders** (educators, students, funders)

This foundation prepared me for industry transition, where these skills translated directly to building professional tools for Density (commercial DAWs, AI systems, web platforms).

---

## Legacy

While I ceased active development in 2020 when transitioning to industry, Compose with Sounds demonstrated viability of purpose-built educational music software and contributed to ongoing discussions about technology in music education.

The experience of building a complete audio application from scratch—audio engine, GUI, internationalization, deployment—became foundation for all subsequent work in professional audio software development.

---

**Related Projects:**
- [Density DAW](02-Density-DAW.html) - Professional C++/JUCE application building on audio development expertise
- [Density Copilot](01-Density-Copilot.html) - PyQt5 desktop app leveraging Qt framework experience

**External Links:**
- [ADC 2019 Talk (YouTube)](https://www.youtube.com/watch?v=kyALim8FSew)
- [University of Portsmouth Research Portal](https://researchportal.port.ac.uk/en/publications/composing-with-sounds-designing-an-object-oriented-daw-for-the-te)
