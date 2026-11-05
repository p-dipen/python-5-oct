# ==============================================================================
# Course: Python Programming
# Session: Day 8 (Chapter 13: Files, File System & Exception Handling)
# Activity: The Bug Hunt — 5 Tricky File System & I/O Coding Bugs
#
# Instructions:
# 1. Read through each challenge below.
# 2. Uncomment the buggy line(s) under "UNCOMMENT TO TEST".
# 3. Run the file: python3 Day-8/bug_hunt_day8.py
# 4. Observe the error message or faulty output.
# 5. Fix the bug so that all 5 challenges produce the expected output!
# ==============================================================================

import os
import shutil

print("=" * 68)
print("     DAY 8 BUG HUNT: 5 FILE SYSTEM & I/O CODING CHALLENGES")
print("=" * 68)

HUNT_DIR = os.path.join(".", "_day8_hunt_scratch")
os.makedirs(HUNT_DIR, exist_ok=True)


# ------------------------------------------------------------------------------
# CHALLENGE 1: The Accidental Overwrite Trap ('w' vs 'a')
# Goal: Record 3 visitor log entries into "visitors.txt".
# Problem: Using mode="w" inside a loop or function resets/truncates the file
#          on every call, leaving only the very last entry!
# Fix: Open the file with append mode ("a") or open it once outside the loop.
# ------------------------------------------------------------------------------
print("\n[Challenge 1: The Accidental Overwrite Trap]")
visitors_log = os.path.join(HUNT_DIR, "visitors.txt")
new_visitors = ["Alice Cooper", "Bob Smith", "Charlie Brown"]

# BUGGY VERSION (Uncomment to test):
# for person in new_visitors:
#     with open(visitors_log, mode="w", encoding="utf-8") as f:
#         f.write(person + "\n")
# with open(visitors_log, "r") as f:
#     print("Buggy Log Content (Only last person saved!):")
#     print(f.read().strip())

# FIXED VERSION:
with open(visitors_log, mode="w", encoding="utf-8") as f:
    f.write("--- Visitor Log ---\n")

for person in new_visitors:
    with open(visitors_log, mode="a", encoding="utf-8") as f:
        f.write(person + "\n")

with open(visitors_log, "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f]
    print(f"Fixed Log Entries ({len(lines)} lines): {lines}")


# ------------------------------------------------------------------------------
# CHALLENGE 2: The Missing Newline Trap in .write()
# Goal: Write 3 server error codes to "errors.log" on separate lines.
# Problem: Unlike print(), file.write() DOES NOT automatically append a newline!
#          Everything gets jammed together on one line ("ERR_401ERR_403ERR_500").
# Fix: Explicitly add "\n" at the end of each string passed to .write().
# ------------------------------------------------------------------------------
print("\n[Challenge 2: The Missing Newline Trap in .write()]")
errors_file = os.path.join(HUNT_DIR, "errors.log")
error_codes = ["ERR_401", "ERR_403", "ERR_500"]

# BUGGY VERSION (Uncomment to test):
# with open(errors_file, "w") as f:
#     for err in error_codes:
#         f.write(err)

# FIXED VERSION:
with open(errors_file, "w", encoding="utf-8") as f:
    for err in error_codes:
        f.write(err + "\n")

with open(errors_file, "r", encoding="utf-8") as f:
    saved_errors = [line.strip() for line in f if line.strip()]
print(f"Fixed Error Lines: {saved_errors}")


# ------------------------------------------------------------------------------
# CHALLENGE 3: Trailing Newline Comparison Trap
# Goal: Scan status codes in a file and count how many say "APPROVED".
# Problem: file.readline() or iterating 'for line in f' retains the trailing
#          newline character '\n'. The comparison `line == "APPROVED"` fails
#          because "APPROVED\n" != "APPROVED"!
# Fix: Strip trailing whitespace with `line.rstrip("\r\n")` or `line.strip()`.
# ------------------------------------------------------------------------------
print("\n[Challenge 3: Trailing Newline Comparison Trap]")
status_file = os.path.join(HUNT_DIR, "statuses.txt")
with open(status_file, "w", encoding="utf-8") as f:
    f.write("APPROVED\nPENDING\nAPPROVED\nREJECTED\nAPPROVED\n")

# BUGGY VERSION (Uncomment to test):
# approved_count = 0
# with open(status_file, "r") as f:
#     for line in f:
#         if line == "APPROVED":  # Bug: line contains '\n'
#             approved_count += 1
# print(f"Buggy Approved Count (shows 0!): {approved_count}")

# FIXED VERSION:
approved_count = 0
with open(status_file, "r", encoding="utf-8") as f:
    for line in f:
        if line.strip() == "APPROVED":
            approved_count += 1
print(f"Fixed Approved Count: {approved_count} (Expected: 3)")


# ------------------------------------------------------------------------------
# CHALLENGE 4: Cross-Platform Path Concatenation Bug
# Goal: Build a path to a file inside a nested subfolder without breaking
#       across Linux, macOS, and Windows.
# Problem: Hardcoding slashes or manual string concatenation like
#          `folder + "/" + file` or `folder + "\\" + file` causes issues
#          with missing/duplicate slashes or OS incompatibilities.
# Fix: Use `os.path.join(folder, subfolder, file)`.
# ------------------------------------------------------------------------------
print("\n[Challenge 4: Cross-Platform Path Concatenation Bug]")
sub_dir = os.path.join(HUNT_DIR, "archive")
os.makedirs(sub_dir, exist_ok=True)
filename = "backup.tar.gz"

# BUGGY VERSION (Uncomment to test):
# buggy_path = HUNT_DIR + "archive" + filename  # Produces '_day8_hunt_scratcharchivebackup.tar.gz'
# print("Buggy joined path:", buggy_path)

# FIXED VERSION:
clean_path = os.path.join(HUNT_DIR, "archive", filename)
print(f"Fixed Joined Path: {clean_path}")
print(f"Parent directory correctly resolved: {os.path.dirname(clean_path)}")


# ------------------------------------------------------------------------------
# CHALLENGE 5: Unhandled FileNotFoundError Crash
# Goal: Read system config from "app_settings.json". If missing, gracefully
#       fallback to default settings instead of crashing the application.
# Problem: Opening a non-existent file without try-except raises a fatal
#          FileNotFoundError that terminates the program abruptly.
# Fix: Wrap the open() block in try-except FileNotFoundError.
# ------------------------------------------------------------------------------
print("\n[Challenge 5: Unhandled FileNotFoundError Crash]")
config_file = os.path.join(HUNT_DIR, "app_settings.json")
default_config = {"app_name": "LogSentinel", "version": "1.0.0", "theme": "dark"}

# BUGGY VERSION (Uncomment to test):
# with open(config_file, "r") as f:  # File does not exist! Crashes with FileNotFoundError
#     config_data = f.read()

# FIXED VERSION:
try:
    with open(config_file, "r", encoding="utf-8") as f:
        loaded_config = f.read()
    print("Config file found and loaded!")
except FileNotFoundError:
    print(f"Notice: '{config_file}' not found. Loading default fallback config.")
    loaded_config = default_config

print(f"Current System Config: {loaded_config}")

# Cleanup
shutil.rmtree(HUNT_DIR, ignore_errors=True)
print("\n" + "=" * 68)
print("           ALL 5 BUG HUNT CHALLENGES RESOLVED!")
print("=" * 68)

