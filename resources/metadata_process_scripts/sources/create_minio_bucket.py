import argparse
import os
from minio import Minio
import pandas as pd

def get_dataset_directory(dataset_name, mapping_file):
    # Load dataset-to-directory mapping from the previous script's output

    dataset_dirs= pd.read_csv(mapping_file)

    pass

def create_minio_bucket(minio_client, bucket_name):
    # Check if the bucket exists, create if not
    pass

def upload_dataset_to_minio(minio_client, bucket_name, dataset_dir):
    # Upload dataset files to Minio bucket
    pass

def main(dataset_name, mapping_file, dataset_identifier, minio_host, minio_access_key, minio_secret_key):
    # Initialize Minio client
    # minio_client = Minio(minio_host, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

    # Get dataset directory
    dataset_dir = get_dataset_directory(dataset_name, mapping_file)

    # Create bucket and upload data
    # bucket_name = dataset_name.replace("_", "-").lower()
    # create_minio_bucket(minio_client, bucket_name)
    # upload_dataset_to_minio(minio_client, bucket_name, dataset_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create MinIO bucket and upload dataset.")
    parser.add_argument("--dataset_name", type=str, default='' help="Name of the dataset.")
    parser.add_argument("--dataset_identifier", type=str, default='', help="Identifier of the dataset.")
    parser.add_argument("--mapping_file", type=str, default='default="/Users/munkhdelger/Knowdive/LivePeople/resources/metadata_process_scripts/sources/dataset_dirs",' help="Path to dataset mapping file.")
    parser.add_argument("--minio_host", type=str, required=False, default="", help="MinIO host URL.")
    parser.add_argument("--minio_access_key", type=str, required=False, default="", help="MinIO access key.")
    parser.add_argument("--minio_secret_key", type=str, required=False, default="", help="MinIO secret key.")

    args = parser.parse_args()
    main(args.dataset_name, args.mapping_file, args.dataset_identifier, args.minio_host, args.minio_access_key, args.minio_secret_key)
