# System Architecture

The Advanced Phishing Detection System (APDS) is designed as a **Modular Monolith** with a strict separation between the Public API Gateway and the Protected Core Logic.

## Diagram
[Public API (FastAPI)] -> [Service Layer] -> [Protected Core (Compiled/Obfuscated)]
                                      |
                                      v
                                [Async Workers (Celery)]

## Components

### 1. API Gateway (`src/api`)
- Handles authentication, rate limiting, and request validation.
- Delegates business logic to the Core or Workers.

### 2. Core Logic (`src/core`)
- **Lexical Engine**: NLP and heuristic analysis of URLs.
- **Visual Engine**: Computer vision for logo detection and OCR.
- **Network Engine**: Infrastructure analysis (DNS, SSL).
- **ML Engine**: Ensemble models for final scoring.

### 3. Workers (`src/workers`)
- Asynchronous processing for deep scans and reporting.
