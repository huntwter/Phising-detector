"""
Protected Core Logic Package.

This package contains the proprietary analysis engines and domain logic.
It is structured using Domain-Driven Design (DDD) principles.

**Structure:**
- `lexical_engine`: Text-based analysis (URL string analysis, NLP).
- `visual_engine`: Computer vision, OCR, screenshot analysis.
- `network_engine`: DNS resolution, IP reputation, SSL/TLS analysis.
- `ml_engine`: Heuristic and model-based scoring aggregation.
- `shared_kernel`: Common value objects, entities, and interfaces shared across domains.

**Security Notice:**
This package is intended to be compiled into binary extensions in production.
Do not expose internal modules directly to the public API without an Application Layer facade.
"""
