#!/usr/bin/python3
"""
Advanced Logging for MLOps
Demonstrates structured logging patterns for machine learning pipelines
including custom formatters and JSON logging for observability
"""

import logging
import json

# Example 1: Basic Logging Configuration
# Standard logging setup with custom format for ML workflows
print("=== Basic Logging Configuration ===")
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    level=logging.INFO
)
logging.info("Model training started")

print("\n" + "="*40 + "\n")

# Example 2: Named Logger with Different Level
# Component-specific loggers for different parts of ML pipeline
print("=== Named Logger Example ===")
logger = logging.getLogger("data_pipeline")
logger.setLevel(logging.DEBUG)
logger.debug("Loading dataset from S3")
logger.info("Dataset loaded successfully")

print("\n" + "="*40 + "\n")

# Example 3: Structured JSON Logging
# JSON format enables better log parsing and monitoring in production
print("=== Structured JSON Logging ===")

def json_log(level, message, **kwargs):
    """Log structured data in JSON format for better observability"""
    log_entry = {"level": level, "message": message, **kwargs}
    print(json.dumps(log_entry))

# Log ML metrics and metadata in structured format
json_log("INFO", "Training complete", accuracy=0.92, runtime="2h15m")
json_log("INFO", "Model evaluation", precision=0.89, recall=0.94, f1_score=0.91)


