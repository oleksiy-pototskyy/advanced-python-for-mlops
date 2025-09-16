#!/usr/bin/python3
"""
Nested Exception Handling in Python for MLOps
Demonstrates how to handle multiple layers of exceptions
in ML data processing pipelines
"""

# Example 1: Nested try-except with finally
# Common pattern for file operations with cleanup
print("=== Example 1: Nested Exception Handling ===")
try:
    # Outer try: Handle file access errors
    f = open("data.txt")
    try:
        # Inner try: Handle data processing errors
        data = f.read()
        number = int(data)
        print(f"Successfully parsed number: {number}")
    except ValueError:
        print("File content is not a valid number")
    finally:
        # Always close the file, regardless of success/failure
        f.close()
        print("File closed")
except FileNotFoundError:
    print("The file does not exist")

print("\n" + "="*50 + "\n")

# Example 2: Exception Propagation in ML Pipeline
# Shows how exceptions bubble up through function calls
print("=== Example 2: Exception Propagation ===")

def read_file(path):
    """Read file content - propagates FileNotFoundError"""
    try:
        return open(path).read()
    except FileNotFoundError:
        print(f"Error in read_file: {path} not found")
        raise  # Re-raise the exception to caller

def parse_number(text):
    """Parse text to number - propagates ValueError"""
    try:
        return int(text.strip())
    except ValueError:
        print(f"Error in parse_number: '{text}' is not a valid number")
        raise  # Re-raise the exception to caller

# ML pipeline with centralized error handling
try:
    content = read_file("data.txt")
    value = parse_number(content)
    print(f"Pipeline success: processed value = {value}")
except FileNotFoundError:
    print("Pipeline failed: Input file missing")
except ValueError:
    print("Pipeline failed: Invalid data format")
except Exception as e:
    print(f"Pipeline failed with unexpected error: {e}")




