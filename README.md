# Advanced Python for MLOps

Advanced Python programming concepts and patterns for Machine Learning Operations (MLOps) workflows.

**Course URL**: [Advanced Python for MLOps - MLOps Specialization](https://nubes.academy/advanced-python-for-mlops-mlops-specialization/)

## Overview

This repository contains practical Python examples demonstrating advanced programming concepts essential for MLOps practitioners. Each module focuses on specific Python features commonly used in production ML systems.

## Project Structure

```
advanced-python-for-mlops/
├── 01_functions/
│   └── 01_decorators.py                    # Function decorators for ML workflows
├── 02_modules_and_packages/
│   ├── plugins/                            # Plugin architecture examples
│   │   ├── accuracy.py                     # Accuracy metric plugin
│   │   └── f1score.py                      # F1 score metric plugin
│   └── 01_dynamic_imports_and_plugin_patterns.py
├── 03_classes_and_oop/
│   ├── 01_inheritance.py                   # OOP inheritance patterns
│   └── 02_dunder_or_magic_methods.py       # Python magic methods
├── 04_exceptions_and_error_handling/
│   └── 01_nested_exception_handling.py     # Error handling in ML pipelines
├── 05_file_and_os_operations/
│   └── 01_high_performance_file_io.py      # Efficient file operations
├── 06_logging/
│   ├── 01_advanced_logging.py              # Structured logging
│   └── 02_logging_handlers.py              # Multiple logging handlers
├── 07_serialization/
│   └── 01_advanced_serialization.py        # Parquet, HDF5 serialization
├── 08_testing/
│   ├── 01_pytest_fixtures.py               # Testing with fixtures
│   └── 02_mocks_and_patches.py             # Mocking external dependencies
├── 09_external_libraries/
│   ├── 01_cloud_sdks.py                    # AWS, GCP, Azure SDKs
│   ├── 02_docker_and_kubernetes_python_sdks.py
│   └── 03_ml_platform_sdks.py              # MLflow integration
├── 11_concurrency_and_parallelism/
│   ├── 01_thread_based_parallelism.py      # Threading for I/O tasks
│   ├── 02_process_based_parallelism.py     # Multiprocessing for CPU tasks
│   ├── 03_parallel_tasks_management.py     # ProcessPoolExecutor
│   ├── 04_subprocess_management.py         # External process management
│   └── 05_synchronized_queue.py            # Thread/process communication
├── 12_building_machine_learning_apis/
│   ├── 01_introduction_to_ml_apis.py       # Basic ML API concepts
│   ├── 02_introduction_to_flask_framework.py
│   ├── 03_building_api_with_flask.py       # Flask API development
│   ├── 04_introduction_to_fastapi.py       # FastAPI basics
│   └── 05_building_api_with_fastapi.py     # FastAPI development
├── requirements.txt                         # Project dependencies
└── README.md                               # This file
```

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd advanced-python-for-mlops
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Each Python file is self-contained and can be run independently:

```bash
# Run individual examples
python 01_functions/01_decorators.py
python 06_logging/01_advanced_logging.py
python 12_building_machine_learning_apis/04_introduction_to_fastapi.py
```

### Running Tests

```bash
# Run pytest examples
python -m pytest 08_testing/01_pytest_fixtures.py -v
```

### Running APIs

```bash
# Flask API
python 12_building_machine_learning_apis/02_introduction_to_flask_framework.py

# FastAPI (requires uvicorn)
uvicorn 12_building_machine_learning_apis.04_introduction_to_fastapi:app --reload
```

## Key Learning Topics

- **Functions & Decorators**: Timing, logging, and validation decorators
- **Modules & Packages**: Dynamic imports and plugin architectures
- **OOP Concepts**: Inheritance and magic methods for ML objects
- **Error Handling**: Robust exception handling in ML pipelines
- **File Operations**: High-performance I/O for large datasets
- **Logging**: Structured logging for ML observability
- **Serialization**: Efficient data formats (Parquet, HDF5)
- **Testing**: pytest fixtures and mocking for ML code
- **External Libraries**: Cloud SDKs and ML platform integration
- **Concurrency**: Threading and multiprocessing for ML workloads
- **API Development**: Flask and FastAPI for ML model serving

## Notes

- Examples use realistic MLOps scenarios (model training, data processing, API serving)
- Code includes educational comments explaining concepts and use cases
- Some examples require external services (cloud credentials, Docker daemon)
- All code follows Python best practices for production ML systems

## Course Information

This repository accompanies the **Advanced Python for MLOps** course, part of the MLOps Specialization.

**Learn more**: [nubes.academy/advanced-python-for-mlops-mlops-specialization](https://nubes.academy/advanced-python-for-mlops-mlops-specialization/)