# ==============================================================================
# Course: Python Programming
# Session: Day 8 (Chapter 13: Files, File System & Exception Handling)
# Textbook Reference: Liang, Chapter 13 (Files and Exception Handling)
#
# Topics Covered:
#   - Part 1: Opening Files, Modes ('r', 'w', 'a', 'x') & the `with` Statement
#   - Part 2: Writing & Appending Data (write, writelines, print to file)
#   - Part 3: Reading Techniques (read, readline, readlines, direct iteration)
#   - Part 4: File Pointer Position (tell, seek)
#   - Part 5: File System & Paths via `os` & `os.path` (exists, join, getsize, listdir)
#   - Part 6: Modern Object-Oriented File Paths via `pathlib.Path`
#   - Part 7: Defensive Programming & File Exception Handling (FileNotFoundError, etc.)
#   - Part 8: Structured Data Parsing (CSV & delimited log lines)
# ==============================================================================

import os
import shutil
from pathlib import Path

print("=" * 76)
print("     DAY 8: MASTERING FILE SYSTEM & FILE I/O IN PYTHON")
print("=" * 76)

DEMO_DIR = os.path.join(".", "_day8_demo_sandbox")
os.makedirs(DEMO_DIR, exist_ok=True)


# ==============================================================================
# PART 1: OPENING FILES, MODES & THE CONTEXT MANAGER (Liang 13.1 - 13.2)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 1: OPENING FILES & THE WITH STATEMENT")
print("=" * 55)

sample_file_1 = os.path.join(DEMO_DIR, "demo_hello.txt")

# Traditional approach (Must manually close, risks leaking if an error occurs):
# f = open(sample_file_1, "w")
# f.write("Hello World\n")
# f.close()

# Pythonic approach: Using the 'with' statement (Context Manager)
# Guarantees the file is closed automatically as soon as the block exits!
with open(sample_file_1, mode="w", encoding="utf-8") as f:
    f.write("Welcome to Day 8 File Systems!\n")
    f.write("Line 2: Python makes file management simple.\n")

print(f"[1.1] File created safely using 'with open(...)': {sample_file_1}")
print(f"[1.2] Is the file handle closed outside the block? {f.closed}")


# ==============================================================================
# PART 2: FILE ACCESS MODES & WRITING DATA (Liang 13.2)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 2: FILE ACCESS MODES & WRITING DATA")
print("=" * 55)

# Mode 'w': Overwrites / truncates existing file or creates new file
with open(sample_file_1, mode="w", encoding="utf-8") as f:
    f.write("Header: System Initialized\n")

# Mode 'a': Appends to the end of the file without deleting existing content
with open(sample_file_1, mode="a", encoding="utf-8") as f:
    f.write("Log Event 001: User Alice logged in.\n")
    f.write("Log Event 002: User Bob requested report.\n")

# Writing multiple lines at once: writelines()
extra_lines = [
    "Log Event 003: Database backup started.\n",
    "Log Event 004: Backup completed in 1.4s.\n"
]
with open(sample_file_1, mode="a", encoding="utf-8") as f:
    f.writelines(extra_lines)

# You can also redirect Python's print() function directly to a file:
with open(sample_file_1, mode="a", encoding="utf-8") as f:
    print("Log Event 005: Sensor check passed (printed via print()).", file=f)

print("[2.1] Appended multiple lines using .write(), .writelines(), and print(..., file=f).")


# ==============================================================================
# PART 3: READING TECHNIQUES (Liang 13.2)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 3: FOUR READING TECHNIQUES")
print("=" * 55)

# Technique 1: read() — Reads the entire file into a single string (or n characters)
with open(sample_file_1, mode="r", encoding="utf-8") as f:
    full_text = f.read()
print(f"[3.1] .read() read {len(full_text)} characters total.")

# Technique 2: readline() — Reads one line at a time
with open(sample_file_1, mode="r", encoding="utf-8") as f:
    first_line = f.readline().rstrip("\r\n")
    second_line = f.readline().rstrip("\r\n")
print(f"[3.2] .readline() Line 1: '{first_line}'")
print(f"[3.2] .readline() Line 2: '{second_line}'")

# Technique 3: readlines() — Reads all lines into a list of strings
with open(sample_file_1, mode="r", encoding="utf-8") as f:
    all_lines_list = f.readlines()
print(f"[3.3] .readlines() returned list of {len(all_lines_list)} lines.")

# Technique 4 (BEST PRACTICE): Direct iteration over the file object (Memory efficient!)
print("[3.4] Direct iteration ('for line in f'):")
with open(sample_file_1, mode="r", encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        clean_line = line.rstrip("\r\n")
        print(f"      [{line_num:02d}] {clean_line}")


# ==============================================================================
# PART 4: FILE POINTER POSITION & SEEKING (Liang 13.2)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 4: FILE POINTER POSITION & SEEKING")
print("=" * 55)

with open(sample_file_1, mode="r", encoding="utf-8") as f:
    print(f"[4.1] Initial pointer position: {f.tell()} bytes")
    header = f.readline()
    print(f"[4.2] After reading header ({len(header)} chars), position: {f.tell()} bytes")
    # Rewind pointer back to start
    f.seek(0)
    print(f"[4.3] After f.seek(0), pointer position: {f.tell()} bytes")
    re_read_header = f.readline().rstrip("\r\n")
    print(f"[4.4] Re-read header: '{re_read_header}'")


# ==============================================================================
# PART 5: FILE SYSTEM OPERATIONS WITH `os` & `os.path` (Liang 13.4)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 5: FILE SYSTEM OPERATIONS WITH `os` & `os.path`")
print("=" * 55)

# 5.1 Checking existence and file types
print(f"[5.1] os.path.exists: {os.path.exists(sample_file_1)}")
print(f"[5.1] os.path.isfile: {os.path.isfile(sample_file_1)}")
print(f"[5.1] os.path.isdir:  {os.path.isdir(DEMO_DIR)}")

# 5.2 Safe path concatenation (Cross-platform compatibility)
subfolder = os.path.join(DEMO_DIR, "logs_subfolder")
os.makedirs(subfolder, exist_ok=True)
sub_file = os.path.join(subfolder, "sub_log.txt")
with open(sub_file, "w") as f:
    f.write("Subfolder file.\n")

print(f"[5.2] Cross-platform path: {sub_file}")

# 5.3 Splitting paths and finding extensions
dir_name, base_name = os.path.split(sub_file)
stem, ext = os.path.splitext(base_name)
print(f"[5.3] Directory: '{dir_name}' | Basename: '{base_name}' | Stem: '{stem}' | Ext: '{ext}'")

# 5.4 File size in bytes
file_size = os.path.getsize(sample_file_1)
print(f"[5.4] File size of demo_hello.txt: {file_size} bytes")

# 5.5 Listing directory contents
entries = os.listdir(DEMO_DIR)
print(f"[5.5] Contents of '{DEMO_DIR}': {entries}")


# ==============================================================================
# PART 6: MODERN PATH HANDLING WITH `pathlib.Path`
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 6: MODERN PATH HANDLING WITH `pathlib`")
print("=" * 55)

demo_path = Path(DEMO_DIR)
p_file = demo_path / "notes.txt"   # Uses the '/' slash operator!

# Quick one-liner write and read
p_file.write_text("Note: Pathlib provides object-oriented paths!\n", encoding="utf-8")
content = p_file.read_text(encoding="utf-8")

print(f"[6.1] Written and read using Path: '{content.strip()}'")
print(f"[6.2] Path details -> Name: {p_file.name}, Suffix: {p_file.suffix}, Parent: {p_file.parent}")

# Pattern matching with .glob()
txt_files = list(demo_path.glob("*.txt"))
print(f"[6.3] Matching *.txt files in demo dir: {[p.name for p in txt_files]}")


# ==============================================================================
# PART 7: DEFENSIVE FILE I/O & EXCEPTION HANDLING (Liang 13.3)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 7: EXCEPTION HANDLING WITH FILE I/O")
print("=" * 55)

missing_path = os.path.join(DEMO_DIR, "non_existent_file.json")

print("[7.1] Attempting to open a missing file with try-except:")
try:
    with open(missing_path, "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError as err:
    print(f"      Caught Expected Exception: FileNotFoundError -> {err.filename} not found!")
except PermissionError:
    print("      Caught PermissionError: Access Denied!")
except Exception as unexpected:
    print(f"      Unexpected error: {unexpected}")
else:
    print("      File read successfully with no exceptions!")
finally:
    print("      Finally block: Always executes (cleanup / logging).")


# ==============================================================================
# PART 8: STRUCTURED DATA & CSV PARSING (Liang 13.5)
# ==============================================================================
print("\n" + "=" * 55)
print(">>> PART 8: PARSING STRUCTURED TEXT (CSV / LOG DATA)")
print("=" * 55)

csv_path = os.path.join(DEMO_DIR, "inventory.csv")

# Create a sample CSV file
with open(csv_path, "w", encoding="utf-8") as f:
    f.write("Item,Quantity,Unit_Price,Category\n")
    f.write("Server Blade X1,12,1250.00,Hardware\n")
    f.write("Ethernet Switch 48P,5,450.50,Networking\n")
    f.write("UPS Battery 1500VA,8,220.00,Power\n")
    f.write("Cat6 Cable Spool,20,85.25,Networking\n")

print(f"[8.1] Created sample CSV inventory at: {csv_path}")

# Read and parse CSV manually line by line
print("\n[8.2] Parsing CSV Records and Computing Inventory Value:")
total_inventory_value = 0.0

with open(csv_path, "r", encoding="utf-8") as f:
    # Read the header line first
    header_line = f.readline().rstrip("\r\n")
    headers = header_line.split(",")
    print(f"      Headers: {headers}")

    # Process data rows
    for row_idx, line in enumerate(f, start=1):
        line = line.rstrip("\r\n")
        if not line:
            continue
        parts = line.split(",")
        item = parts[0]
        qty = int(parts[1])
        unit_price = float(parts[2])
        category = parts[3]

        item_total = qty * unit_price
        total_inventory_value += item_total
        print(f"      Row {row_idx}: {item:<22} | Qty: {qty:2d} | Unit: ${unit_price:7.2f} | Total: ${item_total:8.2f}")

print(f"\n      TOTAL INVENTORY VALUATION: ${total_inventory_value:,.2f}")

# Cleanup demo sandbox directory
shutil.rmtree(DEMO_DIR, ignore_errors=True)
print("\n[Cleanup] Demo sandbox directory safely removed.")
print("=" * 76)
print("           CONCEPTS DEMO COMPLETED SUCCESSFULLY!")
print("=" * 76)

