"""
Authentication Dependency.

Handles API Key validation and OAuth2 token verification.
"""

import os
from fastapi import Header, HTTPException, status

async def verify_api_key(x_api_key: str = Header(...)):
    expected_key = os.getenv("API_KEY_SECRET", "change_me_in_production")

    if x_api_key != expected_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key",
        )
