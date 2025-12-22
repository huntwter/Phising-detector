"""
Deep Scan Tasks.

Celery tasks for long-running deep analysis (Visual + ML).
"""

from src.workers.celery_app import celery_app

@celery_app.task
def run_deep_scan(url: str):
    pass
