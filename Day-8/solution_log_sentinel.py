# ==============================================================================
# Course: Python Programming
# Session: Day 8 (Chapter 13: Files, File System & Exception Handling)
# Lab Activity: LogSentinel — Server Cluster Log & File System Auditor
# File: solution_log_sentinel.py (Complete Reference Solution)
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

# Ensure required directories exist
ensure_directory(LOGS_DIR)
ensure_directory(REPORTS_DIR)
ensure_directory(ARCHIVE_DIR)


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


generate_sample_logs(LOGS_DIR)
print(f"Cluster logs verified in: {LOGS_DIR}")


# ==============================================================================
# STEP 2: DISCOVER & AUDIT INCOMING LOG FILES
# ==============================================================================
print("\n[Step 2: Inspecting Incoming Log Files]")

log_files = scan_directory(LOGS_DIR, extension=".log")
print(f"Discovered {len(log_files)} log file(s) for audit:")
total_log_bytes = 0

for filepath in log_files:
    meta = get_file_metadata(filepath)
    if meta:
        total_log_bytes += meta["size_bytes"]
        print(f"  • {meta['name']:<20} | Size: {meta['size_formatted']:>8} | Modified: {meta['modified_at']}")

print(f"Total Log Volume: {format_file_size(total_log_bytes)}")


# ==============================================================================
# STEP 3: PARSE LOG STREAMS & COMPUTE SEVERITY METRICS
# ==============================================================================
print("\n[Step 3: Parsing Log Streams & Analyzing Event Severities]")

severity_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
security_incidents = []
total_entries = 0

for filepath in log_files:
    with open(filepath, mode="r", encoding="utf-8") as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue
            parts = [p.strip() for p in clean_line.split("|")]
            if len(parts) >= 5:
                timestamp = parts[0]
                level = parts[1].upper()
                service = parts[2]
                status_code = parts[3]
                message = parts[4]

                total_entries += 1
                if level in severity_counts:
                    severity_counts[level] += 1
                else:
                    severity_counts[level] = 1

                if level in ("ERROR", "CRITICAL"):
                    security_incidents.append({
                        "timestamp": timestamp,
                        "service": service,
                        "level": level,
                        "status": status_code,
                        "message": message,
                        "source_file": os.path.basename(filepath)
                    })

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
audit_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(report_file, mode="w", encoding="utf-8") as f:
    f.write("====================================================================\n")
    f.write("            LOGSENTINEL: EXECUTIVE CLUSTER AUDIT REPORT            \n")
    f.write("====================================================================\n")
    f.write(f"Generated At:       {audit_timestamp}\n")
    f.write(f"Files Audited:      {len(log_files)} file(s)\n")
    f.write(f"Total Storage:      {format_file_size(total_log_bytes)}\n")
    f.write(f"Total Log Events:   {total_entries}\n\n")

    f.write("--- SEVERITY DISTRIBUTION ---\n")
    for level, count in severity_counts.items():
        pct = (count / total_entries * 100) if total_entries else 0
        bar = "█" * int(pct / 5)
        f.write(f"{level:<10}: {count:2d} ({pct:5.1f}%) | {bar}\n")
    f.write("\n")

    f.write(f"--- HIGH SEVERITY SECURITY INCIDENTS ({len(security_incidents)} DETECTED) ---\n")
    if not security_incidents:
        f.write("No high-severity incidents detected. System healthy.\n")
    else:
        for idx, inc in enumerate(security_incidents, start=1):
            f.write(f"[{idx}] {inc['timestamp']} [{inc['level']}] in service '{inc['service']}' (HTTP {inc['status']})\n")
            f.write(f"    Source:  {inc['source_file']}\n")
            f.write(f"    Message: {inc['message']}\n")
            f.write("\n")

    f.write("--- AUDITOR RECOMMENDATIONS ---\n")
    f.write("1. Investigate IP 203.0.113.19 brute-force login attempts against auth_service.\n")
    f.write("2. Increase database connection pool ceiling above 20 to prevent transaction deadlock timeouts.\n")
    f.write("====================================================================\n")

print(f"Executive audit report written successfully to:\n  -> {report_file}")


# ==============================================================================
# STEP 5: EXPORT SECURITY ALERTS TO CSV
# ==============================================================================
print("\n[Step 5: Exporting High-Severity Alerts to CSV]")
csv_alerts_file = os.path.join(REPORTS_DIR, "security_alerts.csv")

with open(csv_alerts_file, mode="w", encoding="utf-8") as f:
    # Write CSV Header
    f.write("Timestamp,Service,Level,StatusCode,SourceFile,Message\n")
    for inc in security_incidents:
        # Wrap message in quotes to escape potential commas
        safe_msg = inc['message'].replace('"', '""')
        row = f"{inc['timestamp']},{inc['service']},{inc['level']},{inc['status']},{inc['source_file']},\"{safe_msg}\"\n"
        f.write(row)

print(f"Security alerts CSV exported successfully to:\n  -> {csv_alerts_file}")


# ==============================================================================
# STEP 6: DEFENSIVE ERROR HANDLING TEST
# ==============================================================================
print("\n[Step 6: Defensive Missing File Test]")
missing_test_file = os.path.join(LOGS_DIR, "phantom_service.log")

try:
    with open(missing_test_file, mode="r", encoding="utf-8") as f:
        _ = f.read()
except FileNotFoundError as err:
    print(f"  [Handled Gracefully] Expected file check: '{err.filename}' is absent. No crash.")


# ==============================================================================
# STEP 7: LOG ROTATION & ARCHIVAL
# ==============================================================================
print("\n[Step 7: Log Archival & Backup]")
timestamp_tag = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
archive_session_dir = os.path.join(ARCHIVE_DIR, f"audit_{timestamp_tag}")
ensure_directory(archive_session_dir)

for filepath in log_files:
    fname = os.path.basename(filepath)
    dest_path = os.path.join(archive_session_dir, fname)
    shutil.copy2(filepath, dest_path)

print(f"Archived {len(log_files)} file(s) into: {archive_session_dir}")

print("\n" + "=" * 72)
print("     🎉 LOGSENTINEL AUDIT ENGINE EXECUTED SUCCESSFULLY!")
print("=" * 72)

