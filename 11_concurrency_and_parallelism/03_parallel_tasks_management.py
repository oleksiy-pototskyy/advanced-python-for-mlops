#!/usr/bin/python3
"""
Parallel Tasks Management for MLOps
Demonstrates using concurrent.futures for managing parallel ML tasks
with result collection and error handling
"""

from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import os

# Example: Managed Parallel Task Execution
# High-level interface for ML workload distribution and result collection
print("=== Parallel Tasks Management Example ===")

def compute_square(n):
    """Simulate CPU-intensive ML task (e.g., model training on data chunk)"""
    print(f"Process {os.getpid()} working on {n}")
    time.sleep(2)  # simulate heavy computational task
    result = n * n
    print(f"Process {os.getpid()} completed: {n}² = {result}")
    return result

if __name__ == "__main__":
    # Tasks to process (could represent different model configurations)
    numbers = [1, 2, 3, 4, 5]
    
    print(f"Managing parallel execution of {len(numbers)} tasks...")
    print(f"Main process PID: {os.getpid()}")
    
    start_time = time.time()
    
    # Use ProcessPoolExecutor for automatic process management
    with ProcessPoolExecutor() as executor:
        print(f"Process pool created with {executor._max_workers} workers")
        
        # Submit all tasks to the executor
        futures = [executor.submit(compute_square, num) for num in numbers]
        print(f"Submitted {len(futures)} tasks to process pool")

        # Collect results as they complete (not necessarily in order)
        results = []
        for future in as_completed(futures):
            try:
                result = future.result()  # Get result from completed task
                results.append(result)
                print(f"Collected result: {result}")
            except Exception as e:
                print(f"Task failed with error: {e}")
    
    end_time = time.time()
    total_time = end_time - start_time
    
    print(f"\nAll tasks completed. Results: {sorted(results)}")
    print(f"Total time with ProcessPoolExecutor: {total_time:.1f} seconds")
    print(f"Sequential time would be: {len(numbers) * 2} seconds")
    
    print("\n=== ProcessPoolExecutor Benefits in MLOps ===")
    print("- Automatic process lifecycle management")
    print("- Built-in result collection and error handling")
    print("- Optimal for batch ML training jobs")
    print("- Cleaner code compared to manual process management")


