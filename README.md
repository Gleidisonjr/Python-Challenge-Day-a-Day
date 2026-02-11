# Python Challenge Day a Day

Personal challenge: learn Python from **zero to advanced**, step by step. No fixed schedule — complete at your own pace. Covers fundamentals, core libraries, then advanced topics: **Data Science**, **Data Analytics**, **Machine Learning**, and **AI**.

---

## Objectives

- **Python:** Learn Python from zero to advanced (basics, core libraries, Data Science, Analytics, ML & AI) following the roadmap step by step.
- **English:** Improve and train English for my professional career. Documentation, commits, and practice in this project are also used to build fluency and technical English.

---

## How I use Cursor in this project

- **Commits and deploy:** I use Cursor to manage commits and push this project (e.g. to GitHub).
- **Learning support:** Cursor helps me understand topics, clarify doubts, and learn.
- **Code assistance only:** I write the code myself. At most, I use Cursor to get help with solutions, fix errors, and resolve issues — but the coding is done by me. I do not use AI to generate my code; I use it to support and unblock me while I practice.

---

## About this challenge

- **Personal challenge** — your rhythm, your roadmap.
- **No fixed days** — no pressure to finish by a certain date; focus on consistency and understanding.
- **Step by step** — each stage lists **exactly what to study** so you know the content.
- **Create your own stages** — use the suggested breakdown below or adapt it; the important part is studying everything in order (basics first, then advanced).

---

## Suggested roadmap — what to study (by stage)

Below is a **specific** list of what to study in each stage. One topic per step; study that topic (docs, courses, videos), then practice in a folder (e.g. `day-000`, `day-001`) and move to the next.

---

### Stage 0 — Basics (Python fundamentals)

**What to study, step by step:**

| Step | Topic | Exactly what to study |
|------|--------|------------------------|
| 0 | Variables and Hello World | Variables, `print()`, running your first script |
| 1 | Data types | `int`, `float`, `str`, `bool`, `list`, `tuple`, `range`, `dict`, and `type()` |
| 2 | Operators | Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`), comparison (`==`, `!=`, `<`, `>`), assignment (`=`, `+=`) |
| 3 | User input | `input()`, converting input to int/float (e.g. `int(input())`) |
| 4 | Strings (basics) | Concatenation (`+`), f-strings (`f"..."`), indexing and slicing |
| 5 | Strings (methods) | `.strip()`, `.split()`, `.upper()`, `.lower()`, `.replace()`, etc. |
| 6 | Conditionals — `if` | `if` and `else`, simple conditions |
| 7 | Conditionals — `elif` | Multiple conditions with `elif`, nested `if` |
| 8 | Loop `for` | `for` loop, `range()`, iterating over a sequence |
| 9 | Loop `while` | `while` loop, condition to stop the loop |
| 10 | `break` and `continue` | Exiting a loop with `break`, skipping an iteration with `continue` |
| 11 | Lists (create and access) | Creating lists, indexing, slicing |
| 12 | Lists (modify) | `.append()`, `.remove()`, changing items by index |
| 13 | Lists (methods) | `.sort()`, `.reverse()`, `len()`, `in` |
| 14 | Tuples | Tuples vs lists, immutability |
| 15 | Dictionaries (basics) | Key/value pairs, accessing and changing values |
| 16 | Dictionaries (methods) | `.keys()`, `.values()`, `.items()` |
| 17 | Sets | Sets, no duplicates, set operations |
| 18 | Review structures | Exercise mixing lists, dicts, and sets |
| 19 | Comprehensions | List comprehensions `[x for x in ...]` (and dict/set if you want) |

---

### Stage 1 — Core programming (functions and files)

**What to study, step by step:**

| Step | Topic | Exactly what to study |
|------|--------|------------------------|
| 20 | Functions (define and call) | `def`, parameters, `return` |
| 21 | Parameters and arguments | Positional, default values, `*args` (optional) |
| 22 | Variable scope | Local vs global scope |
| 23 | Modules and `import` | `import module`, `from module import name` |
| 24 | Error handling | `try`, `except`, common exceptions |
| 25 | Working with files (text) | `open()`, `read()`, `write()`, `with` |
| 26 | Reading line by line | `readlines()`, looping over lines |
| 27 | CSV (reading) | `csv.reader` or splitting by comma |
| 28 | CSV (writing) | `csv.writer`, exporting data |
| 29 | Paths and folders | `pathlib` or `os.path` |
| 30 | Small project: script + file | One script that reads/writes a text or CSV file |
| 31 | Review functions and files | Exercise combining everything above |
| 32 | Dates and time (basics) | `datetime`, `date`, `strftime` |
| 33 | Regular expressions (basics) | `re.search`, `re.findall` on text |
| 34 | Style and good practices | PEP 8, clear names, comments |

---

### Stage 2 — Core libraries (stdlib and scripts)

**What to study, step by step:**

| Step | Topic | Exactly what to study |
|------|--------|------------------------|
| 35 | `math` | `math.sqrt`, `math.floor`, `math.ceil`, constants |
| 36 | `json` | `json.load()`, `json.dumps()`, reading/writing JSON files |
| 37 | `datetime` (deeper) | `timedelta`, formatting, parsing strings |
| 38 | `os` and `sys` | `os.listdir()`, `os.path.join()`, `sys.argv` for CLI |
| 39 | Environment and CLI | Command-line arguments, simple CLI scripts |
| 40 | Review core libraries | Small script using `math`, `json`, `datetime`, or `os` |

---

### Stage 3 — Data Science & Analytics (pandas and visualization)

**What to study, step by step:**

| Step | Topic | Exactly what to study |
|------|--------|------------------------|
| 41 | Install and import pandas | `pip install pandas`, `import pandas as pd` |
| 42 | Series | Creating Series, index, basic operations |
| 43 | DataFrame (create) | DataFrame from dict or list of dicts |
| 44 | Read CSV with pandas | `pd.read_csv()`, basic parameters |
| 45 | Explore DataFrame | `.head()`, `.info()`, `.describe()`, `.shape` |
| 46 | Select columns and rows | Selecting columns, `.loc`, `.iloc` (basics) |
| 47 | Filters (boolean indexing) | Masks, filtering rows by condition |
| 48 | Sort and rank | `.sort_values()`, `.sort_index()` |
| 49 | Missing values | `.isna()`, `.dropna()`, `.fillna()` |
| 50 | Simple aggregations | `.sum()`, `.mean()`, `.count()` per column |
| 51 | `groupby` (basics) | `.groupby()`, one aggregator |
| 52 | `groupby` (multiple) | `.agg()`, several functions at once |
| 53 | New columns and transforms | Computing columns, simple `.apply()` |
| 54 | Merge and join (basics) | `pd.merge()` or `.join()` |
| 55 | Concat DataFrames | `pd.concat()` |
| 56 | Project: analyze a CSV | Pick a dataset, explore and summarize |
| 57 | Export results | `.to_csv()`, `.to_excel()` (optional) |
| 58 | Data cleaning (strings) | Normalize text, strip spaces |
| 59 | Data cleaning (dates and types) | Convert to datetime, numeric types |
| 60 | matplotlib (basics) | `plt.plot()`, `plt.show()`, figure and axes |
| 61 | Bar and pie charts | Bar charts, pie charts, legends |
| 62 | Histograms | `plt.hist()`, bins |
| 63 | Pandas + matplotlib | `.plot()` on Series/DataFrame |
| 64 | Seaborn (intro) | Install, first plot |
| 65 | Seaborn: bars and boxplots | Common plot types |
| 66 | Exploratory charts | Choosing the right chart for a dataset |
| 67 | Descriptive statistics | Mean, median, std, correlation |
| 68 | Project: report with charts | One CSV + tables + 2–3 charts |
| 69 | JSON and APIs | `json.load()`, `requests.get()`, turn response into DataFrame |
| 70 | Review: external data | CSV + API or JSON in one script |
| 71 | Virtual env and dependencies | `venv`, `pip freeze`, `requirements.txt` |
| 72 | Project: simple pipeline | Read → clean → aggregate → save or plot |
| 73 | SQL in Python (concept) | Connect to SQLite (or similar), run a query |
| 74 | SQL queries in Python | Execute SELECT and load into pandas |

---

### Stage 4 — Machine Learning & AI (ML basics and projects)

**What to study, step by step:**

| Step | Topic | Exactly what to study |
|------|--------|------------------------|
| 75 | Train/test split | Splitting data, avoiding leakage |
| 76 | scikit-learn (intro) | Fit a first model (e.g. linear regression or classifier) |
| 77 | Regression (basics) | Linear regression, metrics (MAE, RMSE, R²) |
| 78 | Classification (basics) | Logistic regression or tree, accuracy, confusion matrix |
| 79 | Clustering (basics) | K-means, visualizing clusters |
| 80 | Preprocessing | Scaling (e.g. StandardScaler), encoding categories |
| 81 | Pipelines in scikit-learn | `Pipeline`, combine preprocessing + model |
| 82 | Model selection | Cross-validation, comparing models |
| 83 | Project: ML end-to-end | Load data → preprocess → train → evaluate |
| 84 | Optional: NLP intro | Text as features, simple bag-of-words or TF-IDF |
| 85 | Optional: LLM APIs | Calling an LLM API from Python (e.g. for a small project) |
| 86 | Review and portfolio | Pick 3 projects to highlight, document them |

---

## How to use this repo

1. **Pick a step** from the table above (or from [ROADMAP.md](ROADMAP.md) if you use the day-by-day version).
2. **Study** that topic — docs, courses, videos.
3. **Code** — create a folder (e.g. `day-000`, `day-001`) and put your scripts there.
4. **Track progress** — mark what you've done in [ROADMAP.md](ROADMAP.md) or `progress.md`.
5. **Commit often** — small commits to keep the challenge going.

---

## Repository structure (suggestion)

```
Python-Challenge-Day-a-Day/
├── README.md           # This file (roadmap summary)
├── ROADMAP.md          # Full day-by-day list — mark done items here
├── progress.md         # Optional: dates, what you studied
├── day-000/            # Step 0: variables, print, first script
├── day-001/            # Step 1: types
├── ...
└── projects/           # Optional: larger projects (DS or ML)
```

---

## Summary by stage

| Stage | What you study (overview) |
|-------|---------------------------|
| **0** | Variables, types, operators, `print`, `input`, strings, conditionals, loops, lists, tuples, dicts, sets, comprehensions |
| **1** | Functions, parameters, scope, modules, errors, files (txt/CSV), paths, dates, regex, PEP 8 |
| **2** | `math`, `json`, `datetime`, `os`, `sys`, CLI scripts |
| **3** | Pandas (Series, DataFrame, read/filter/group/merge), cleaning, matplotlib, Seaborn, APIs, JSON, SQL in Python, pipelines |
| **4** | Train/test, scikit-learn (regression, classification, clustering), preprocessing, pipelines, ML project; optional NLP/LLM |

No fixed day count. Go step by step, study exactly what’s in each row, and build your own pace. Good luck with your Python Challenge Day a Day.
