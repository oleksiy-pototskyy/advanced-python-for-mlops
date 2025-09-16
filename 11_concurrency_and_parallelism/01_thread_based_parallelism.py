#!/usr/bin/python3
"""
Thread-based Parallelism for MLOps
Demonstrates using threading for I/O-bound tasks in ML pipelines
such as downloading datasets, model files, or API calls
"""

import threading
import time

# Example: Concurrent File Downloads
# Common in MLOps for downloading datasets, models, or artifacts
print("=== Thread-based Parallelism Example ===")

def download_file(name, seconds):
    """Simulate downloading a file (I/O-bound operation)"""
    print(f"Start downloading {name}")
    time.sleep(seconds)  # simulate slow network
    print(f"Finished downloading {name}")

# List of files with their "download time" (simulating different file sizes)
tasks = [("file1", 3), ("file2", 2), ("file3", 4)]

print(f"Starting concurrent download of {len(tasks)} files...")
start_time = time.time()

# Create and start threads for concurrent downloads
threads = []
for name, sec in tasks:
    # Create thread for each download task
    t = threading.Thread(target=download_file, args=(name, sec))
    t.start()  # Start thread immediately
    threads.append(t)

print(f"All {len(threads)} threads started")

# Wait for all threads to finish
for t in threads:
    t.join()  # Block until thread completes

end_time = time.time()
total_time = end_time - start_time

print("All downloads finished")
print(f"Total time with threading: {total_time:.1f} seconds")
print(f"Sequential time would be: {sum(sec for _, sec in tasks)} seconds")

print("\n=== Threading Benefits in MLOps ===")
print("- Concurrent data downloads from multiple sources")
print("- Parallel API calls for model inference")
print("- Simultaneous file processing operations")
print("- Best for I/O-bound tasks, not CPU-intensive work")



