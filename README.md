# OMDb Dad Jokes Mashup  
Author: Denis Naumov

A playful Python project that mixes movie information from the OMDb API with classic dad-style jokes.  
The script fetches movie data, generates random dad jokes, caches API responses, and logs activity — all in one workflow.

---

## 🚀 Features

- Fetches movie details from **OMDb API**
- Injects a random **dad joke** into the output
- Uses a **cache system** to avoid repeated API calls
- Saves results into a local `.txt` file
- Logs all operations to `journal.log`
- Works from CLI or as imported module

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/DenisNaumov7777/omdb-dad-jokes-mashup.git
cd omdb-dad-jokes-mashup

2. Install dependencies:

pip install -r requirements.txt



3. Set your OMDb API key:
Put it into environment variable:
export OMDB_API_KEY=your_api_key_here
or
Add inside .env file:
OMDB_API_KEY=your_api_key_here

▶️ Usage
Run script from terminal:
python main.py "The Matrix"

Example output:
Movie: The Matrix
Year: 1999
Genre: Action, Sci-Fi
Plot: A computer hacker learns about the true nature of reality...
Dad joke: Why don’t programmers like nature? — Too many bugs.

