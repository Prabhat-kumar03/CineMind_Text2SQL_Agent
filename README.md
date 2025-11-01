# 🔥 CineMind_Text2SQL_Agent 🤖

> `text2sql` for cinema DB • built like a hacker tool • terminal-native energy

```
$ ask "top 5 movies this week by booking?"
→ SELECT movie_name, COUNT(*) ...
```

```
 ██████╗██╗███╗   ██╗███████╗███╗   ███╗██╗███╗   ██╗██████╗ 
██╔════╝██║████╗  ██║██╔════╝████╗ ████║██║████╗  ██║██╔══██╗
██║     ██║██╔██╗ ██║█████╗  ██╔████╔██║██║██╔██╗ ██║██║  ██║
██║     ██║██║╚██╗██║██╔══╝  ██║╚██╔╝██║██║██║╚██╗██║██║  ██║
╚██████╗██║██║ ╚████║███████╗██║ ╚═╝ ██║██║██║ ╚████║██████╔╝
 ╚═════╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═════╝ 
```

## Tech Stack 🧬

| Layer | Tech |
|---|---|
| LLM text2sql | Python + LLM provider |
| Database | MySQL |
| App glue | Python (modular functions) |

## Features ✨
- Natural language → SQL generation (text2sql).
- Query execution on a MySQL database.
- Human-friendly response formatting.
- Minimal, easy-to-read Python codebase intended for experimentation and integration.

## Repository layout
```
.env                 # environment variables (DB credentials, API keys)
app.py               # main entry point / API wrapper
database.py          # MySQL connection & helper functions
generate_sql.py      # logic that turns NL into SQL
generate_response.py # converts DB results into readable text
notes.md             # developer notes
__pycache__/         # compiled python files
```

## Requirements
- Python 3.8+ (or newer)
- MySQL server (or accessible MySQL instance)
- Python packages listed in `requirements.txt` (if you add one). Typical packages: `mysql-connector-python` (or `pymysql`), `openai` (or other LLM client), and `python-dotenv`.

## Setup
1. Clone the repo:
```bash
git clone https://github.com/Prabhat-kumar03/CineMind_Text2SQL_Agent.git
cd CineMind_Text2SQL_Agent
```
2. Create and populate a `.env` file with your configuration (example keys shown below).
3. Install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### Suggested `.env` variables
```
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=username
MYSQL_PASSWORD=password
MYSQL_DATABASE=cinemind_db
GOOGLE_API_KEY=sk-...      # if using Google genai LLM
```

## Usage 🚀
Run the main application (or integrate the functions in `generate_sql.py` / `generate_response.py` into your app):
```bash
python app.py
```

Example flow:
1. User asks: "Which movies are booked more than 100 seats on 2025-10-15?"
2. `generate_sql.py` produces a SELECT query.
3. `database.py` runs the query against MySQL and returns rows.
4. `generate_response.py` formats rows into a readable summary.

## Design notes
- The code is intentionally modular: SQL generation, DB access, and response formatting live in separate files to make testing and replacement simple.
- Keep production safety in mind: validate/parameterize generated SQL before running it on production databases.

## Contributing
- Create issues for bugs or feature requests.
- Open a PR with a clear description of changes.
- Add tests for new logic, especially around SQL generation and sanitization.

## Security & privacy
- Never commit real credentials or API keys. Add `.env` to `.gitignore`.
- Sanitize and review generated SQL before executing against sensitive production data.

## Next steps / ideas
- Add a `requirements.txt` and a Dockerfile for easier setup.
- Add unit tests and integration tests that mock the DB and LLM.
- Add a simple web UI to demo prompt→results flow.

## License
Add a license (e.g. MIT) to make your intentions clear.

---

> AI agent that auto-writes SQL for a cinema booking database and returns clean, human-readable answers.
