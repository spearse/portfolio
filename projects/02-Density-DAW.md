---
layout: default
title: Density DAW
permalink: /projects/02-Density-DAW.html
---

# Density DAW - Professional DJ Software

Role: Software Engineer → Technical Lead (3 years) • Scale: ~2,500 DAU • Users: Pro DJs (Burning Man, EDC)

## Overview
Joined the team to evolve a DJ-focused DAW that pairs live performance workflows with pro-grade audio processing. Led the shift to Windows alongside macOS, tightened reliability, and sped up delivery for a fast-moving DJ market.

## What Changed
- Cross-platform port: Reworked threading/interop to bring the macOS codebase to Windows while keeping one code line.
- Real-time engine: Lock-free audio/UI messaging and preallocated buffers to keep sub-10ms latency under load.
- DSP/effects: LUFS metering (BS.1770-4), Pioneer-style filter modeling, fractional delay and multi-band limiting with artifact-free switching.
- Reliability & rollout: Sentry + structured logging, feature-flagged releases, graceful degradation patterns.
- CI/CD: GitHub Actions pipelines for Mac/Windows, signing/notarization, universal binaries, Windows installer, semantic versioning.

## Impact
- Crash rate down 40% (5% → 3%) after observability + rollout controls.
- Release cadence improved from monthly to ~1.5 weeks.
- Windows launch expanded addressable market and achieved platform parity.
- Supported ~2,500 daily active DJs in production environments.

## Technical Highlights
- Lock-free queues and dedicated thread pools for real-time audio paths.
- zplane SDK integration for beat detection/time-stretch; custom LUFS/true-peak analysis.
- ConfigCat feature flags enabling staged rollouts and A/B tests.
- Automated signing/notarization (macOS) and code-signed Windows installers in CI.

## Leadership
- Grew from contributor to lead for the cross-platform port and audio/DSP architecture; set patterns to avoid platform-specific forks.
- Built onboarding/interview loops for audio engineers and mentored the team through the cross-platform launch.
