#!/usr/bin/python3
"""
Advanced Serialization for MLOps
Demonstrates efficient serialization formats for ML data:
Parquet for structured data and HDF5 for numerical arrays
"""

import pandas as pd
import h5py
import numpy as np

# Example 1: Parquet Format
# Columnar storage format ideal for ML datasets and analytics
print("=== Parquet Serialization ===")
df = pd.DataFrame({"id": [1, 2, 3], "score": [0.95, 0.89, 0.76]})
print("Original DataFrame:")
print(df)

# Save to Parquet (compressed, efficient for large datasets)
df.to_parquet("results.parquet")
print("\nSaved to results.parquet (columnar format)")

# Load from Parquet
loaded = pd.read_parquet("results.parquet")
print("\nLoaded from Parquet:")
print(loaded)

print("\n" + "="*50 + "\n")



# Example 2: HDF5 Format
# Hierarchical format excellent for large numerical datasets
print("=== HDF5 Serialization ===")

# Create sample ML data (model scores)
scores_array = np.array([0.95, 0.89, 0.76])
print(f"Original array: {scores_array}")

# Save to HDF5 (supports compression and chunking)
with h5py.File("data.h5", "w") as f:
    f.create_dataset("scores", data=scores_array)
    print("\nSaved to data.h5 (hierarchical format)")

# Load from HDF5
with h5py.File("data.h5", "r") as f:
    loaded_scores = f["scores"][:]
    print(f"\nLoaded from HDF5: {loaded_scores}")

print("\n=== Format Comparison ===")
print("Parquet: Best for structured/tabular ML data")
print("HDF5: Best for large numerical arrays and matrices")




