#!/usr/bin/python3
"""
Inheritance in Python for MLOps
Demonstrates how inheritance enables code reuse and polymorphism
in machine learning data processing pipelines
"""

# Base class - defines common interface for all datasets
class Dataset:
    """Base class for all dataset types in ML pipeline"""
    
    def __init__(self, path):
        self.path = path

    def load(self):
        """Default loading behavior - can be overridden by subclasses"""
        print(f"Loading data from {self.path}")


# Example 1: Simple Inheritance - Adding Specific Functionality
class CSVDataset(Dataset):
    """CSV-specific dataset that inherits from Dataset"""
    
    def parse(self):
        """CSV-specific parsing method"""
        print("Parsing CSV file")


print("=== Example 1: Simple Inheritance ===")
data = CSVDataset("train.csv")
data.load()   # inherited from Dataset
data.parse()  # defined in CSVDataset

print("\n" + "="*50 + "\n")

# Example 2: Method Overriding - Changing Parent Behavior
class JSONDataset(Dataset):
    """JSON dataset with overridden load method"""
    
    def load(self):
        """Override parent's load method for JSON-specific behavior"""
        print(f"Reading JSON file from {self.path}")


print("=== Example 2: Method Overriding ===")
json_data = JSONDataset("config.json")
json_data.load()  # uses overridden method

print("\n" + "="*50 + "\n")

# Example 3: Using super() - Extending Parent Behavior
class ValidatedDataset(Dataset):
    """Dataset with validation that extends parent's load method"""
    
    def load(self):
        """Add validation before calling parent's load method"""
        print("Checking file before loading...")
        super().load()  # call parent's load method


print("=== Example 3: Extending with super() ===")
validated_data = ValidatedDataset("validated_train.csv")
validated_data.load()  # validation + parent's load





