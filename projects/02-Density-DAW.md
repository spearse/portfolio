---
layout: default
title: Density DAW - Professional DJ Software
permalink: /projects/02-Density-DAW.html
---

# Density DAW - Professional DJ Software

Role: Software Engineer → Technical Lead (3 years) • Scale: ~2,500 DAU • Users: Pro DJs (Burning Man, EDC)

## Overview
Joined to evolve a DJ-focused DAW that pairs live performance workflows with pro-grade audio processing. Led the shift to Windows alongside macOS, tightened reliability, and sped up delivery.

<div class="highlight-box" markdown="1">
Built a unified Mac/Windows codebase, reworked threading/interop, and delivered a real-time engine that holds sub-10ms latency under load. Added LUFS metering and pro-grade effects, production observability, and CI/CD with signing/notarization and Windows installers.
</div>

## Impact
Crash rate down 40% (5% → 3%); releases from monthly to ~1.5 weeks; Windows launch achieved platform parity and supported ~2,500 daily DJs.

## How it works
- Real-time: Lock-free audio/UI messaging, preallocated buffers, dedicated thread pools.
- DSP/effects: BS.1770-4 LUFS, Pioneer-style filters, fractional delay, multi-band limiting with artifact-free switching.
- Reliability & rollout: Sentry + structured logging, feature flags, graceful degradation.
- Delivery: GitHub Actions for Mac/Windows, universal binaries, signing/notarization, Windows installer, semantic versioning.

## Leadership
Grew from contributor to lead for the cross-platform port and audio/DSP architecture; set patterns to avoid platform-specific forks; built onboarding/interview loops and mentored the team through the launch.
