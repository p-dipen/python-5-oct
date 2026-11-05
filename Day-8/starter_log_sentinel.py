# ==============================================================================
# Course: Python Programming
# Session: Day 8 (Chapter 13: Files, File System & Exception Handling)
# Lab Activity: LogSentinel — Server Cluster Log & File System Auditor
# File: starter_log_sentinel.py (Student Starter Template)
#
# Instructions:
# Complete the 6 TODO sections below to build your server log auditor!
# Follow the docstrings and guided instructions.
# Run this script to test your progress:
#     python3 Day-8/starter_log_sentinel.py
# ==============================================================================

import os
import shutil
import datetime
from file_helpers import (
    ensure_directory,
    format_file_size,
    get_file_metadata,
    safe_read_text,
    safe_write_text,
    scan_directory
)

print("=" * 72)
print("     🛡️  LOGSENTINEL: SERVER CLUSTER LOG & FILE SYSTEM AUDITOR 🛡️")
print("=" * 72)

# Define project directory paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOGS_DIR = os.path.join(BASE_DIR, "incoming_logs")
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
ARCHIVE_DIR = os.path.join(BASE_DIR, "archive")


# ==============================================================================
# STEP 1: INITIALIZE DIRECTORIES & SAMPLE DATA GENERATOR
# ==============================================================================
print("\n[Step 1: Setting Up Directories & Generating Cluster Logs]")

# TODO 1.1: Ensure LOGS_DIR, REPORTS_DIR, and ARCHIVE_DIR all exist using ensure_directory().
# YOUR CODE HERE:
pass


def generate_sample_logs(target_dir):
    """Generates mock server cluster log files if they don't already exist."""
    auth_log = os.path.join(target_dir, "auth_service.log")
    api_log = os.path.join(target_dir, "api_gateway.log")
    db_log = os.path.join(target_dir, "database.log")

    if not os.path.exists(auth_log):
        auth_data = (
            "2026-11-04 10:14:02 | INFO | auth | 200 | User 'alex' logged in successfully from 192.168.1.45\n"
            "2026-11-04 10:15:23 | WARNING | auth | 401 | Failed login attempt for 'admin' from 203.0.113.19\n"
            "2026-11-04 10:15:27 | WARNING | auth | 401 | Failed login attempt for 'admin' from 203.0.113.19\n"
            "2026-11-04 10:15:31 | CRITICAL | auth | 403 | Multiple failed attempts! IP 203.0.113.19 blacklisted\n"
            "2026-11-04 10:18:40 | INFO | auth | 200 | User 'maria' logged in successfully from 192.168.1.88\n"
        )
        safe_write_text(auth_log, auth_data)

    if not os.path.exists(api_log):
        api_data = (
            "2026-11-04 10:16:00 | INFO | api | 200 | GET /api/v1/health status=healthy latency=12ms\n"
            "2026-11-04 10:16:15 | INFO | api | 200 | GET /api/v1/catalog items=45 latency=38ms\n"
            "2026-11-04 10:17:02 | ERROR | api | 500 | POST /api/v1/orders DB connection timeout latency=1250ms\n"
            "2026-11-04 10:17:45 | WARNING | api | 429 | Rate limit exceeded for client_token=tk_9812 latency=4ms\n"
            "2026-11-04 10:19:10 | INFO | api | 200 | GET /api/v1/user/profile latency=24ms\n"
        )
        safe_write_text(api_log, api_data)

    if not os.path.exists(db_log):
        db_data = (
            "2026-11-04 10:12:00 | INFO | db | 200 | Database pool initialized with 20 connections\n"
            "2026-11-04 10:17:01 | ERROR | db | 500 | Deadlock detected on table 'orders' during transaction tx_4021\n"
            "2026-11-04 10:17:03 | CRITICAL | db | 503 | Connection pool exhausted! 0 of 20 available\n"
            "2026-11-04 10:17:30 | INFO | db | 200 | Connection pool auto-recovery completed\n"
        )
        safe_write_text(db_log, db_data)


# Call generator
generate_sample_logs(LOGS_DIR)
print(f"Cluster logs ready in: {LOGS_DIR}")


# ==============================================================================
# STEP 2: DISCOVER & AUDIT INCOMING LOG FILES
# ==============================================================================
print("\n[Step 2: Inspecting Incoming Log Files]")

# TODO 2.1: Scan LOGS_DIR for all files ending with '.log' using scan_directory().
# Store the result in a list called `log_files`.
log_files = []  # YOUR CODE HERE

print(f"Discovered {len(log_files)} log file(s) for audit:")
total_log_bytes = 0

# TODO 2.2: Loop through each log file path in log_files:
#   a) Extract its metadata using get_file_metadata(filepath).
#   b) Accumulate its 'size_bytes' into total_log_bytes.
#   c) Print the filename and human-formatted size (e.g., "auth_service.log (384 B)").
# YOUR CODE HERE


print(f"Total Log Volume: {format_file_size(total_log_bytes)}")


# ==============================================================================
# STEP 3: PARSE LOG STREAMS & COMPUTE SEVERITY METRICS
# ==============================================================================
print("\n[Step 3: Parsing Log Streams & Analyzing Event Severities]")

# Initialize counters and incident tracker
severity_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
security_incidents = []  # Store dict of high-severity events (ERROR and CRITICAL)
total_entries = 0

# TODO 3.1: Iterate through each file in `log_files`.
#   Open each file safely with `with open(filepath, 'r', encoding='utf-8') as f:`.
#   Iterate through each line:
#     - Strip trailing whitespace using .strip().
#     - Skip empty lines.
#     - Split the line by the delimiter " | " into:
#         timestamp, level, service, status_code, message
#     - Increment total_entries by 1.
#     - Increment severity_counts[level] (if level in severity_counts).
#     - If level is "ERROR" or "CRITICAL":
#         Append a dict to `security_incidents`:
#         {"timestamp": timestamp, "service": service, "level": level, "status": status_code, "message": message}
# YOUR CODE HERE


print(f"Processed {total_entries} total log entries.")
print("Severity Breakdown:")
for level, count in severity_counts.items():
    pct = (count / total_entries * 100) if total_entries else 0
    print(f"  - {level:<10}: {count:2d} ({pct:5.1f}%)")


# ==============================================================================
# STEP 4: WRITE EXECUTIVE AUDIT REPORT (TEXT FILE)
# ==============================================================================
print("\n[Step 4: Writing Executive Audit Report]")
report_file = os.path.join(REPORTS_DIR, "audit_summary.txt")

# TODO 4.1: Write a formatted text audit summary to `report_file` using `with open(report_file, 'w')`.
# Include:
#   - Header title with timestamp.
#   - Total files audited and total storage volume.
#   - Total entries processed and severity breakdown.
#   - High severity security incidents listed one by one.
# YOUR CODE HERE


print(f"Executive audit report written to: {report_file}")


# ==============================================================================
# STEP 5: EXPORT SECURITY ALERTS TO CSV
# ==============================================================================
print("\n[Step 5: Exporting High-Severity Alerts to CSV]")
csv_alerts_file = os.path.join(REPORTS_DIR, "security_alerts.csv")

# TODO 5.1: Export all `security_incidents` to `csv_alerts_file` with comma-separated values:
# Header: "Timestamp,Service,Level,StatusCode,Message\n"
# Each row: f"{inc['timestamp']},{inc['service']},{inc['level']},{inc['status']},\"{inc['message']}\"\n"
# YOUR CODE HERE


print(f"Security alerts CSV exported to: {csv_alerts_file}")


# ==============================================================================
# STEP 6: DEFENSIVE ERROR HANDLING (STRETCH GOAL)
# ==============================================================================
print("\n[Step 6: Defensive Missing File Test]")
# TODO 6.1: Wrap an attempt to open a non-existent file "phantom_vault.log"
# in a try-except FileNotFoundError block.
# If caught, print a friendly notice without crashing the script.
# YOUR CODE HERE


print("\n" + "=" * 72)
print("     🎉 LOGSENTINEL AUDIT COMPLETED SUCCESSFULLY!")
print("=" * 72)

