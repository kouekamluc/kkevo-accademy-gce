import pytest
from django.core.cache import cache


@pytest.fixture(autouse=True)
def _clear_cache():
    """Rate-limit counters live in the cache; start every test clean."""
    cache.clear()
    yield
    cache.clear()
