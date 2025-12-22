"""
Database Connection.

Manages SQLAlchemy engine and sessions.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# ENGINE = create_engine("postgresql://...")
# SessionLocal = sessionmaker(bind=ENGINE)
