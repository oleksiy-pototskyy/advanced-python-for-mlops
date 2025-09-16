#!/usr/bin/python3
"""
Mocks & Patches for MLOps Testing
Demonstrates mocking external dependencies in ML pipelines:
API calls, database connections, and cloud services
"""

from unittest.mock import Mock, patch

# Example 1: Basic Mock Objects
# Simulate API responses for ML model serving endpoints
print("=== Basic Mock Example ===")

mock_response = Mock()
mock_response.status_code = 200
mock_response.json.return_value = {"message": "ok"}

print(f"Mock status code: {mock_response.status_code}")
print(f"Mock JSON response: {mock_response.json()}")

# Test the mock behavior
assert mock_response.json()["message"] == "ok"
print("✓ Mock assertion passed")

print("\n" + "="*50 + "\n")

# Example 2: Patching External Dependencies
# Mock external API calls to test ML data fetching without network
print("=== Patch Example ===")

def fetch_data():
    """Function that fetches data from external API"""
    import requests
    return requests.get("https://example.com").status_code

print("Testing fetch_data() with mocked requests...")

# Patch requests.get to avoid actual HTTP calls
with patch("requests.get") as mock_get:
    # Configure the mock return value
    mock_get.return_value.status_code = 200
    
    # Test the function with mocked dependency
    result = fetch_data()
    print(f"Mocked API call returned: {result}")
    
    assert result == 200
    print("✓ Patch assertion passed")
    
    # Verify the mock was called
    mock_get.assert_called_once_with("https://example.com")
    print("✓ Mock call verification passed")

print("\n=== Mocking Benefits ===")
print("- Test without external dependencies")
print("- Control return values and exceptions")
print("- Verify function calls and arguments")




