#!/usr/bin/python3
"""
Synchronized Queue for MLOps
Demonstrates thread-safe and process-safe queues for coordinating
ML pipeline tasks between producers and consumers
"""

import threading
import queue
import time
from multiprocessing import Process, Queue

# Example 1: Thread-Safe Queue (threading.queue)
# Ideal for coordinating I/O-bound ML tasks within a single process
print("=== Thread-Safe Queue Example ===")

# Create synchronized queue for thread communication
q = queue.Queue()

def producer():
    """Producer thread - generates ML tasks (e.g., data batches)"""
    for i in range(5):
        print(f"Producing task: {i}")
        q.put(i)  # Thread-safe put operation
        time.sleep(0.5)  # Simulate task generation delay
    print("Producer finished")

def consumer():
    """Consumer thread - processes ML tasks (e.g., model inference)"""
    while True:
        item = q.get()  # Thread-safe get operation (blocks if empty)
        if item is None:  # Poison pill to stop consumer
            break
        print(f"Consuming task: {item}")
        time.sleep(0.3)  # Simulate processing time
        q.task_done()  # Mark task as completed
    print("Consumer finished")

# Start producer and consumer threads
print("Starting producer and consumer threads...")
t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

# Wait for producer to finish, then signal consumer to stop
t1.join()
q.put(None)   # Send poison pill to stop consumer
t2.join()

print("Thread-based queue processing completed")
print("\n" + "="*50 + "\n")

# Example 2: Process-Safe Queue (multiprocessing.Queue)
# Ideal for CPU-intensive ML tasks distributed across multiple processes
print("=== Process-Safe Queue Example ===")

def worker(q):
    """Worker process - handles ML computation tasks"""
    while not q.empty():
        try:
            item = q.get(timeout=1)  # Get with timeout to avoid hanging
            print(f"Process {Process().pid} processing: {item}")
            time.sleep(0.5)  # Simulate CPU-intensive work
        except:
            break  # Queue is empty, exit

if __name__ == "__main__":
    # Create process-safe queue
    q = Queue()
    
    # Fill queue with tasks (e.g., model training parameters)
    print("Adding tasks to process queue...")
    for i in range(5):
        q.put(i)
    
    print(f"Queue size: {q.qsize()}")
    
    # Create worker processes to handle tasks
    processes = [Process(target=worker, args=(q,)) for _ in range(2)]
    
    print("Starting worker processes...")
    for p in processes:
        p.start()
    
    # Wait for all processes to complete
    for p in processes:
        p.join()
    
    print("Process-based queue processing completed")
    
    print("\n=== Queue Benefits in MLOps ===")
    print("- Coordinate data processing pipelines")
    print("- Distribute ML training tasks across workers")
    print("- Buffer between data producers and model consumers")
    print("- Enable scalable batch processing workflows")


