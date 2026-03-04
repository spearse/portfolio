---
layout: default
title: Density Copilot - AI Voice Assistant for Music Production
permalink: /projects/01-Density-Copilot.html
---

# Density Copilot - AI Voice Assistant for Music Production

Role: Lead Software Engineer (ongoing) • Scope: Voice-driven AI music production; sole owner of voice assistant frontend; heavy contribution to LangGraph multi-agent backend

## Overview
Built the complete voice assistant and contributed heavily to the LangGraph multi-agent backend powering Density Copilot — an AI assistant that lets producers speak a brief in plain English and receive a professional DJ-ready arrangement, complete with palette curation, effects, and intelligent sample search.

<div class=”highlight-box” markdown=”1”>
Sole architect and implementer of the Electron + React 19 + TypeScript voice interface, integrating ElevenLabs Conversational AI for real-time speech-to-speech interaction, a LangGraph SDK streaming connection to the agent backend, and a Three.js 3D orb visualisation. On the backend, contributed significantly to the LangGraph multi-agent pipeline — a graph of specialised subagents that detect genre, route intent, generate and modify sample palettes, arrange tracks with DensityMark, and apply effects — deployed on LangGraph Platform.
</div>

## Impact
Demos cited by VCs as the key differentiator; pro DJs report trusted arrangement quality with zero friction; voice interface lets producers express ideas naturally without touching a keyboard. System now ships with a cloud-deployed LangGraph backend handling full track generation end-to-end.

## How it works
- **Voice layer:** ElevenLabs Conversational AI (speech-to-speech) with a custom interrupt system so the agent can notify users mid-generation without losing context.
- **Frontend:** Electron 28 + React 19 + TypeScript + Vite; custom hooks (useVoiceAgent, useLangGraph, useTCP) decouple voice, agent streaming, and DAW communication.
- **Visualisation:** Three.js + React Three Fiber 3D orb animates in sync with agent state (idle / listening / processing / speaking).
- **Agent backend:** LangGraph multi-agent graph (router → palette → arrange → effects) deployed on LangGraph Platform with staging and production environments; genre detection, intent routing, and graceful mid-flow interrupts.
- **DAW integration:** Length-prefix TCP socket + Python Remote Script connects to Ableton Live; DensityMark DSL with streaming parser/validator keeps arrangements musically valid.
- **Sample search:** Google Discovery Engine (Vertex AI Search) for context-aware semantic sample curation.

## Ownership & Contribution
Complete ownership of the voice assistant (Electron/React/ElevenLabs/LangGraph SDK integration, 3D UI, interrupt system, audio analysis client). Heavy contribution to the LangGraph agent — intent routing graph, subagent state design, palette modification flow, effects pipeline, and interrupt protocol.
