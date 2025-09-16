#!/usr/bin/python3
"""
Subprocess Management for MLOps
Demonstrates running external commands and tools from Python
for ML pipeline integration and system operations
"""

import subprocess

# Example 1: Basic Command Execution
# Run external ML tools, data processing scripts, or system commands
print("=== Basic Subprocess Execution ===")

# Run a simple shell command (could be ML training script)
result = subprocess.run(["echo", "Hello from subprocess"], capture_output=True, text=True)

print("Return code:", result.returncode)
print("Output:", result.stdout.strip())
print("Command completed synchronously")

print("\n" + "="*50 + "\n")

# Example 2: Command with Error Handling
# Essential for robust ML pipeline execution
print("=== Subprocess with Error Handling ===")

# Run directory listing (could be checking for model files)
result = subprocess.run(["ls", "-l"], capture_output=True, text=True)

if result.returncode == 0:
    print("Command succeeded")
    print("Directory listing:")
    print(result.stdout)
else:
    print("Command failed with error:")
    print(result.stderr)

print("\n" + "="*50 + "\n")

# Example 3: Streaming Output with Popen
# Useful for long-running ML training processes
print("=== Streaming Subprocess Output ===")

# Start process that produces streaming output
print("Starting ping command (streaming output)...")
process = subprocess.Popen(
    ["ping", "-c", "2", "google.com"], 
    stdout=subprocess.PIPE, 
    text=True
)

# Process output line by line as it arrives
for line in process.stdout:
    print("LIVE OUTPUT:", line.strip())

# Wait for process to complete
process.wait()
print(f"Process finished with exit code: {process.returncode}")

print("\n=== Subprocess Use Cases in MLOps ===")
print("- Execute ML training scripts and tools")
print("- Run data preprocessing pipelines")
print("- Integrate with external ML frameworks")
print("- Monitor system resources during training")



