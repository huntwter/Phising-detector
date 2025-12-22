from celery import Celery
# from src.infrastructure.config import redis_settings

celery_app = Celery(
    "apds_workers",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/1",
    include=["src.workers.tasks.scanning", "src.workers.tasks.ingestion"]
)

celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)
