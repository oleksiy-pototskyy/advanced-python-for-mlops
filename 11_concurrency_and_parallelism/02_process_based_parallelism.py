#!/usr/bin/python3
"""
Process-based Parallelism for MLOps
Demonstrates using multiprocessing for CPU-intensive tasks in ML pipelines
such as model training, data preprocessing, or feature engineering
"""

from multiprocessing import Process
import os
import time

# Example: CPU-intensive Computation
# Ideal for ML tasks like model training, feature extraction, or data processing
print("=== Process-based Parallelism Example ===")

def worker(n):
    """Simulate CPU-intensive work (e.g., model training on data chunk)"""
    print(f"Process {os.getpid()} computing square of {n}")
    time.sleep(2)  # simulate heavy computational work
    result = n * n
    print(f"Process {os.getpid()} result: {result}")
    return result

if __name__ == "__main__":
    # Data to process (could represent different model parameters or data chunks)
    numbers = [2, 3, 4, 5]
    
    print(f"Starting parallel processing of {len(numbers)} tasks...")
    print(f"Main process PID: {os.getpid()}")
    
    start_time = time.time()
    processes = []

    # Create and start separate processes for CPU-intensive work
    for num in numbers:
        p = Process(target=worker, args=(num,))
        p.start()  # Start process immediately
        processes.append(p)
        print(f"Started process for number {num}")

    print(f"All {len(processes)} processes started")

    # Wait for all processes to complete
    for p in processes:
        p.join()  # Block until process finishes

    end_time = time.time()
    total_time = end_time - start_time
    
    print("All processes finished")
    print(f"Total time with multiprocessing: {total_time:.1f} seconds")
    print(f"Sequential time would be: {len(numbers) * 2} seconds")
    
    print("\n=== Multiprocessing Benefits in MLOps ===")
    print("- Parallel model training on different data chunks")
    print("- Concurrent hyperparameter optimization")
    print("- Distributed feature engineering")
    print("- Best for CPU-intensive tasks, bypasses Python GIL")


