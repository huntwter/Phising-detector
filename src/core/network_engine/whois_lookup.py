"""
WHOIS Lookup Service.

Retrieves domain registration details and creation dates.
"""

def lookup_domain(domain: str) -> dict:
    return {"registrar": "GoDaddy", "days_active": 5}
