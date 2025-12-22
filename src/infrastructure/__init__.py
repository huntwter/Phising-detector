"""
Shared Infrastructure Layer.

This package provides low-level technical capabilities used by both the API and the Core.
It includes:
- Redis Client wrappers
- Database Session management
- Logging configurations
- External Service Adapters (if generic)

Note: Domain-specific infrastructure (e.g., a specific repository implementation)
should reside in `src/core/<domain>/infrastructure`.
"""
