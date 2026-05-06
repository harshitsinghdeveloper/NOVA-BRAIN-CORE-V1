# NOVA-BRAIN-CORE-V1

Prototype AGI core architecture focused on modular cognition, persistent state continuity, packet-based sensory routing, and scalable cognitive orchestration.

---

# Overview

NOVA Brain Core V1 is an experimental AGI-oriented software architecture designed around biologically inspired cognitive system organization.

The project focuses on:

- Persistent global state continuity
- Modular cognitive processing
- Packet-based sensory transmission
- Centralized routing systems
- Scalable orchestration between subsystems
- Long-term architectural traceability

This repository represents the foundational prototype phase of the NOVA architecture.

---

# Current Architecture

Current implemented modules:

## Core Runtime Components

- `state_schema.py`
  - Global runtime state container
  - Maintains active cognitive context
  - Enables inter-module communication
  - Supports persistent structured state updates

- `sensory_listener.py`
  - Captures raw environmental input
  - Performs rough validation
  - Generates standardized transmission packets
  - Prepares data for routing into the system

- `modality.py`
  - Helper class for modality-specific processing
  - Supports future expansion for:
    - Speech
    - Sensor systems
    - Vision
    - Additional modalities

- `sensory_test.py`
  - Validation and edge-case testing suite
  - Tests:
    - Empty input
    - Invalid input
    - Boundary conditions
    - Structured input edge cases

---

# Core Design Philosophy

The NOVA architecture is designed around:

## 1. Persistent State Continuity

A unified global state container maintains runtime context across all cognitive layers.

This improves:
- traceability
- debugging
- coherence
- long-term memory organization

---

## 2. Packet-Based Transmission

Raw inputs are transformed into structured transmission packets before entering the routing system.

Benefits:
- modular scalability
- consistent validation
- easier debugging
- system observability

---

## 3. Modular Cognitive Architecture

Each subsystem performs a specialized responsibility while communicating through structured interfaces.

This allows:
- incremental scaling
- safer experimentation
- subsystem isolation
- future hardware integration

---

# Planned Future Modules

Planned architecture expansion includes:

- ThalamusIO
- CortexController
- Working Memory Layer
- Salience and Attention Layer
- Executive Controller Layer
- Planning and Reasoning Layer
- Self Evaluation Layer
- Habit Loop Layer
- Hippocampus Memory Layer
- Bridge Fusion System

---

# Project Status

Current Status:
- Early Prototype Phase (V1)

Current Focus:
- Architecture stabilization
- State continuity
- Packet validation systems
- Runtime traceability
- Module communication standards

---

# Technologies

- Python
- Dataclasses
- Object-Oriented Design
- Modular System Architecture

---

# Research Direction

NOVA Brain Core explores scalable AGI-oriented system design through structured cognitive abstraction, modular orchestration, and persistent contextual reasoning.

The project is experimental and intended for research, architectural exploration, and iterative system development.

---

# Author

Harshit Singh

---

# License

GNU GPL v3
