#!/usr/bin/python3
"""
pytest Fixtures for MLOps Testing
Demonstrates fixture patterns for ML pipeline testing:
setup/teardown of resources like databases and temporary files
"""

import pytest
import tempfile
import os

# Example 1: Basic Fixture with Setup and Teardown
# Common pattern for database connections in ML data pipelines
print("=== Basic Fixture Example ===")

@pytest.fixture
def db_connection():
    """Fixture that provides a database connection for testing"""
    # Setup: Create connection
    conn = "fake-database-connection"
    print(f"Setup: Created {conn}")
    
    yield conn  # This is where the test runs
    
    # Teardown: Cleanup after test
    print("Teardown: Closing database connection")
    # cleanup code here, for example conn.close()


def test_query(db_connection):
    """Test that uses the database connection fixture"""
    print(f"Test running with: {db_connection}")
    assert db_connection == "fake-database-connection"


print("\n" + "="*50 + "\n")

# Example 2: File System Fixture
# Useful for testing ML model serialization and data processing
print("=== File System Fixture Example ===")

@pytest.fixture
def temp_file():
    """Fixture that provides a temporary file for testing"""
    # Setup: Create temporary file
    file = tempfile.NamedTemporaryFile(delete=False)
    print(f"Setup: Created temp file {file.name}")
    
    yield file.name  # Provide file path to test
    
    # Teardown: Clean up temporary file
    os.unlink(file.name)
    print(f"Teardown: Deleted temp file {file.name}")


def test_file_operations(temp_file):
    """Test that uses the temporary file fixture"""
    # Write some test data (like model weights)
    with open(temp_file, 'w') as f:
        f.write("test model data")
    
    # Verify file exists and has content
    assert os.path.exists(temp_file)
    with open(temp_file, 'r') as f:
        content = f.read()
    assert content == "test model data"
    print(f"Test completed with file: {temp_file}")


print("\n=== Fixture Benefits ===")
print("- Automatic setup/teardown of test resources")
print("- Reusable across multiple tests")
print("- Ensures clean test environment")

print("\n" + "="*50 + "\n")

# Example 3: Session-Scoped Fixture
# Expensive operations run once per test session
print("=== Session-Scoped Fixture Example ===")

@pytest.fixture(scope="session")
def ml_model():
    """Session-scoped fixture for expensive ML model loading"""
    print("Setup: Loading expensive ML model (once per session)")
    model = "trained-model-weights"  # Simulate loading large model
    yield model
    print("Teardown: Unloading ML model (end of session)")

def test_model_prediction_1(ml_model):
    """First test using the shared model"""
    print(f"Test 1 using model: {ml_model}")
    assert ml_model == "trained-model-weights"

def test_model_prediction_2(ml_model):
    """Second test using the same model instance"""
    print(f"Test 2 using same model: {ml_model}")
    assert ml_model == "trained-model-weights"

print("\n=== Fixture Scopes ===")
print("- function (default): Fresh fixture per test")
print("- session: One fixture for entire test session")
print("- Useful for: databases, large datasets, ML models")





