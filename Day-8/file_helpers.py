# ==============================================================================
# Course: Python Programming
# Session: Day 8 (Chapter 13: Files, File System & Exception Handling)
# Module: file_helpers.py — Reusable File System Utility Library
#
# Purpose:
# Provides modular, robust helper functions for directory inspection,
# file reading/writing, cross-platform path handling, and file metadata extraction.
# ==============================================================================

import os
import shutil
import datetime


def ensure_directory(dir_path):
    """
    Ensures that a directory exists; creates it if it does not.
    
    Args:
        dir_path (str): Path to the target directory.
        
    Returns:
        str: Absolute path of the ensured directory.
    """
    os.makedirs(dir_path, exist_ok=True)
    return os.path.abspath(dir_path)


def format_file_size(size_in_bytes):
    """
    Converts a byte count into a human-readable string (B, KB, MB, GB).
    
    Args:
        size_in_bytes (int): Size in bytes.
        
    Returns:
        str: Human-readable file size with units (e.g., '14.25 KB').
    """
    if size_in_bytes < 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_idx = 0
    size = float(size_in_bytes)
    while size >= 1024.0 and unit_idx < len(units) - 1:
        size /= 1024.0
        unit_idx += 1
    return f"{size:.2f} {units[unit_idx]}" if unit_idx > 0 else f"{int(size)} B"


def get_file_metadata(file_path):
    """
    Retrieves key file metadata safely without raising uncaught exceptions.
    
    Args:
        file_path (str): Path to the file.
        
    Returns:
        dict: Metadata dictionary containing existence, size, extension, and timestamp,
              or None if the file does not exist.
    """
    if not os.path.exists(file_path):
        return None

    stat_info = os.stat(file_path)
    base_name = os.path.basename(file_path)
    stem, extension = os.path.splitext(base_name)
    mod_time = datetime.datetime.fromtimestamp(stat_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "path": os.path.abspath(file_path),
        "name": base_name,
        "stem": stem,
        "extension": extension.lower(),
        "is_file": os.path.isfile(file_path),
        "is_dir": os.path.isdir(file_path),
        "size_bytes": stat_info.st_size,
        "size_formatted": format_file_size(stat_info.st_size),
        "modified_at": mod_time
    }


def safe_read_text(file_path, default=""):
    """
    Reads all text content from a file safely, returning a default value if missing.
    
    Args:
        file_path (str): Path to the file to read.
        default (str): Fallback string returned if the file is not found or unreadable.
        
    Returns:
        str: The file's text contents or the fallback default.
    """
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            return f.read()
    except (FileNotFoundError, PermissionError, IOError) as err:
        print(f"[Warning] Unable to read '{file_path}': {err}")
        return default


def safe_write_text(file_path, content, append=False):
    """
    Writes or appends text to a file safely, auto-creating parent directories.
    
    Args:
        file_path (str): Target file path.
        content (str): Text content to write.
        append (bool): If True, appends ('a'); if False, overwrites ('w').
        
    Returns:
        bool: True if writing succeeded, False otherwise.
    """
    try:
        parent_dir = os.path.dirname(file_path)
        if parent_dir:
            ensure_directory(parent_dir)
        mode = "a" if append else "w"
        with open(file_path, mode=mode, encoding="utf-8") as f:
            f.write(content)
        return True
    except (PermissionError, IOError) as err:
        print(f"[Error] Failed to write to '{file_path}': {err}")
        return False


def scan_directory(dir_path, extension=None):
    """
    Scans a directory and returns sorted paths of matching files.
    
    Args:
        dir_path (str): Directory to scan.
        extension (str, optional): Filter by file extension (e.g., '.log' or 'txt').
        
    Returns:
        list of str: List of matching full file paths.
    """
    if not os.path.isdir(dir_path):
        return []

    if extension and not extension.startswith("."):
        extension = "." + extension

    matches = []
    for entry in sorted(os.listdir(dir_path)):
        full_path = os.path.join(dir_path, entry)
        if os.path.isfile(full_path):
            if extension is None or entry.lower().endswith(extension.lower()):
                matches.append(full_path)
    return matches


# Self-test block when executed directly
if __name__ == "__main__":
    print("=" * 68)
    print("           TESTING FILE_HELPERS UTILITY LIBRARY")
    print("=" * 68)

    test_dir = os.path.join(".", "_test_scratch_helpers")
    ensure_directory(test_dir)
    print(f"1. Ensured directory: {test_dir}")

    test_file = os.path.join(test_dir, "sample.txt")
    write_ok = safe_write_text(test_file, "Line 1: Hello File System!\nLine 2: Python 3 I/O.\n")
    print(f"2. Written successfully: {write_ok}")

    meta = get_file_metadata(test_file)
    print("3. Metadata extracted:")
    for k, v in meta.items():
        print(f"   - {k}: {v}")

    read_back = safe_read_text(test_file)
    print(f"4. Content read back ({len(read_back)} chars):\n{read_back.strip()}")

    dir_files = scan_directory(test_dir)
    print(f"5. Scanned files in dir: {dir_files}")

    # Clean up test artifact
    shutil.rmtree(test_dir, ignore_errors=True)
    print("6. Cleaned up scratch directory successfully!")

