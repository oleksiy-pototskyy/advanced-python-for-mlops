# MLOps Pipeline Package

A modern Python package for MLOps workflows with proper dependency management.

## Installation

```bash
# Install the package
pip install .

# Install with development dependencies
pip install .[dev]

# Install with API dependencies
pip install .[api]
```

## Usage

```python
from mlops_pipeline.models import ModelTrainer
from mlops_pipeline.data import DataProcessor

# Train a model
trainer = ModelTrainer()
model = trainer.train(data_path="data.csv")

# Deploy model
trainer.deploy(model, endpoint="production")
```

## CLI Commands

```bash
# Train model via CLI
train-model --data data.csv --output model.pkl

# Deploy model
deploy-model --model model.pkl --endpoint production
```

## Development

```bash
# Install development dependencies
pip install .[dev]

# Run tests
pytest

# Format code
black src/

# Type checking
mypy src/
```

## Version

Current version: 1.2.3 (major.minor.patch)
- Major: Breaking changes
- Minor: New features
- Patch: Bug fixes