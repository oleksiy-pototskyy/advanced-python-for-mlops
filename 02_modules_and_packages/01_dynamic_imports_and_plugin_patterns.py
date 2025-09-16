#!/usr/bin/python3
"""
Dynamic Imports and Plugin Patterns for MLOps
Demonstrates how to dynamically load modules and implement plugin architectures
commonly used in ML pipelines for flexibility and extensibility
"""

import importlib

# Example 1: Basic Dynamic Import
# Useful when module names are determined at runtime
print("=== Example 1: Basic Dynamic Import ===")
module_name = "math"
math_module = importlib.import_module(module_name)
print(f"Dynamic import of '{module_name}': sqrt(16) = {math_module.sqrt(16)}")

print("\n" + "="*50 + "\n")

# Example 2: Cloud Provider Abstraction
# Common pattern in MLOps for switching between cloud providers
print("=== Example 2: Cloud Provider Selection ===")
provider = "boto3"  # Could be "google.cloud.storage" or "azure.storage.blob"
try:
    sdk = importlib.import_module(provider)
    print(f"Successfully loaded cloud SDK: {provider}")
except ImportError:
    print(f"Cloud SDK '{provider}' not available - install with: pip install {provider}")

print("\n" + "="*50 + "\n")

# Example 3: Plugin Pattern for ML Metrics
# Allows dynamic loading of different evaluation metrics
print("=== Example 3: ML Metrics Plugin System ===")
metrics = ["accuracy", "f1score"]

# Sample predictions for demonstration
y_true = [1, 0, 1]
y_pred = [1, 1, 1]

for metric in metrics:
    try:
        plugin = importlib.import_module(f"plugins.{metric}")
        result = plugin.run(y_true, y_pred)
        print(f"{metric}: {result:.3f}")
    except (ImportError, AttributeError) as e:
        print(f"Failed to load {metric} plugin: {e}")




