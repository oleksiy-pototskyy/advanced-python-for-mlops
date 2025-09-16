#!/usr/bin/python3
"""
High-Performance File I/O for MLOps
Demonstrates buffered and memory-mapped file operations
for efficient handling of large datasets and model files
"""

# Example 1: Buffered File I/O
# Custom buffer size (8KB) improves performance for large ML datasets
print("=== Buffered File I/O ===")
try:
    with open("data.txt", "r", buffering=8192) as f:
        content = f.read()
        print(f"Read content with 8KB buffer: {len(content)} characters")
except FileNotFoundError:
    print("data.txt not found - buffering controls read/write chunk size")

print("\n" + "="*40 + "\n")

# Example 2: Memory-Mapped Files
# Maps file directly to memory for ultra-fast random access
import mmap

print("=== Memory-Mapped File I/O ===")
try:
    with open("large_file.txt", "r+") as f:
        mm = mmap.mmap(f.fileno(), 0)
        print(mm[0:50])   # read first 50 bytes
        mm.close()
        print("Memory mapping provides instant access to any file position")
except FileNotFoundError:
    print("large_file.txt not found - mmap enables zero-copy file access")






