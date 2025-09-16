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



