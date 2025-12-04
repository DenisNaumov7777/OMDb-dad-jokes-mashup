import unittest
import json
import os
from haha_me import create_mix, load_cache, save_cache, cached_get

class TestOfflineLab(unittest.TestCase):

    def setUp(self):
        
        cache = {
            "http://www.omdbapi.com/|{\"t\": \"Test Film\"}": {
                "Title": "Test Film",
                "Year": "2000",
                "Plot": "A test plot."
            }
        }
        save_cache(cache)

    def test_cached_get_returns_from_cache(self):
        url = "http://www.omdbapi.com/"
        params = {"t": "Test Film"}

        result = cached_get(url, params)

        self.assertEqual(result["Title"], "Test Film")

    def test_create_mix_structure(self):
        result = create_mix("Test Film")

        self.assertIn("movie", result)
        self.assertIn("year", result)
        self.assertIn("plot", result)
        self.assertIn("joke", result)

    def test_joke_is_string(self):
        result = create_mix("Test Film")
        self.assertIsInstance(result["joke"], str)

if __name__ == "__main__":
    unittest.main()
