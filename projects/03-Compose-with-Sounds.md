---
layout: default
title: Compose with Sounds v2
permalink: /projects/03-Compose-with-Sounds.html
---

# Compose with Sounds v2
Role: Sole Developer (2013–2020, ~1,500 hours) • Funding: EU Commission grant • Reach: European schools, 10 languages • Platforms: macOS/Windows/Linux

## Overview
Built a pedagogical DAW for electroacoustic/experimental music where sound objects—not notation—are the primary unit. Shipped cross-platform with a custom C++ audio engine (FSOM) and Qt UI, translated into 10 languages for European deployment.

## What I Built
- FSOM audio engine: real-time sound-object playback/mixing with non-destructive editing.
- Qt app/UI: drag-and-drop sound objects, custom visualizations (3D/animated) to make abstract concepts tangible.
- Internationalization: 10-language support via Qt i18n; coordinated terminology with educators.
- Curriculum alignment: workflows, materials, and teacher training tailored to classroom use.
- Cross-platform delivery: installers for Mac/Win/Linux; stable in varied school environments.

## Impact
- EU Commission–funded; deployed across multiple European countries/schools.
- Enabled learners without notation literacy to compose with sound objects.
- Academic dissemination: ADC 2019 talk; SMC 2019 paper.
- Sustained solo maintenance for 7 years alongside a senior lecturer role.

## Key Technical Highlights
- Platform abstraction for consistent audio behavior across OSs.
- Progressive-disclosure UX for beginners; visual feedback over dense controls.
- Robust i18n with regional formatting and terminology alignment.
- Clean modular C++/Qt architecture to support long-term solo upkeep.

## Challenges & Solutions
- Long-term solo maintenance: disciplined architecture, documentation, and version control.
- Cross-platform audio quirks: abstraction layer + extensive testing/fallbacks.
- Balancing power vs. approachability: guided workflows, sensible defaults, and visual scaffolding.

## Links
- ADC 2019 talk (YouTube): https://www.youtube.com/watch?v=kyALim8FSew
- SMC 2019 paper: https://researchportal.port.ac.uk/en/publications/composing-with-sounds-designing-an-object-oriented-daw-for-the-te
