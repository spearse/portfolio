---
layout: default
title: About — Stephen Pearse
permalink: /about/
---

# About Me

I'm **Stephen Pearse**, a music computing researcher and production systems engineer with **PhD + 13 years professional experience** bridging academic research and industry. I build tools for music creators—from EU-funded educational software deployed across Europe to AI systems driving venture capital investment.

My career arc spans **9 years in academia** (Senior Lecturer, research group leader, program director) and **4 years in industry** (engineer → tech lead → AI design lead), giving me a unique perspective combining deep domain expertise with production engineering.

---

## Career Journey

### Academic Foundation (2011-2020)

After completing my **PhD in music computing** focused on agentic tools for experimental music composition, I spent 9 years as **Senior Lecturer at the University of Portsmouth**, where I:

- **Led the music computing research group**
- **Directed the MSc Music & Sound Technology program**
- **Secured EU Commission funding** for educational technology
- **Built Compose with Sounds v2** as sole developer over 7 years

**Compose with Sounds** was a pedagogical digital audio workstation enabling students to compose with sound objects rather than traditional notation. Built in C++ with Qt framework, it featured:
- Custom audio engine (Free Sound Object Mixer)
- 3D visualizations for educational engagement
- 10 language translations for European deployment
- Cross-platform support (Mac, Windows, Linux)

The project was deployed across European schools with comprehensive curriculum materials. I presented the work at **Audio Developer Conference 2019** ([watch on YouTube](https://www.youtube.com/watch?v=kyALim8FSew)) and Sound and Music Computing Conference 2019.

This phase established my deep understanding of music production workflows, audio technology, and the challenges of building tools for creative users.

---

### Industry Transition (2020-2021)

After 9 years building educational tools, I wanted to create systems for professional artists. I joined **Density** as a software engineer working on their professional DJ/DAW application.

**Key learnings during transition:**
- Production engineering vs. academic prototypes (reliability, scale, user support)
- Commercial software development (CI/CD, monitoring, crash tracking)
- Team collaboration and fast iteration cycles
- Business context (revenue, users, market fit, product roadmap)

---

### Technical Leadership (2021-2023)

I was **promoted to Tech Lead** after 1.5 years based on technical contributions and cross-platform expertise.

**Major achievements:**
- **Cross-platform transformation**: Led Mac-only → Windows+Mac migration
- **CI/CD infrastructure**: Built complete deployment pipeline from scratch (GitHub Actions, code signing, automated releases)
- **Reliability improvements**: Reduced crash rate from 5% to 3% (40% improvement) via Sentry integration
- **Release velocity**: Accelerated releases from monthly to every 1.5 weeks (6x faster)
- **Real-time audio**: Implemented <10ms latency processing with lock-free queues
- **Professional DSP**: ITU-R BS.1770-4 LUFS metering, filter modeling, effects processing
- **Hardware integration**: CDJ equipment recording via custom Java/C++ interop
- **Hiring & onboarding**: Lead technical interviewer, developed onboarding program for audio engineers

**Scale:** Supporting **2,500 daily active users**, with the software used at major festivals including **Burning Man** and **EDC Las Vegas**.

This phase demonstrated my ability to lead technical teams, make architectural decisions, and scale production systems while maintaining quality.

---

### AI/ML Systems (2023-Present)

As Density invested in LLM-powered music production tools, I pivoted to lead **Copilot**, an AI music production assistant generating professional arrangements from natural language.

**Design leadership role:**
- **Architected complete system**: PyQt5 desktop app integrating Google Gemini LLM
- **Designed custom DSL (DensityMark)**: Bridging LLMs and musical structure with streaming parser
- **Built semantic audio search** in under 1 month: MERT→Clamp3 embeddings, FAISS vector search, processing tens of thousands of samples
- **Multi-DAW integration**: Socket-based IPC with Ableton Live, extensible to Density DAW
- **Coordinated cross-functional teams**: Backend engineers, ML engineers, product team
- **100+ comprehensive tests**: Unit, integration, and regression coverage

**Business impact:**
- **Shipped to multiple VCs**: Demos driving "heavy investment" interest
- **Professional DJ validation**: Real-world testing in production workflows
- **VC investment driver**: Cited as key differentiator for fundraising

This phase shows my ability to rapidly acquire new technical domains (AI/ML) while applying existing expertise (music computing, desktop development, production engineering).

---

## Technical Expertise

### Audio & DSP (11+ years)
- **C++17 with JUCE**: Professional-grade real-time audio engines
- **Real-time constraints**: <10ms latency, lock-free communication, pre-allocated memory
- **DSP algorithms**: LUFS/EBU R128, filters, effects, fractional delay, SIMD optimization
- **Cross-platform**: Mac (Intel + Apple Silicon Universal Binaries), Windows, Linux
- **Hardware integration**: CDJ equipment, professional audio interfaces, MIDI controllers
- **Custom audio engines**: Built from scratch for specific workflows (FSOM, Density processing)

### AI/ML Systems (Recent)
- **LLM integration**: Google Vertex AI (Gemini), streaming responses, prompt engineering
- **Audio embeddings**: MERT (audio features), Clamp3 (multimodal audio+text)
- **Semantic search**: FAISS vector indexes, sub-second search across tens of thousands of files
- **Custom DSL design**: DensityMark language for musical arrangement representation
- **ML infrastructure**: PyTorch, Transformers, Docker deployment, CPU optimization

### Full-Stack Development
- **Desktop applications**: PyQt5, Qt Framework, multi-threaded architectures
- **Backend**: NestJS, TypeScript, RESTful APIs, webhook processing
- **Frontend**: React, Material-UI, Redux, responsive design
- **Databases**: PostgreSQL with TypeORM, complex state machines
- **Payment systems**: Chargebee integration, rent-to-own logic, discount calculation

### Production Engineering
- **CI/CD**: GitHub Actions, automated builds, code signing, notarization
- **Monitoring**: Sentry crash tracking, structured logging, performance profiling
- **Feature management**: ConfigCat feature flags, A/B testing, gradual rollouts
- **Deployment**: Google Cloud Run, Docker, Kubernetes, cross-platform installers

### Leadership & Communication
- **Technical leadership**: 11+ years (9 academic + 2.5 industry)
- **Research group leader**: Led music computing research for 9 years
- **Program direction**: Directed MSc Music & Sound Technology program
- **Hiring & mentorship**: Lead technical interviewer, onboarding program development
- **Cross-functional collaboration**: Product, hardware, ML, backend teams
- **Public speaking**: Conference presentations (ADC 2019, SMC 2019)

---

## What Makes My Profile Unique

**Domain Expertise Applied:** 13+ years of music computing knowledge directly informing system design. Not just an engineer building audio tools—I understand the creative workflows deeply from research and professional use.

**Rare Skill Combination:** Audio DSP + AI/ML + Production Engineering + Music Domain. Very few engineers have this complete combination.

**Academic Research Background:** PhD and 9 years research experience bring deep technical thinking, novel problem-solving approaches, and ability to navigate cutting-edge domains.

**Proven Business Impact:** Built systems driving VC investment (Copilot), used at major festivals worldwide (DAW), deployed across Europe (educational software). Not just technical achievements—real business and user impact.

**Full Lifecycle Experience:** From research prototypes to production systems supporting thousands of users. Experience with every phase: ideation, architecture, implementation, deployment, monitoring, iteration.

**Fast Execution:** Semantic search infrastructure built in <1 month, RTO payment system delivered in 2 months—all while maintaining quality and comprehensive testing.

---

## Current Focus

I'm interested in opportunities that leverage my unique combination of music computing domain expertise and production engineering skills:

- **Audio AI/ML systems** (Spotify, Google Research, Meta Reality Labs)
- **Professional audio tools** (Native Instruments, Ableton, iZotope)
- **Research labs** combining music and technology (academic or industry)
- **Senior/Staff engineer roles** where domain expertise adds value

**Preferred locations:** UK-based, EU remote, or US remote opportunities considered for exceptional fit.

---

## Contact & Links

**LinkedIn:** [linkedin.com/in/stephen-pearse-1870b050](https://www.linkedin.com/in/stephen-pearse-1870b050/)
**GitHub:** [github.com/spearse](https://github.com/spearse)
**ResearchGate:** [researchgate.net/profile/Stephen-Pearse](https://www.researchgate.net/profile/Stephen-Pearse)
**ADC 2019 Talk:** [youtube.com/watch?v=kyALim8FSew](https://www.youtube.com/watch?v=kyALim8FSew)

Feel free to reach out if you'd like to discuss music technology, AI systems for creative applications, or potential collaborations.

---

## Recent Projects

For detailed technical write-ups of my work, see:

- [Density Copilot](projects/01-Density-Copilot.html) - AI music production assistant driving VC investment
- [Density DAW](projects/02-Density-DAW.html) - Professional DJ software (tech lead, 3 years)
- [Compose with Sounds](projects/03-Compose-with-Sounds.html) - EU-funded educational DAW (sole developer, 7 years)
- [CLaMP3 Audio Semantic Search](projects/04-CLaMP3-Audio-Semantic-Search.html) - ML pipeline built in <1 month
- [Density Web Platform](projects/05-Density-Web-Platform.html) - Full-stack RTO payment system

Each project demonstrates different aspects of my technical range while maintaining consistent focus on building tools for music creators.
