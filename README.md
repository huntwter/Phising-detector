# Advanced Phishing Detection System (APDS)

## ⚠️ Proprietary & Confidential
**Copyright (c) 2024. All Rights Reserved.**

This repository contains the source code for the high-performance Advanced Phishing Detection System. It is architected using Domain-Driven Design (DDD) principles to support massive scale and security.

## Architectural Overview

The system is designed as a **Modular Monolith** with a strict separation of concerns to facilitate security and code obfuscation.

### High-Level Layers

1.  **Public API Gateway (`src/api`)**:
    *   Built with FastAPI.
    *   Handles Authentication, Rate Limiting, Input Validation, and Request Routing.
    *   Acts as the secure entry point, wrapping the protected core.

2.  **Protected Core Logic (`src/core`)**:
    *   **The "Crown Jewels"**. This package contains the proprietary hybrid analysis engines (Lexical, Network, Visual, ML).
    *   Designed to be compiled/obfuscated (via Cython/Nuitka) into binary extensions.
    *   Follows strict DDD "Package by Component" structure.

3.  **Asynchronous Workers (`src/workers`)**:
    *   Powered by Redis and Celery.
    *   Handles heavy lifting: data ingestion, ML inference, and heavy scanning tasks decoupled from the real-time API.

## Directory Structure

*   `src/`: Application Source Code.
*   `build_tools/`: Scripts for compiling and obfuscating the Core logic.
*   `docs/`: Comprehensive Architecture and API documentation.

## License

See `LICENSE` file. Strictly Proprietary.
