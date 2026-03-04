---
layout: default
title: Density Copilot - AI Voice Assistant for Music Production
permalink: /projects/01-Density-Copilot.html
---

# Density Copilot - AI Voice Assistant for Music Production

Role: Lead Software Engineer (ongoing) • Scope: Voice + LangGraph agent • Users: Pro DJs & producers

## Overview
Built an AI assistant that lets producers speak a brief in plain English and receive professional DJ-ready arrangements. Sole owner of the voice interface; heavy contributor to the LangGraph multi-agent backend.

<div class="highlight-box" markdown="1">
Delivered Electron + React 19 voice UI with ElevenLabs speech-to-speech, Three.js 3D orb visualization, and LangGraph SDK streaming. Designed and built the LangGraph multi-agent pipeline (genre detection, intent routing, palette generation, arrangement via DensityMark DSL, effects) deployed on LangGraph Platform.
</div>

<div class="metrics-box">
  <div class="metric">
    <span class="metric-value">VC</span>
    <span class="metric-label">Demo<br>Differentiator</span>
  </div>
  <div class="metric">
    <span class="metric-value">Zero</span>
    <span class="metric-label">Friction<br>Workflow</span>
  </div>
  <div class="metric">
    <span class="metric-value">Real-time</span>
    <span class="metric-label">Speech-to-Speech<br>Interrupts</span>
  </div>
  <div class="metric">
    <span class="metric-value">Full-Stack</span>
    <span class="metric-label">Voice → Agent<br>→ DAW</span>
  </div>
</div>

## How it works
- Voice: ElevenLabs Conversational AI (speech-to-speech) with custom interrupt protocol for mid-generation updates.
- Frontend: Electron + React 19 + TypeScript; custom hooks (useVoiceAgent, useLangGraph, useTCP) decouple layers.
- Visualization: Three.js 3D orb synced to agent state (idle / listening / processing / speaking).
- Agent: LangGraph multi-agent graph (router → palette → arrange → effects) with streaming state; deployed on LangGraph Platform.
- DAW integration: TCP socket + Python Remote Script to Ableton Live; DensityMark DSL for musically valid arrangements.
- Search: Google Vertex AI Search for semantic sample curation.

## Leadership
Owned voice assistant architecture and implementation; designed LangGraph agent graph structure, subagent state flow, and interrupt system; drove full-stack integration from voice input to DAW automation.
