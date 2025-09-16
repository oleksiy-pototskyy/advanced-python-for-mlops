#!/usr/bin/python3
"""
Docker & Kubernetes Python SDKs for MLOps
Demonstrates container orchestration and management for ML workloads
using Python SDKs for Docker and Kubernetes
"""

# Example 1: Docker Python SDK
# Manage ML model containers programmatically
print("=== Docker Python SDK Example ===")

try:
    import docker
    
    # Connect to Docker daemon
    client = docker.from_env()
    print("Docker client connected")
    
    # Run a container (e.g., ML inference service)
    print("Running Ubuntu container with 'echo hello' command...")
    container = client.containers.run(
        "ubuntu:20.04", 
        "echo hello", 
        detach=True
    )
    
    # Get container logs
    logs = container.logs()
    print(f"Container logs: {logs.decode('utf-8').strip()}")
    
    # Cleanup container
    container.remove()
    print("Container removed")
    
except Exception as e:
    print(f"Docker example (requires docker library and Docker daemon): {e}")

print("\n" + "="*50 + "\n")

# Example 2: Kubernetes Python SDK
# Manage ML workloads in Kubernetes clusters
print("=== Kubernetes Python SDK Example ===")

try:
    from kubernetes import client, config
    
    # Load Kubernetes configuration
    config.load_kube_config()
    v1 = client.CoreV1Api()
    print("Kubernetes client configured")
    
    # List all pods across namespaces (e.g., ML training jobs)
    print("Listing all pods in cluster:")
    pods = v1.list_pod_for_all_namespaces()
    
    for pod in pods.items:
        namespace = pod.metadata.namespace
        name = pod.metadata.name
        status = pod.status.phase
        print(f"  - {namespace}/{name} ({status})")
        
    print(f"Total pods found: {len(pods.items)}")
    
except Exception as e:
    print(f"Kubernetes example (requires kubernetes library and cluster access): {e}")

print("\n=== Container Orchestration in MLOps ===")
print("Docker SDK: Build, run, and manage ML model containers")
print("Kubernetes SDK: Deploy and scale ML workloads in clusters")
print("Use cases: Model serving, training jobs, data processing")






