# Python Challenge Day a Day — Roadmap

Step-by-step list of **exactly what to study**. Pick a step, study the topic (docs, courses, videos), code in a folder (e.g. `day-000`), then mark **Done** and commit.

---

## Stage 0 — Basics

| Step | Topic | Exactly what to study | Done |
|------|--------|------------------------|------|
| 0 | Variables and Hello World | Variables, `print()`, first script | [x] |
| 1 | Data types | `int`, `float`, `str`, `bool`, `list`, `tuple`, `range`, `dict`, `type()` | [ ] |
| 2 | Operators | Arithmetic, comparison, assignment | [ ] |
| 3 | User input | `input()`, converting to int/float | [ ] |
| 4 | Strings (basics) | Concatenation, f-strings, indexing, slicing | [ ] |
| 5 | Strings (methods) | `.strip()`, `.split()`, `.upper()`, `.lower()`, `.replace()` | [ ] |
| 6 | Conditionals — `if` | `if`, `else`, simple conditions | [ ] |
| 7 | Conditionals — `elif` | `elif`, multiple conditions, nested `if` | [ ] |
| 8 | Loop `for` | `for`, `range()`, iterating sequences | [ ] |
| 9 | Loop `while` | `while`, stopping condition | [ ] |
| 10 | `break` and `continue` | Exit loop, skip iteration | [ ] |
| 11 | List (create and access) | Create list, indices, slicing | [ ] |
| 12 | List (modify) | `.append()`, `.remove()`, change by index | [ ] |
| 13 | List (methods) | `.sort()`, `.reverse()`, `len()`, `in` | [ ] |
| 14 | Tuples | Tuples vs lists, immutability | [ ] |
| 15 | Dictionaries (basics) | Key/value, access, change values | [ ] |
| 16 | Dictionaries (methods) | `.keys()`, `.values()`, `.items()` | [ ] |
| 17 | Sets | Sets, no duplicates, set operations | [ ] |
| 18 | Review structures | Exercise: lists, dicts, sets together | [ ] |
| 19 | Comprehensions | List comprehension, dict/set (optional) | [ ] |

---

## Stage 1 — Core programming

| Step | Topic | Exactly what to study | Done |
|------|--------|------------------------|------|
| 20 | Functions (define and call) | `def`, parameters, `return` | [ ] |
| 21 | Parameters and arguments | Positional, default, `*args` (optional) | [ ] |
| 22 | Variable scope | Local vs global | [ ] |
| 23 | Modules and `import` | `import`, `from ... import` | [ ] |
| 24 | Error handling | `try`, `except`, common exceptions | [ ] |
| 25 | Files (text) | `open()`, `read()`, `write()`, `with` | [ ] |
| 26 | Read line by line | `readlines()`, loop over lines | [ ] |
| 27 | CSV (read) | `csv.reader` or split by comma | [ ] |
| 28 | CSV (write) | `csv.writer`, export data | [ ] |
| 29 | Paths and folders | `pathlib` or `os.path` | [ ] |
| 30 | Small project: script + file | Script that reads/writes txt or CSV | [ ] |
| 31 | Review functions and files | Exercise combining above | [ ] |
| 32 | Dates and time | `datetime`, `date`, `strftime` | [ ] |
| 33 | Regular expressions | `re.search`, `re.findall` | [ ] |
| 34 | Style and good practices | PEP 8, naming, comments | [ ] |

---

## Stage 2 — Core libraries

| Step | Topic | Exactly what to study | Done |
|------|--------|------------------------|------|
| 35 | `math` | `math.sqrt`, `math.floor`, `math.ceil`, constants | [ ] |
| 36 | `json` | `json.load()`, `json.dumps()`, read/write JSON | [ ] |
| 37 | `datetime` (deeper) | `timedelta`, format, parse strings | [ ] |
| 38 | `os` and `sys` | `os.listdir()`, `os.path.join()`, `sys.argv` | [ ] |
| 39 | CLI scripts | Command-line arguments, simple CLI | [ ] |
| 40 | Review core libraries | Script with math, json, datetime, or os | [ ] |

---

## Stage 3 — Data Science & Analytics

| Step | Topic | Exactly what to study | Done |
|------|--------|------------------------|------|
| 41 | Pandas (install and import) | `pip install pandas`, `import pandas as pd` | [ ] |
| 42 | Series | Create Series, index, operations | [ ] |
| 43 | DataFrame (create) | DataFrame from dict or list of dicts | [ ] |
| 44 | Read CSV | `pd.read_csv()`, basic parameters | [ ] |
| 45 | Explore DataFrame | `.head()`, `.info()`, `.describe()`, `.shape` | [ ] |
| 46 | Select columns and rows | Columns, `.loc`, `.iloc` (basics) | [ ] |
| 47 | Filters | Boolean indexing, filter rows | [ ] |
| 48 | Sort and rank | `.sort_values()`, `.sort_index()` | [ ] |
| 49 | Missing values | `.isna()`, `.dropna()`, `.fillna()` | [ ] |
| 50 | Simple aggregations | `.sum()`, `.mean()`, `.count()` | [ ] |
| 51 | groupby (basics) | `.groupby()`, one aggregator | [ ] |
| 52 | groupby (multiple) | `.agg()`, several functions | [ ] |
| 53 | New columns | Compute column, `.apply()` (simple) | [ ] |
| 54 | Merge and join | `pd.merge()`, `.join()` | [ ] |
| 55 | Concat DataFrames | `pd.concat()` | [ ] |
| 56 | Project: analyze CSV | Pick dataset, explore, summarize | [ ] |
| 57 | Export | `.to_csv()`, `.to_excel()` (optional) | [ ] |
| 58 | Cleaning (strings) | Normalize text, strip spaces | [ ] |
| 59 | Cleaning (dates and types) | Datetime, numeric types | [ ] |
| 60 | matplotlib (basics) | `plt.plot()`, `plt.show()`, figure/axes | [ ] |
| 61 | Bar and pie charts | Bar, pie, legends | [ ] |
| 62 | Histograms | `plt.hist()`, bins | [ ] |
| 63 | Pandas + matplotlib | `.plot()` on Series/DataFrame | [ ] |
| 64 | Seaborn (intro) | Install, first plot | [ ] |
| 65 | Seaborn: bars and boxplots | Common plot types | [ ] |
| 66 | Exploratory charts | Right chart for the data | [ ] |
| 67 | Descriptive statistics | Mean, median, std, correlation | [ ] |
| 68 | Project: report with charts | CSV + tables + 2–3 charts | [ ] |
| 69 | JSON and APIs | `json.load()`, `requests.get()`, to DataFrame | [ ] |
| 70 | Review: external data | CSV + API or JSON in one script | [ ] |
| 71 | Virtual env | `venv`, `pip freeze`, `requirements.txt` | [ ] |
| 72 | Project: simple pipeline | Read → clean → aggregate → save/plot | [ ] |
| 73 | SQL in Python (concept) | Connect SQLite, run query | [ ] |
| 74 | SQL queries in Python | SELECT and load into pandas | [ ] |

---

## Stage 4 — Machine Learning & AI

| Step | Topic | Exactly what to study | Done |
|------|--------|------------------------|------|
| 75 | Train/test split | Split data, avoid leakage | [ ] |
| 76 | scikit-learn (intro) | Fit first model (regression or classifier) | [ ] |
| 77 | Regression (basics) | Linear regression, MAE, RMSE, R² | [ ] |
| 78 | Classification (basics) | Logistic regression or tree, accuracy, confusion matrix | [ ] |
| 79 | Clustering (basics) | K-means, visualize clusters | [ ] |
| 80 | Preprocessing | Scaling (e.g. StandardScaler), encode categories | [ ] |
| 81 | Pipelines | `Pipeline`, preprocessing + model | [ ] |
| 82 | Model selection | Cross-validation, compare models | [ ] |
| 83 | Project: ML end-to-end | Load → preprocess → train → evaluate | [ ] |
| 84 | Optional: NLP intro | Text as features, bag-of-words or TF-IDF | [ ] |
| 85 | Optional: LLM APIs | Call LLM API from Python | [ ] |
| 86 | Review and portfolio | Pick 3 projects, document them | [ ] |

---

When you finish a step, mark `[x]` in **Done**, update `progress.md` if you like, and commit. No fixed schedule — go at your own pace.
