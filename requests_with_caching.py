
"""Simple requests-with-caching shim that reads from a local JSON file.

This implementation mimics the minimal interface the course assignment expects:
- requests_with_caching.get(url, params=dict) -> object with .json()
- requests_with_caching.clear_cache() -> removes in-memory cache
- requests_with_caching.perm_cache() -> dict of cached keys

The real course cache keys are the URL + the sorted params. This shim builds the same key format
so students can drop in a larger `permanent_cache.json` downloaded from the course.
"""
import json
from pathlib import Path
from typing import Any

CACHE_PATH = Path(__file__).parent / "permanent_cache.json"

class ResponseLike:
    def __init__(self, data: Any):
        self._data = data
    def json(self):
        return self._data


class RequestCache:
    def __init__(self):
        self._cache = {}
        self._load()

    def _load(self):
        if CACHE_PATH.exists():
            with open(CACHE_PATH, "r", encoding="utf-8") as f:
                try:
                    self._cache = json.load(f)
                except Exception:
                    self._cache = {}
        else:
            self._cache = {}

    def perm_cache(self):
        return self._cache

    def clear_cache(self):
        self._cache = {}

    def _make_key(self, url: str, params: dict) -> str:
        # Use a stable ordering for params so keys match the course's cache format
        if params:
            items = "&".join(f"{k}={params[k]}" for k in sorted(params))
            return f"{url}?{items}"
        return url

    def get(self, url: str, params: dict = None):
        key = self._make_key(url, params or {})
        if key in self._cache:
            # simulate the "found in permanent_cache" behavior
            return ResponseLike(self._cache[key])
        else:
            raise RuntimeError(f"Cache miss for key: {key}. Please add the appropriate response to permanent_cache.json")

# module-level instance
_inst = RequestCache()

def get(url: str, params: dict = None):
    return _inst.get(url, params)

def clear_cache():
    _inst.clear_cache()

def perm_cache():
    return _inst.perm_cache()
