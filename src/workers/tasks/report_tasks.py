"""
Reporting Tasks.

Generates PDF/JSON reports and emails them to users.
"""

from src.workers.celery_app import celery_app

@celery_app.task
def generate_report(scan_id: str):
    pass
