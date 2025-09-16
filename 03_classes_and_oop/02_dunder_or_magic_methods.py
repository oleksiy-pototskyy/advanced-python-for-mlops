#!/usr/bin/python3
"""
Dunder (Magic) Methods in Python for MLOps
Demonstrates how special methods enable Pythonic behavior
for ML objects and data structures
"""

# Example 1: __str__ - String Representation
# Makes objects human-readable when printed
class Dataset:
    """Dataset class demonstrating __str__ for readable output"""
    
    def __init__(self, path, samples):
        self.path = path
        self.samples = samples

    def __str__(self):
        """Return human-readable string representation"""
        return f"Dataset(path={self.path}, samples={len(self.samples)})"


print("=== Example 1: __str__ Method ===")
train = Dataset("train.csv", [1, 2, 3])
print(train)
# Output: Dataset(path=train.csv, samples=3)

print("\n" + "="*50 + "\n")

# Example 2: __len__ - Enable len() Function
# Allows using built-in len() function on custom objects
class DatasetWithLength:
    """Dataset class demonstrating __len__ for size queries"""
    
    def __init__(self, samples):
        self.samples = samples

    def __len__(self):
        """Return the number of samples in dataset"""
        return len(self.samples)


print("=== Example 2: __len__ Method ===")
train_data = DatasetWithLength([1, 2, 3])
print(f"Dataset length: {len(train_data)}")  # 3

print("\n" + "="*50 + "\n")

# Example 3: __eq__ - Custom Equality Comparison
# Defines how objects are compared with == operator
class Model:
    """Model class demonstrating __eq__ for comparison"""
    
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """Compare models based on their names"""
        return self.name == other.name


print("=== Example 3: __eq__ Method ===")
m1 = Model("baseline")
m2 = Model("baseline")
print(f"Models are equal: {m1 == m2}")  # True

print("\n" + "="*50 + "\n")

# Example 4: __call__ - Make Objects Callable
# Allows objects to be used like functions
class Preprocessor:
    """Preprocessor demonstrating __call__ for function-like behavior"""
    
    def __call__(self, data):
        """Make the object callable - converts strings to lowercase"""
        return [item.lower() for item in data]


print("=== Example 4: __call__ Method ===")
clean = Preprocessor()
result = clean(["Hello", "WORLD"])
print(f"Preprocessed data: {result}")
# Output: ['hello', 'world']



