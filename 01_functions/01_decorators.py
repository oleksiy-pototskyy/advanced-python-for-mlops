#!/usr/bin/python3
"""
Decorators in Python for MLOps
Demonstrates common decorator patterns used in machine learning workflows
"""

import time

# Example 1: Basic Logging Decorator
# Useful for tracking function execution in ML pipelines
def log_decorator(func):
    """Decorator that logs function start and completion"""
    def wrapper(*args, **kwargs):
        print(f"Starting {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper


@log_decorator
def train_model():
    """Simulates model training process"""
    print("Training...")


# Execute the decorated function
train_model()

print("\n" + "="*50 + "\n")

# Example 2: Timing Decorator
# Essential for performance monitoring in ML workflows
def timing_decorator(func):
    """Decorator that measures and reports function execution time"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper


@timing_decorator
def load_data():
    """Simulates data loading with artificial delay"""
    time.sleep(2)


# Execute the timed function
load_data()




