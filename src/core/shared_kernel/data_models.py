"""
Data Models.

Common Pydantic models and Value Objects used across engines.
"""

from pydantic import BaseModel

class ScanResult(BaseModel):
    url: str
    score: float
    verdict: str
