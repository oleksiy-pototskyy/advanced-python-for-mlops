#!/usr/bin/python3
"""
Logging Handlers for MLOps
Demonstrates different logging handlers for ML pipeline observability:
console output for development and rotating files for production
"""

import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler, SocketHandler, HTTPHandler, SysLogHandler

# Create logger for ML pipeline
logger = logging.getLogger("pipeline")
logger.setLevel(logging.DEBUG)  # Capture all levels

print("=== Setting up Multiple Logging Handlers ===")

# Example 1: Console Output (for development/debugging)
console = logging.StreamHandler()
console.setLevel(logging.INFO)  # Only INFO and above to console
console_format = logging.Formatter('%(levelname)s - %(message)s')
console.setFormatter(console_format)

# Example 2: Basic FileHandler (simple file logging)
print("\n=== FileHandler Example ===")
file_logger = logging.getLogger("simple_file")
file_logger.setLevel(logging.INFO)

simple_file = logging.FileHandler("simple.log")
simple_file.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
file_logger.addHandler(simple_file)

file_logger.info("Model training started")
file_logger.warning("File can grow large without rotation!")
print("Logs written to 'simple.log' (grows indefinitely)")

# Example 3: Rotating File Handler (for production logs)
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

# Example 4: TimedRotatingFileHandler (rotate by time)
print("\n=== TimedRotatingFileHandler Example ===")
timed_logger = logging.getLogger("timed_rotation")
timed_logger.setLevel(logging.INFO)

# Rotate daily at midnight, keep 7 days of logs
timed_handler = TimedRotatingFileHandler(
    "daily.log", 
    when="midnight",  # Options: 'S', 'M', 'H', 'D', 'midnight'
    interval=1,       # Every 1 day
    backupCount=7     # Keep 7 days
)
timed_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
timed_logger.addHandler(timed_handler)

timed_logger.info("Long-running service log entry")
print("Logs rotate daily at midnight, keeping 7 days")

# Example 5: Advanced Handlers (for distributed systems)
print("\n=== Advanced Handlers Example ===")

# SocketHandler - send logs to remote server
try:
    socket_handler = SocketHandler('localhost', 9999)
    print("SocketHandler: Sends logs to remote server (localhost:9999)")
except:
    print("SocketHandler: Would send to remote server (connection failed)")

# HTTPHandler - send logs via HTTP POST
try:
    http_handler = HTTPHandler('localhost:8080', '/logs')
    print("HTTPHandler: Sends logs via HTTP POST to /logs endpoint")
except:
    print("HTTPHandler: Would send logs via HTTP (server unavailable)")

# SysLogHandler - system logging (Unix/Linux)
try:
    syslog_handler = SysLogHandler(address='/dev/log')
    print("SysLogHandler: Sends logs to system logger")
except:
    print("SysLogHandler: Would send to system logger (not available)")

print("\nAdvanced handlers enable centralized logging in distributed ML systems")







