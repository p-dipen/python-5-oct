# ==============================================================================
# Course: Python Programming
# Session: Day 8 (Chapter 13: Files, File System & Exception Handling)
# Activity: Quick Practice Drills — 3 Rapid Warm-up Exercises
#
# Instructions:
# Practice these 3 short coding drills to master:
#   - Drill 1: Safe File Journaling & Line Traversal (with open, append, read)
#   - Drill 2: Directory Inspector & Storage Auditor (os.listdir, os.path.getsize)
#   - Drill 3: Structured Server Log Aggregator (parsing fields, metrics calculation)
# ==============================================================================

import os
import shutil
import datetime

print("=" * 68)
print("             DAY 8: 3 QUICK PRACTICE DRILLS")
print("=" * 68)

DRILL_DIR = os.path.join(".", "_day8_drills_scratch")
os.makedirs(DRILL_DIR, exist_ok=True)


# ------------------------------------------------------------------------------
# DRILL 1: Safe File Journaling & Line Traversal (Liang 13.2)
# Goal:
#   1. Open a new file "dev_journal.txt" in write mode ('w') and write a header.
#   2. Append 3 timestamped journal notes using append mode ('a').
#   3. Read the file line-by-line and print each line formatted with line numbers.
# ------------------------------------------------------------------------------
print("\n--- Drill 1: Developer Journal with Timestamps ---")
journal_file = os.path.join(DRILL_DIR, "dev_journal.txt")

# Step 1: Write header
with open(journal_file, "w", encoding="utf-8") as f:
    f.write("=== DEVELOPER ACTIVITY LOG ===\n")

# Step 2: Append notes
notes = [
    "Configured local PostgreSQL database instance.",
    "Patched security vulnerability in authentication token handler.",
    "Executed automated integration test suite with 100% pass rate."
]

for note in notes:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(journal_file, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {note}\n")

# Step 3: Read back and display
print(f"Reading back '{journal_file}':")
with open(journal_file, "r", encoding="utf-8") as f:
    for idx, line in enumerate(f, start=1):
        print(f"  Line {idx}: {line.rstrip()}")


# ------------------------------------------------------------------------------
# DRILL 2: Directory Inspector & Storage Auditor (Liang 13.4)
# Goal:
#   1. Populate a folder with several sample files of various extensions and sizes.
#   2. Inspect the folder using os.listdir() and os.path.
#   3. Print a formatted table showing: File Name, Extension, and Size in Bytes.
#   4. Compute and print the total directory size in bytes.
# ------------------------------------------------------------------------------
print("\n--- Drill 2: Directory Inspector & Storage Auditor ---")
audit_dir = os.path.join(DRILL_DIR, "storage_vault")
os.makedirs(audit_dir, exist_ok=True)

# Create mock files
mock_files = {
    "system_config.json": '{"env": "production", "debug": false}',
    "readme.md": "# Storage Vault\nContains sensitive cluster assets.\n",
    "backup_dump.sql": "-- SQL DUMP\nCREATE TABLE logs (id INT, msg TEXT);\n" * 10,
    "changelog.txt": "v1.0.0 Initial release.\nv1.0.1 Bug fixes.\n"
}

for fname, content in mock_files.items():
    fpath = os.path.join(audit_dir, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)

# Inspect files
total_size = 0
print(f"{'File Name':<22} | {'Extension':<10} | {'Size (Bytes)':>12}")
print("-" * 50)

for filename in sorted(os.listdir(audit_dir)):
    full_path = os.path.join(audit_dir, filename)
    if os.path.isfile(full_path):
        size = os.path.getsize(full_path)
        total_size += size
        _, ext = os.path.splitext(filename)
        print(f"{filename:<22} | {ext:<10} | {size:>12} B")

print("-" * 50)
print(f"Total Vault Storage: {total_size} Bytes across {len(mock_files)} files.")


# ------------------------------------------------------------------------------
# DRILL 3: Structured Server Log Aggregator (Liang 13.2 & 13.5)
# Goal:
#   1. Create a simulated server log file "access.log".
#   2. Parse each record (fields separated by " | "):
#      Timestamp | HTTP Method & Path | HTTP Status Code | Latency (ms)
#   3. Calculate:
#      - Total requests
#      - Success count (HTTP 200) vs Error count (4xx, 5xx)
#      - Average response latency
# ------------------------------------------------------------------------------
print("\n--- Drill 3: Server Log Aggregator & Health Metrics ---")
log_path = os.path.join(DRILL_DIR, "access.log")

raw_log_entries = [
    "2026-11-04 14:00:01 | GET /api/v1/health | 200 | 15ms\n",
    "2026-11-04 14:00:05 | POST /api/v1/login | 200 | 145ms\n",
    "2026-11-04 14:00:12 | GET /api/v1/user/99 | 404 | 22ms\n",
    "2026-11-04 14:00:18 | POST /api/v1/checkout | 500 | 850ms\n",
    "2026-11-04 14:00:25 | GET /api/v1/products | 200 | 65ms\n",
    "2026-11-04 14:00:30 | POST /api/v1/admin | 403 | 110ms\n"
]

with open(log_path, "w", encoding="utf-8") as f:
    f.writelines(raw_log_entries)

total_reqs = 0
success_reqs = 0
error_reqs = 0
total_latency = 0

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(" | ")
        timestamp, endpoint, status_str, latency_str = parts
        status_code = int(status_str)
        latency_ms = int(latency_str.replace("ms", ""))

        total_reqs += 1
        total_latency += latency_ms
        if status_code == 200:
            success_reqs += 1
        else:
            error_reqs += 1

avg_latency = total_latency / total_reqs if total_reqs else 0.0

print(f"Total Requests:       {total_reqs}")
print(f"Successful (200 OK):  {success_reqs} ({(success_reqs/total_reqs)*100:.1f}%)")
print(f"Errors (4xx / 5xx):   {error_reqs} ({(error_reqs/total_reqs)*100:.1f}%)")
print(f"Average Latency:      {avg_latency:.2f} ms")

# Cleanup scratch
shutil.rmtree(DRILL_DIR, ignore_errors=True)
print("\n" + "=" * 68)
print("             ALL 3 DRILLS EXECUTED SUCCESSFULLY!")
print("=" * 68)

