# Setup Guide

## Prerequisites
- Python 3.10+
- Redis
- PostgreSQL

## Installation
1. Clone repository.
2. `pip install -r requirements.txt`
3. `cp .env.example .env`

## Running
- **API**: `uvicorn src.api.main:app --reload`
- **Workers**: `celery -A src.workers.celery_app worker --loglevel=info`

## Build/Obfuscation
- Run `python build_tools/compile_core.py` to compile the core logic.
