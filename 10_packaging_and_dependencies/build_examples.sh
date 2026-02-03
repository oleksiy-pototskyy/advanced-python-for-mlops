#!/bin/bash
"""
Package Build and Installation Examples
Demonstrates modern Python packaging workflow
"""

echo "=== Modern Python Packaging Examples ==="

echo -e "\n1. Install package in development mode:"
echo "pip install -e ."

echo -e "\n2. Install with optional dependencies:"
echo "pip install .[dev]"
echo "pip install .[api]"

echo -e "\n3. Install build tool and create distribution packages:"
echo "pip install build"
echo "python -m build"

echo -e "\n4. Install from built package:"
echo "pip install dist/mlops_pipeline-1.2.3-py3-none-any.whl"

echo -e "\n5. Upload to PyPI (if public):"
echo "python -m twine upload dist/*"

echo -e "\n=== Version Specification Examples ==="
echo "pandas>=1.5,<2.0     # At least 1.5, but not 2.0+"
echo "numpy>=1.20.0        # Minimum version only"
echo "scikit-learn~=1.0.0  # Compatible release (1.0.x)"
echo "mlflow==2.1.0        # Exact version (avoid unless necessary)"

echo -e "\n=== Semantic Versioning ==="
echo "1.2.3 = major.minor.patch"
echo "- Major: Breaking changes"
echo "- Minor: New features (backward compatible)"
echo "- Patch: Bug fixes"