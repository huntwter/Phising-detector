"""
Unit tests for Lexical Engine.
"""

from src.core.lexical_engine.analyzer import analyze_url

def test_analyze_url():
    result = analyze_url("http://google.com")
    assert "score" in result
