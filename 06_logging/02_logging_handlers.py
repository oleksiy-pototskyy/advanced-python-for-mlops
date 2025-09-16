#!/usr/bin/python3
"""
Logging Handlers for MLOps
Demonstrates different logging handlers for ML pipeline observability:
console output for development and rotating files for production
"""

import logging
from logging.handlers import RotatingFileHandler

# Create logger for ML pipeline
logger = logging.getLogger("pipeline")
logger.setLevel(logging.DEBUG)  # Capture all levels

print("=== Setting up Multiple Logging Handlers ===")

# Handler 1: Console Output (for development/debugging)
console = logging.StreamHandler()
console.setLevel(logging.INFO)  # Only INFO and above to console
console_format = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(console_format)

# Handler 2: Rotating File Handler (for production logs)
file_handler = RotatingFileHandler(
    "pipeline.log", 
    maxBytes=1024*1024,  # 1MB per file
    backupCount=5        # Keep 5 backup files
)
file_handler.setLevel(logging.DEBUG)  # All levels to file
file_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)

# Add handlers to logger
logger.addHandler(console)
logger.addHandler(file_handler)

print("Handlers configured: Console (INFO+) and File (DEBUG+)")
print("\n=== Testing Multi-Handler Logging ===")

# Test logging at different levels
logger.info("Pipeline started")           # Goes to both console and file
logger.debug("Loading data from S3")      # Only goes to file
logger.warning("Low memory warning")      # Goes to both console and file
logger.error("Failed to load model")      # Goes to both console and file

print("\nCheck 'pipeline.log' file for detailed DEBUG logs")







