# 📖 Python File System & File I/O: Instructor & Student Master Teaching Guide

> **Course:** Python Programming  
> **Session:** Day 8 (Chapter 13: Files, File System & Exception Handling)  
> **Textbook Alignment:** Liang, *Introduction to Programming Using Python*, Chapter 13  
> **Target Audience:** Instructor lecture guide and student reference manual  

---

## 📑 Table of Contents

1. [Why Do We Need File Systems? (RAM vs Disk)](#1-why-do-we-need-file-systems-ram-vs-disk)
2. [File Paths: Absolute vs Relative](#2-file-paths-absolute-vs-relative)
3. [Opening & Closing Files: The `with` Statement](#3-opening--closing-files-the-with-statement)
4. [File Modes Demystified (`r`, `w`, `a`, `x`)](#4-file-modes-demystified-r-w-a-x)
5. [The 4 Ways to Read Files in Python](#5-the-4-ways-to-read-files-in-python)
6. [Writing & Appending Data (The `\n` Gotcha)](#6-writing--appending-data-the-n-gotcha)
7. [The File Pointer: `tell()` and `seek()`](#7-the-file-pointer-tell-and-seek)
8. [Navigating the File System with `os` and `os.path`](#8-navigating-the-file-system-with-os-and-ospath)
9. [Modern File Paths with `pathlib.Path`](#9-modern-file-paths-with-pathlibpath)
10. [Defensive Programming & Exception Handling](#10-defensive-programming--exception-handling)
11. [Working with Structured Files (CSV & Delimited Logs)](#11-working-with-structured-files-csv--delimited-logs)
12. [Top 5 Traps & Pitfalls in Python File I/O](#12-top-5-traps--pitfalls-in-python-file-io)
13. [Classroom Discussion Questions & Live Demos](#13-classroom-discussion-questions--live-demos)

---

## 1. Why Do We Need File Systems? (RAM vs Disk)

In earlier sessions, everything stored in Python variables (`x = 42`, `names = ["Alice", "Bob"]`) resided inside **RAM (Random Access Memory)**:

| Characteristic | Primary Memory (RAM) | Secondary Storage (Disk / SSD) |
| :--- | :--- | :--- |
| **Persistence** | **Volatile** (data disappears when Python exits or power turns off) | **Non-volatile** (data persists permanently until deleted) |
| **Speed** | Extremely fast (nanoseconds) | Slower than RAM (microseconds to milliseconds) |
| **Capacity** | Limited (e.g., 8 GB – 32 GB) | Massive (e.g., 512 GB – 4 TB+) |
| **Usage** | Program execution & active calculation | Storing logs, databases, user profiles, documents |

> **Key Takeaway for Students:**  
> Files allow our Python applications to save their state, load historical data, generate reports, communicate between different programs, and survive system reboots.

---

## 2. File Paths: Absolute vs Relative

A **path** is the address string specifying the location of a file or folder in the operating system's directory tree.

```
Root Directory /
├── Users/
│   └── dipenparihar/
│       └── Documents/
│           └── Python-5-Oct/          <-- Working Directory (cwd)
│               ├── Day-8/
│               │   ├── incoming_logs/
│               │   │   └── auth.log   <-- Target File
│               │   └── concepts_demo.py
```

### Absolute Path
- Specifies the exact, full location starting from the root of the filesystem.
- **macOS / Linux:** Starts with `/` (e.g. `/Users/dipenparihar/Documents/CBC/Day-8/auth.log`)
- **Windows:** Starts with a drive letter (e.g. `C:\Users\Student\Documents\Day-8\auth.log`)

### Relative Path
- Specifies the location relative to the **Current Working Directory (`os.getcwd()`)**.
- `.` represents the current directory (`./incoming_logs/auth.log`)
- `..` represents the parent directory (`../Day-7/matrix_helpers.py`)

```python
import os

# Where is Python currently looking?
print("Current Working Directory:", os.getcwd())

# Convert a relative path to an absolute path
rel_path = "incoming_logs/auth.log"
abs_path = os.path.abspath(rel_path)
print("Resolved Absolute Path:", abs_path)
```

---

## 3. Opening & Closing Files: The `with` Statement

To interact with a file on disk, Python must request an open **file stream / handle** from the Operating System.

### The Old / Dangerous Way (Manual `.close()`):
```python
# ⚠️ RISKY: If an error happens before f.close(), the file handle leaks!
f = open("data.txt", "w")
f.write("Important data")
f.close()
```

### The Modern Pythonic Way: The `with` Statement (Context Manager)
The `with` keyword automatically closes the file the exact millisecond execution leaves the indented block—even if an exception crashes your program!

```python
with open("data.txt", mode="w", encoding="utf-8") as f:
    f.write("Line 1: Stored safely!\n")
    f.write("Line 2: Automatically flushed to disk.\n")

# File is GUARANTEED to be closed here:
print("Is file closed?", f.closed)  # True
```

> **Teaching Tip:**  
> Always specify `encoding="utf-8"`. On Windows, Python defaults to system codepages (like `cp1252`) which causes crashes when encountering emojis or international characters.

---

## 4. File Modes Demystified (`r`, `w`, `a`, `x`)

When calling `open(filename, mode)`:

| Mode | Name | File Exists? | File Missing? | Pointer Position |
| :---: | :--- | :--- | :--- | :--- |
| `'r'` | **Read (Default)** | Reads from start | 💥 **Crashes (`FileNotFoundError`)** | Start (Byte 0) |
| `'w'` | **Write (Truncate)** | ⚠️ **Wipes existing content!** | Creates new file | Start (Byte 0) |
| `'a'` | **Append** | Preserves content; appends at end | Creates new file | End of file |
| `'x'` | **Exclusive Create** | 💥 **Crashes (`FileExistsError`)** | Creates new file | Start (Byte 0) |
| `'r+'`| **Read + Write** | Does not truncate | 💥 **Crashes (`FileNotFoundError`)** | Start (Byte 0) |

### Text Mode vs Binary Mode:
- Default is text mode (`'rt'` or `'wt'`). Characters are strings (`str`).
- Adding `'b'` (e.g. `'rb'`, `'wb'`) opens in binary mode for images, PDFs, audio, or compiled bytecode (`bytes` objects).

---

## 5. The 4 Ways to Read Files in Python

Suppose `fruits.txt` contains:
```
Apple
Banana
Cherry
Date
```

### Technique 1: `f.read()` — Read Entire File or N Characters
```python
with open("fruits.txt", "r") as f:
    content = f.read()       # Entire file as a single str
    print(repr(content))     # 'Apple\nBanana\nCherry\nDate\n'

with open("fruits.txt", "r") as f:
    first_5 = f.read(5)      # Reads first 5 characters: 'Apple'
```
*Best for:* Small configuration files or JSON strings.  
*Worst for:* 10 GB log files (will exhaust your computer's RAM!).

### Technique 2: `f.readline()` — Line-by-Line On Demand
```python
with open("fruits.txt", "r") as f:
    line1 = f.readline()     # 'Apple\n'
    line2 = f.readline()     # 'Banana\n'
```
*Best for:* Reading header lines before iterating the rest.

### Technique 3: `f.readlines()` — List of All Lines
```python
with open("fruits.txt", "r") as f:
    all_lines = f.readlines()  # ['Apple\n', 'Banana\n', 'Cherry\n', 'Date\n']
```
*Best for:* When you need list indexing (e.g. `all_lines[2]`).

### Technique 4 (Industry Standard): Direct Stream Iteration
```python
with open("fruits.txt", "r") as f:
    for line in f:
        print(line.rstrip())  # Strips trailing \n
```
*Why this is the best practice:*  
Python streams the file line-by-line dynamically using a buffer. You can process a 50 GB log file using only a few megabytes of RAM!

---

## 6. Writing & Appending Data (The `\n` Gotcha)

### The Missing Newline Trap:
Unlike `print()`, `file.write()` does **NOT** add a newline `\n`!

```python
# ❌ INCORRECT:
with open("names.txt", "w") as f:
    f.write("Alice")
    f.write("Bob")
# File content: "AliceBob" (jammed together!)

# ✅ CORRECT:
with open("names.txt", "w") as f:
    f.write("Alice\n")
    f.write("Bob\n")
# File content:
# Alice
# Bob
```

### Writing a List of Lines: `f.writelines()`
```python
cities = ["Toronto\n", "Vancouver\n", "Montreal\n"]
with open("cities.txt", "w") as f:
    f.writelines(cities)
```

### The `print(..., file=f)` Shortcut:
```python
with open("output.txt", "w") as f:
    print("User ID:", 1042, "Status: Active", file=f)
    # print automatically converts to string and appends \n!
```

---

## 7. The File Pointer: `tell()` and `seek()`

Python maintains an internal cursor (the file pointer) marking the byte offset where the next read or write occurs:

- `f.tell()`: Returns the integer byte position of the cursor.
- `f.seek(offset)`: Moves the cursor to a specific byte position.

```python
with open("sample.txt", "w+") as f:
    f.write("ABCDEFGHIJ")
    
    print("Current position:", f.tell())  # 10 bytes
    
    # Rewind cursor back to the start (Byte 0)
    f.seek(0)
    print("After seek(0):", f.tell())     # 0 bytes
    
    first_3 = f.read(3)
    print("Read first 3:", first_3)       # 'ABC'
```

---

## 8. Navigating the File System with `os` and `os.path`

Python's built-in `os` and `os.path` modules let you inspect, create, and manage filesystem trees.

### 8.1 Inspection
```python
import os

path = "incoming_logs/auth.log"

print(os.path.exists(path))    # True if file OR directory exists
print(os.path.isfile(path))    # True if it's a regular file
print(os.path.isdir("reports"))# True if it's a directory
print(os.path.getsize(path))   # File size in bytes (e.g. 483)
```

### 8.2 Safe Cross-Platform Path Joining
Never concatenate paths using `+ "/"`:
```python
# ❌ BAD: Breaks on Windows or causes double slashes
full_path = "incoming_logs" + "/" + "auth.log"

# ✅ GOOD: Automatically uses '/' on Mac/Linux and '\' on Windows
full_path = os.path.join("incoming_logs", "subfolder", "auth.log")
```

### 8.3 Splitting Filenames & Extensions
```python
file_name = "data_backup_2026.tar.gz"
base, ext = os.path.splitext(file_name)
print("Base:", base)  # 'data_backup_2026.tar'
print("Ext:", ext)    # '.gz'
```

### 8.4 Directory Operations
```python
# Create nested folders safely
os.makedirs("backups/november/week1", exist_ok=True)

# List all files and subfolders in a directory
entries = os.listdir("incoming_logs")
print("Files:", entries)  # ['auth_service.log', 'api_gateway.log', 'database.log']

# Delete a single file
# os.remove("temp.txt")

# Delete an empty directory
# os.rmdir("temp_dir")
```

---

## 9. Modern File Paths with `pathlib.Path`

Introduced in modern Python 3, `pathlib` represents filesystem paths as objects rather than plain strings:

```python
from pathlib import Path

# Create a Path object pointing to current directory
base = Path(".")

# Build subpaths using the '/' operator!
log_file = base / "incoming_logs" / "auth.log"

# Path attributes
print("File Name:", log_file.name)         # 'auth.log'
print("Stem:", log_file.stem)              # 'auth'
print("Suffix:", log_file.suffix)          # '.log'
print("Parent Folder:", log_file.parent)   # 'incoming_logs'

# Convenient one-liners (handles open & close under the hood):
notes = base / "quick_note.txt"
notes.write_text("Hello from Pathlib!\n", encoding="utf-8")
read_data = notes.read_text(encoding="utf-8")

# Pattern searching (.glob)
for py_file in base.glob("*.py"):
    print("Found Python script:", py_file.name)
```

---

## 10. Defensive Programming & Exception Handling

Filesystem operations depend on external hardware, operating system permissions, and user actions that can fail unpredictably:

```python
target_file = "confidential_database.cfg"

try:
    with open(target_file, mode="r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError as e:
    print(f"⚠️ [Missing File] '{e.filename}' does not exist. Creating default config...")
except PermissionError:
    print("⛔ [Access Denied] You do not have permission to read this file!")
except IsADirectoryError:
    print("📁 [Invalid Target] Expected a file, but found a directory!")
except IOError as io_err:
    print(f"💥 [Disk Error] Input/Output error occurred: {io_err}")
else:
    print("✅ File loaded successfully with zero errors!")
finally:
    print("🔒 File security check completed.")
```

---

## 11. Working with Structured Files (CSV & Delimited Logs)

A frequent real-world task is reading text structured with delimiters (commas `,`, pipes `|`, or tabs `\t`).

### Parsing Pipe-Delimited Server Logs:
```python
log_line = "2026-11-04 10:17:02 | ERROR | api | 500 | DB connection timeout\n"

# 1. Strip trailing newline
clean_line = log_line.strip()

# 2. Split by delimiter
fields = clean_line.split(" | ")
timestamp, level, service, status_code, message = fields

status_code = int(status_code)

print(f"Service '{service}' threw a {level} ({status_code}): {message}")
```

### Parsing CSV Lines:
```python
csv_row = "Server Blade X1,12,1250.00,Hardware"
parts = csv_row.split(",")
item = parts[0]
quantity = int(parts[1])
price = float(parts[2])
total = quantity * price
print(f"{item}: {quantity} units @ ${price:.2f} = ${total:,.2f}")
```

---

## 12. Top 5 Traps & Pitfalls in Python File I/O

| # | Pitfall | Bad Code | The Consequence | The Fix |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Accidental Overwrite** | `open("log.txt", "w")` inside a loop | Wipes the file every iteration; only last line remains | Use mode `"a"` for appending |
| **2** | **Missing Newlines** | `f.write("Entry 1")`<br>`f.write("Entry 2")` | Words are jammed together on one line | `f.write("Entry 1\n")` |
| **3** | **Unstripped `\n` in comparisons** | `if line == "ACTIVE":` | Fails because `"ACTIVE\n" != "ACTIVE"` | `if line.strip() == "ACTIVE":` |
| **4** | **Unchecked File Existence** | `open("missing.txt", "r")` | Program crashes with `FileNotFoundError` | Wrap in `try-except` or check `os.path.exists()` |
| **5** | **Path Concatenation with `+`** | `"dir" + "/" + "file.txt"` | Broken slashes or Windows incompatibility | Use `os.path.join("dir", "file.txt")` |

---

## 13. Classroom Discussion Questions & Live Demos

### Quick Concept Checks (Ask Students):
1. **Question:** "If I run `with open('scores.txt', 'w') as f: pass` on a file that already had 1,000 student grades, what happens?"  
   *Answer:* It immediately wipes the entire file clean (0 bytes)! Mode `'w'` truncates immediately upon opening.
2. **Question:** "What is the difference between `f.readline()` and `f.readlines()`?"  
   *Answer:* `readline()` returns a single string of the next line; `readlines()` returns a list containing all remaining lines as strings.
3. **Question:** "Why should we prefer `for line in f:` over `f.read().splitlines()` for large files?"  
   *Answer:* `for line in f:` streams lines one by one without loading the entire multi-gigabyte file into RAM.

---

## 🛠️ Session 8 Lab & Practice Roadmap

1. Run the concept demo:
   ```bash
   python3 Day-8/concepts_demo.py
   ```
2. Challenge students with the bug hunt:
   ```bash
   python3 Day-8/bug_hunt_day8.py
   ```
3. Complete the warm-up drills:
   ```bash
   python3 Day-8/practice_drills.py
   ```
4. Build the **LogSentinel** cluster log auditor project:
   ```bash
   python3 Day-8/starter_log_sentinel.py
   ```
5. Compare with the reference solution:
   ```bash
   python3 Day-8/solution_log_sentinel.py
   ```

