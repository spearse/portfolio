---
layout: page
title: Density Audio Workstation — DJ-Focused DAW with CDJ Integration
---

# Project: Density Audio Workstation
## Summary
A specialized Digital Audio Workstation designed specifically for DJ workflows, built with the JUCE framework in C++. The application automates the traditionally manual process of preparing DJ sets by intelligently importing recordings from CDJ hardware, automatically extracting beat grids, and generating time-aligned multi-track projects. The system features real-time DSP processing including custom delay effects with crossfade algorithms to eliminate Doppler artifacts, LUFS-based loudness metering for broadcast-quality output, and sophisticated tempo automation. A custom recording manager parses JSON-based event logs from hardware, identifies track boundaries, and converts recordings into editable projects with precisely synchronized beat grids. The application integrates REST APIs for user authentication and analytics, implements auto-updating capabilities, and includes comprehensive crash tracking and logging infrastructure to support production deployment.

## CV Bullets
- Architected and developed a C++-based DJ-focused DAW using JUCE framework, featuring automatic CDJ beat grid extraction, multi-track project management, and real-time audio processing with custom DSP effects
- Implemented intelligent recording management system that parses hardware event streams, automatically detects track boundaries, and converts CDJ recordings into time-aligned multi-track projects with synchronized beat grids
- Designed custom audio processors including fractional delay with crossfade interpolation to eliminate Doppler effects, LUFS loudness metering for broadcast compliance, and wet/dry mix curves for professional audio processing
- Engineered modular architecture using unity build system for optimized compilation, integrating REST APIs for authentication/analytics, crash tracking, and comprehensive logging infrastructure
- Developed sophisticated beat grid analysis algorithms that compute best-fitting uniform grids from CDJ markers, automatically segment tracks with multiple BPMs, and generate editable automation timelines

## Tagline
Specialized DJ DAW with intelligent CDJ integration that automatically transforms hardware recordings into beat-synced, broadcast-ready multi-track projects through advanced DSP and machine learning-driven beat analysis.

## Architecture Overview
The system follows a modular JUCE-based architecture organized as a unity build for optimal compilation performance. It consists of three primary layers: a native C++ audio engine handling real-time DSP processing, a model layer managing project state (projects, tracks, and clips), and a UI layer built on custom graphics components. The recording management subsystem parses JSON event logs from CDJ hardware, identifying track boundaries and timestamps, then coordinates conversion into editable projects. Beat grid data flows from CDJ markers through analysis algorithms into uniform beat sequences that drive tempo automation and clip alignment. Audio processing utilizes a plugin-style architecture with effect controllers and custom processors for delay, filtering, and dynamics. The system integrates external services via REST APIs for authentication, analytics, and cloud logging, with local state persistence using ValueTree serialization and automatic crash reporting for production monitoring.