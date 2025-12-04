import json
import os
import random

CACHE_FILE = "permanent_cache.json"



def load_cache():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)
    return {}

def save_cache(cache_data):
    with open(CACHE_FILE, "w") as f:
        json.dump(cache_data, f, indent=4)

def cached_get(url, params):
    
    cache = load_cache()
    key = url + "|" + json.dumps(params, sort_keys=True)

    if key in cache:
        return cache[key]

    
    fake_result = {"Error": "No online access in offline mode"}

    cache[key] = fake_result
    save_cache(cache)

    return fake_result



DAD_JOKES = [
    "Why don't eggs tell jokes? — They'd crack each other up.",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "Why did the scarecrow win an award? — He was outstanding in his field.",
    "Why don’t programmers like nature? — Too many bugs."
]

def get_movie(title):
    url = "http://www.omdbapi.com/"
    params = {"t": title}
    return cached_get(url, params)

def generate_joke():
    return random.choice(DAD_JOKES)

def create_mix(title):
    movie = get_movie(title)
    joke = generate_joke()

    return {
        "movie": movie.get("Title"),
        "year": movie.get("Year"),
        "plot": movie.get("Plot"),
        "joke": joke
    }

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print('Usage: python haha_me.py "Movie Title"')
        exit(1)

    title = " ".join(sys.argv[1:])
    result = create_mix(title)
    print(json.dumps(result, indent=4))
