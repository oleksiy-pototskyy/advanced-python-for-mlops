#!/usr/bin/python3
"""
ML Platform SDKs for MLOps
Demonstrates MLflow SDK for experiment tracking, model logging,
and ML lifecycle management in production workflows
"""

# Example 1: MLflow Experiment Tracking
# Track parameters, metrics, and artifacts for ML experiments
print("=== MLflow Experiment Tracking ===")

try:
    import mlflow
    
    # Start an MLflow run (experiment session)
    with mlflow.start_run():
        print("MLflow run started")
        
        # Log hyperparameters
        mlflow.log_param("learning_rate", 0.01)
        print("Logged parameter: learning_rate = 0.01")
        
        # Log performance metrics
        mlflow.log_metric("accuracy", 0.95)
        print("Logged metric: accuracy = 0.95")
        
        # Log configuration files or other artifacts
        try:
            mlflow.log_artifact("config.yaml")
            print("Logged artifact: config.yaml")
        except FileNotFoundError:
            print("Artifact config.yaml not found (would log if exists)")
        
        print("MLflow run completed")
        
except Exception as e:
    print(f"MLflow tracking example (requires mlflow library): {e}")

print("\n" + "="*50 + "\n")

# Example 2: MLflow Model Logging
# Log trained models for versioning and deployment
print("=== MLflow Model Logging ===")

try:
    import mlflow.sklearn
    
    # Create a dummy model for demonstration
    from sklearn.linear_model import LogisticRegression
    import numpy as np
    
    # Train a simple model
    X = np.array([[1, 2], [3, 4], [5, 6]])
    y = np.array([0, 1, 0])
    model = LogisticRegression().fit(X, y)
    
    print("Trained a simple LogisticRegression model")
    
    # Log the model to MLflow
    with mlflow.start_run():
        mlflow.sklearn.log_model(model, "model")
        print("Model logged to MLflow with name 'model'")
        
except Exception as e:
    print(f"MLflow model logging example (requires mlflow and sklearn): {e}")

print("\n=== MLflow Benefits in MLOps ===")
print("- Experiment tracking and reproducibility")
print("- Model versioning and registry")
print("- Automated model deployment")
print("- Collaboration and model governance")





