# 🛡️ Day 8 In-Class Activity: Mastering File Systems, File I/O & Exception Handling

- **Course:** Python Programming
- **Session:** Day 8 (Liang Chapter 13: Files and Exception Handling)
- **Pedagogical Scope:** Persistent disk storage vs volatile RAM, file access modes (`'r'`, `'w'`, `'a'`, `'x'`), safe resource management with the `with` context manager, line-by-line streaming traversal, text encoding (`utf-8`), buffer flushing, file pointers (`tell` & `seek`), filesystem navigation and inspection via `os` & `os.path` (`exists`, `isfile`, `isdir`, `join`, `getsize`, `listdir`, `makedirs`), modern object-oriented paths via `pathlib.Path`, defensive error handling (`try-except-else-finally`, `FileNotFoundError`, `PermissionError`), and processing structured text files (CSV records and delimited server logs).
- **Textbook Alignment:** Liang, *Introduction to Programming Using Python*, Chapter 13 (Files and Exception Handling).
- **Time Allocated:** 45–60 minutes
- **Files in this folder:**
  - [`tutorial_file_system.md`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/tutorial_file_system.md) — Comprehensive master teaching tutorial and lecture notes for the instructor and students.
  - [`concepts_demo.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/concepts_demo.py) — Runnable master reference guide demonstrating all 8 file I/O and file system topics.
  - [`bug_hunt_day8.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/bug_hunt_day8.py) — 5 debugging mini-challenges on accidental overwrite traps, missing newlines in `.write()`, trailing newline string comparison traps, cross-platform path concatenation, and unhandled `FileNotFoundError` crashes.
  - [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/practice_drills.py) — 3 quick 5-minute warm-up drills (safe journal logging, directory storage inspection, and server log metrics aggregation).
  - [`file_helpers.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/file_helpers.py) — Modular helper library containing `ensure_directory()`, `format_file_size()`, `get_file_metadata()`, `safe_read_text()`, `safe_write_text()`, and `scan_directory()`.
  - [`starter_log_sentinel.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/starter_log_sentinel.py) — Guided student starter template for the main hands-on lab.
  - [`solution_log_sentinel.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/solution_log_sentinel.py) — Complete instructor reference solution.

---

## 🎯 Learning Objectives

1. **Understand Persistent Storage vs Volatile RAM**: Contrast dynamic in-memory data structures with permanent disk storage (Liang 13.1).
2. **Master Context-Managed File Operations**: Safely open, read, write, and append to files using `with open(..., mode, encoding='utf-8') as f` to guarantee deterministic resource cleanup (Liang 13.2).
3. **Differentiate File Access Modes**: Prevent data loss by understanding the consequences of `'r'` (read), `'w'` (truncate/overwrite), `'a'` (append), and `'x'` (exclusive creation) (Liang 13.2).
4. **Choose Optimal Reading Strategies**: Contrast `f.read()`, `f.readline()`, `f.readlines()`, and stream iteration `for line in f:` for memory efficiency with large data sets (Liang 13.2).
5. **Navigate and Query the File System**: Use `os` and `os.path` to check file existence (`exists`, `isfile`, `isdir`), safely construct cross-platform paths (`os.path.join`), inspect sizes (`os.path.getsize`), and create nested directory structures (`os.makedirs`) (Liang 13.4).
6. **Apply Modern Path Handling**: Leverage Python 3's `pathlib.Path` syntax for intuitive object-oriented path manipulation and pattern matching (`glob`) (Liang 13.4).
7. **Implement Defensive Error Handling**: Wrap file I/O operations inside `try ... except (FileNotFoundError, PermissionError) ... else ... finally` blocks to safeguard production systems against crashes (Liang 13.3).
8. **Parse Delimited Structured Records**: Parse CSV tables and pipe-delimited cluster logs into actionable business metrics and export clean executive reports (Liang 13.5).

---

## 📋 Activity Roadmap

### Part 1: Interactive Shell Warm-up (10 mins)

Open your terminal or interactive Python shell and test these fundamental file operations:

```python
# 1. Writing with the 'with' statement
>>> with open("test.txt", "w", encoding="utf-8") as f:
...     f.write("Line 1: Hello File System!\n")
...     f.write("Line 2: Python 3 I/O\n")
... 
>>> f.closed
True

# 2. Reading back via stream iteration
>>> with open("test.txt", "r", encoding="utf-8") as f:
...     for line in f:
...         print(line.rstrip())
... 
Line 1: Hello File System!
Line 2: Python 3 I/O

# 3. Path inspection via os.path
>>> import os
>>> os.path.exists("test.txt")
True
>>> os.path.getsize("test.txt")
48
>>> os.path.split("Day-8/incoming_logs/auth.log")
('Day-8/incoming_logs', 'auth.log')

# 4. Clean up
>>> os.remove("test.txt")
```

---

### Part 2: The Bug Hunt (15 mins)

Open [`bug_hunt_day8.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/bug_hunt_day8.py). Uncomment each challenge, run the script, examine the error or faulty output, and fix the bugs:

- **Challenge 1:** *The Accidental Overwrite Trap* — Replacing mode `'w'` with append mode `'a'` so multiple logging events don't wipe prior entries.
- **Challenge 2:** *The Missing Newline Trap in `.write()`* — Appending explicit `\n` to prevent words from being glued together.
- **Challenge 3:** *Trailing Newline Comparison Trap* — Calling `line.strip()` so `"APPROVED\n"` matches `"APPROVED"`.
- **Challenge 4:** *Cross-Platform Path Concatenation Bug* — Replacing string concatenation with `os.path.join()`.
- **Challenge 5:** *Unhandled FileNotFoundError Crash* — Wrapping missing file lookups in a defensive `try-except FileNotFoundError` block with default fallback data.

Run to verify:

```bash
python3 Day-8/bug_hunt_day8.py
```

---

### Part 3: Quick Concept Drills (10 mins)

Open [`practice_drills.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/practice_drills.py) to complete three rapid coding checkpoints:

1. **Drill 1 (Developer Journal):** Initialize a journal file, append timestamped developer notes with `'a'`, and read back all lines numbered.
2. **Drill 2 (Directory Inspector & Storage Auditor):** Inspect multiple files using `os.listdir()` and `os.path.getsize()`, displaying a formatted metadata table and total byte consumption.
3. **Drill 3 (Server Log Health Aggregator):** Read simulated server logs, split records by `" | "`, count HTTP 200 vs error codes, and compute average latency.

Run to verify:

```bash
python3 Day-8/practice_drills.py
```

---

### Part 4: Main Lab — LogSentinel Cluster Auditor (25–35 mins)

Open [`starter_log_sentinel.py`](file:///Users/dipenparihar/Documents/CBC/Python-5-Oct/Day-8/starter_log_sentinel.py). Complete the 6 guided TODO sections:

1. **Step 1:** Ensure incoming, report, and archive directories exist.
2. **Step 2:** Scan incoming logs using `scan_directory()` and compute total storage volume.
3. **Step 3:** Stream through every log line, parsing timestamps, levels, status codes, and error messages.
4. **Step 4:** Generate an executive markdown/text audit summary report into `reports/audit_summary.txt`.
5. **Step 5:** Export all high-severity incidents (`ERROR` and `CRITICAL`) to a formatted CSV file `reports/security_alerts.csv`.
6. **Step 6:** Implement defensive error handling for missing files.

Run to verify:

```bash
python3 Day-8/starter_log_sentinel.py
```

Inspect reference solution if needed:

```bash
python3 Day-8/solution_log_sentinel.py
```

---

## 💡 Key Concept Cheat Sheet

```python
# 1. SAFE READING (Memory efficient stream)
with open("data.log", mode="r", encoding="utf-8") as f:
    for line in f:
        clean = line.strip()

# 2. SAFE APPENDING
with open("data.log", mode="a", encoding="utf-8") as f:
    f.write(f"[{timestamp}] New entry recorded\n")

# 3. DIRECTORY SCANNING & METADATA
import os
for entry in sorted(os.listdir("logs")):
    path = os.path.join("logs", entry)
    if os.path.isfile(path):
        size = os.path.getsize(path)

# 4. DEFENSIVE ERROR HANDLING
try:
    with open("config.json", "r") as f:
        data = f.read()
except FileNotFoundError:
    data = "{}"  # Default fallback
```

