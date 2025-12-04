Понял тебя, вот полностью готовый **README.md** в один файл, можно просто скопировать целиком без разделения на ячейки и лишних комментариев:

````markdown
# 🎬 OMDb Dad Jokes Mashup

A fun Python project that combines movie information with dad jokes!  
Enter a movie title and get its plot along with a related dad joke.

Created by **Denis Naumov**.

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/DenisNaumov7777/omdb-dad-jokes-mashup.git
cd omdb-dad-jokes-mashup
````

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

> ⚠️ This project works fully offline using the provided cache, so you **do not need an OMDb API key** unless you want to fetch live data.

---

## ▶️ Usage

Run the script from the terminal:

```bash
python main.py "The Matrix"
```

Example output:

```
Movie: The Matrix
Year: 1999
Plot: A computer hacker learns about the true nature of reality and his role in the war against its controllers.
Dad joke: Why don’t programmers like nature? — Too many bugs.
```

> Works offline using cached movie data — no internet required.

---

## 🛠 Project Structure

```
OMDb-dad-jokes-mashup/
│
├── haha_me.py
├── main.py
├── tests.py
├── requests_with_caching.py
├── permanent_cache.json
├── requirements.txt
├── README.md
└── __init__.py
```

---

## ✅ Features

* Fetch movie info from offline cache
* Add dad jokes related to the movie plot
* Fully offline, no internet required
* Easy CLI interface
* Works with multiple movies in cache
* Unit tests included

---

## 🧪 Running Tests

```bash
python -m unittest tests.py
```

Example output:

```
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```

---

## ⚠️ Notes

* Make sure all files (`haha_me.py`, `main.py`, `requests_with_caching.py`, `permanent_cache.json`) are in the **same folder**.
* Use `python main.py "Movie Title"` instead of `python haha_me.py` for CLI usage.
* The project is **offline by default**, but you can modify `cached_get` to fetch live data if you have an OMDb API key.

---

## 📄 License

This project is licensed under the MIT License.

Made with ❤️ by **Denis Naumov**

```

---

