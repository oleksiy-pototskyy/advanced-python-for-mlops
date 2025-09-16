#!/usr/bin/python3
"""
Cloud SDKs for MLOps
Demonstrates using AWS, GCP, and Azure SDKs for ML data storage
and model artifact management in cloud environments
"""

# Example 1: AWS S3 with boto3
# Common for storing ML datasets and model artifacts
print("=== AWS S3 Example ===")

try:
    import boto3
    
    # Create S3 client (requires AWS credentials)
    s3 = boto3.client("s3")
    print("S3 client created")
    
    # List objects in bucket (e.g., training datasets)
    response = s3.list_objects_v2(Bucket="my-bucket")
    print("Listing objects in bucket:")
    for obj in response.get("Contents", []):
        print(f"  - {obj['Key']}")
        
except Exception as e:
    print(f"AWS S3 example (requires boto3 and credentials): {e}")

print("\n" + "="*50 + "\n")

# Example 2: Google Cloud Storage
# Popular for ML workflows on GCP
print("=== Google Cloud Storage Example ===")

try:
    from google.cloud import storage
    
    # Create GCS client (requires GCP credentials)
    client = storage.Client()
    bucket = client.bucket("my-bucket")
    blob = bucket.blob("file.txt")
    
    print("GCS client created")
    print("Uploading file to GCS bucket...")
    
    # Upload file (e.g., trained model)
    blob.upload_from_filename("file.txt")
    print("File uploaded successfully")
    
except Exception as e:
    print(f"GCP Storage example (requires google-cloud-storage): {e}")

print("\n" + "="*50 + "\n")

# Example 3: Azure Blob Storage
# Used for ML data storage on Azure platform
print("=== Azure Blob Storage Example ===")

try:
    from azure.storage.blob import BlobServiceClient
    
    # Create Azure client (requires connection string)
    client = BlobServiceClient.from_connection_string("CONNECTION_STRING")
    container = client.get_container_client("my-container")
    blob = container.get_blob_client("file.txt")
    
    print("Azure Blob client created")
    print("Downloading file from Azure blob...")
    
    # Download file (e.g., pre-trained model)
    with open("file.txt", "wb") as f:
        data = blob.download_blob()
        f.write(data.readall())
    print("File downloaded successfully")
    
except Exception as e:
    print(f"Azure Storage example (requires azure-storage-blob): {e}")

print("\n=== Cloud SDK Usage in MLOps ===")
print("- Store training datasets and validation data")
print("- Save and load trained model artifacts")
print("- Manage experiment results and logs")
print("- Enable scalable data processing pipelines")





