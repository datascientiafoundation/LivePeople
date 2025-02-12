import argparse
import os
from minio import Minio
import pandas as pd
from datetime import datetime
import json
import paramiko
import uuid
import io
from stat import S_ISDIR
import sys
import re
from tqdm import tqdm

def get_extension(dataset_dir):
    return os.path.splitext(dataset_dir)[1]

def get_dataset_identifier(dataset_name, dataset_mapping):
    # Load dataset-to-directory mapping from the mapping file (CSV)

    # Check if the dataset is in the mapping file
    if dataset_name in dataset_mapping['dataset_name'].values:
        # If found, get the directory path from the mapping file
        dataset_id = dataset_mapping.loc[dataset_mapping['dataset_name'] == dataset_name, 'identifier'].values[0]
        return dataset_id
    else:
        print(f"Dataset {dataset_name} not found in the mapping file.")
        return None


def get_dataset_directory(ssh, dataset_name, dataset_mapping):
    # Load dataset-to-directory mapping from the mapping file (CSV)

    # Check if the dataset is in the mapping file
    if dataset_name in dataset_mapping['dataset_name'].values:
        # If found, get the directory path from the mapping file
        dataset_dir = dataset_mapping.loc[dataset_mapping['dataset_name'] == dataset_name, 'directory'].values[0]

        # Now, check if the directory exists in the remote server (CREP directory)
        if is_dataset_exist(ssh, dataset_dir):
            return dataset_dir
        else:
            print(f"Dataset directory {dataset_dir} not found in the CREP directory.")
            return None
    else:
        print(f"Dataset {dataset_name} not found in the mapping file.")
        return None



def create_minio_bucket(minio_client, bucket_name):
    # Check if the bucket exists, create if not
    pass

def upload_dataset_to_minio(minio_client, bucket_name, dataset_dir):
    # Upload dataset files to Minio bucket
    pass

def connect_ssh(hostname, username, private_key_path):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.RejectPolicy())  # Secure: reject unknown hosts

    private_key = paramiko.RSAKey.from_private_key_file(private_key_path)
    client.connect(hostname, username=username, pkey=private_key)
    return client

def is_dataset_exist(ssh, dataset_path):
    # Check if the dataset exists in the specified directory on the remote server
    stdin, stdout, stderr = ssh.exec_command(f"test -e {dataset_path} && echo 'exists' || echo 'not exists'")
    result = stdout.read().decode('utf-8').strip()
    return result == "exists"


def create_remote_directory(ssh, remote_directory):
    try:
        # Ensure the remote directory exists by running 'mkdir -p' command
        ssh.exec_command(f"mkdir -p {remote_directory}")
        print(f"Directory {remote_directory} created or already exists.")
    except Exception as e:
        print(f"Error creating directory {remote_directory}: {e}")


# def copy_directory_using_ssh(ssh, source_path, destination_path):
#     try:
#         # Execute the cp -r command via SSH to copy the directory
#         stdin, stdout, stderr = ssh.exec_command(f"cp -r {source_path} {destination_path}")
#
#         # Read the output and error streams
#         error = stderr.read().decode('utf-8')
#         if error:
#             print(f"Error occurred: {error}")
#         else:
#             print(f"Directory copied from {source_path} to {destination_path}")
#         return True
#     except Exception as e:
#         print(f"Error executing copy command: {e}")
#         return False

#
# def copy_directory_using_ssh(ssh, source_path, destination_path):
#     try:
#         # Use rsync for progress tracking
#         command = f"rsync -ah --info=progress2 {source_path}/ {destination_path}/"
#
#         stdin, stdout, stderr = ssh.exec_command(command)
#
#         # Extract total file size using regex
#         total_size = 0
#         for line in stdout:
#             match = re.search(r'total size is (\d+) speedup', line)
#             if match:
#                 total_size = int(match.group(1))
#                 break
#
#         # Initialize progress bar
#         progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Copying")
#
#         # Read output line by line and update progress
#         for line in stdout:
#             match = re.search(r'(\d+)%', line)  # Match percentage progress
#             if match:
#                 progress_bar.n = int(total_size * int(match.group(1)) / 100)
#                 progress_bar.refresh()
#
#         progress_bar.close()
#
#         # Check for errors
#         error = stderr.read().decode('utf-8').strip()
#         if error:
#             print(f"Error occurred: {error}")
#             return False
#
#         print(f"Directory copied successfully from {source_path} to {destination_path}")
#         return True
#
#     except Exception as e:
#         print(f"Error executing copy command: {e}")
#         return False

def copy_directory_using_ssh(ssh, source_path, destination_path):
    try:
        command = f"rsync -ah --info=progress2 {source_path}/ {destination_path}/"
        stdin, stdout, stderr = ssh.exec_command(command)

        # Print progress in real-time
        for line in iter(stdout.readline, ""):
            print(line, end="")

        error = stderr.read().decode('utf-8')
        if error:
            print(f"Error occurred: {error}")
        else:
            print(f"Directory copied")
        return True
    except Exception as e:
        print(f"Error executing rsync command: {e}")
        return False



def is_directory(ssh, path):
    # Check if the given path is a directory
    stdin, stdout, stderr = ssh.exec_command(f"test -d {path} && echo 'dir' || echo 'not dir'")
    result = stdout.read().decode('utf-8').strip()
    return result == "dir"


def minio_create_bucket(client, bucket_name):
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

def minio_upload_file_to_bucket(client, bucket_name,source_file, destination_file ):
    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )

    policy = {
        "PolicyName": "request-2-policy",
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": ["s3:GetBucketLocation", "s3:ListBucket"],
                "Resource": f"arn:aws:s3:::{bucket_name}",  # Use the actual bucket name
            },
            {
                "Effect": "Allow",
                "Principal": {"AWS": "*"},
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*",  # Use the actual bucket name
            },
        ],
    }

    client.set_bucket_policy(bucket_name, json.dumps(policy))

    print(
        "UPLOADED:", source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )

def stream_and_upload_to_minio(ssh, minio_client, bucket_name, remote_file_path, object_name):
    """
    Streams a file or directory (for partitioned Parquet files) from a remote server via SSH and uploads it to MinIO.

    :param ssh: Paramiko SSH client (already connected).
    :param minio_client: MinIO client (already initialized).
    :param remote_file_path: Path to the dataset on the remote server.
    :param bucket_name: MinIO bucket name.
    :param object_name: Object name to be used in MinIO (usually the filename).
    """
    try:
        # Open remote file via SFTP (binary mode)
        sftp = ssh.open_sftp()

        # Check if the remote path is a directory
        if is_directory(sftp, remote_file_path):
            # If it's a directory, list all files inside it
            remote_files = sftp.listdir(remote_file_path)

            # Upload each file individually
            for remote_file_name in remote_files:
                remote_file_full_path = f"{remote_file_path}/{remote_file_name}"
                stream_and_upload_to_minio(ssh, minio_client, bucket_name, remote_file_full_path,
                                           f"{object_name}/{remote_file_name}")

        else:
            # Otherwise, handle it as a single file (standard file upload)
            remote_file = sftp.open(remote_file_path, 'rb')

            # Prepare to upload to MinIO by reading in chunks
            chunk_size = 1024 * 1024  # 1MB chunk size

            # Upload to MinIO in chunks directly (no buffer holding entire file)
            while True:
                data_chunk = remote_file.read(chunk_size)
                if not data_chunk:
                    break  # Stop if there's no more data

                # Upload the current chunk to MinIO directly
                minio_client.put_object(
                    bucket_name=bucket_name,
                    object_name=object_name,
                    data=io.BytesIO(data_chunk),
                    length=len(data_chunk),
                    part_size=10 * 1024 * 1024  # 10MB chunk size for large files
                )

            print(f"Uploaded {remote_file_path} to MinIO bucket: {bucket_name}")

            # Close the remote file and SFTP connection
            remote_file.close()

        sftp.close()

    except Exception as e:
        print(f"Failed to upload {remote_file_path} to MinIO: {e}")

def is_directory(sftp, remote_path):
    """Check if a remote path is a directory."""
    try:
        return S_ISDIR(sftp.lstat(remote_path).st_mode)
    except IOError:
        return False

def is_project(dataset):
    return str(dataset['is_project']).lower() == "true"

def is_bundle(dataset):
    return str(dataset['is_bundle']).lower() == "true"

def is_dataset(dataset):
    return str(dataset['is_dataset']).lower() == "true"


def extract_datasets(requested_datasets):
    all_datasets = []
    for reqested_ds in requested_datasets:
        if is_project(reqested_ds):
            identifier_key = '.'.join(reqested_ds['dataset_identifier'].split('.')[0:-1])
            datasets = dataset_mapping[dataset_mapping['identifier'].str.startswith(identifier_key)]
            all_datasets.append(datasets)

        elif is_bundle(reqested_ds):
            child_identifiers = ['.'.join(reqested_ds['dataset_identifier'].split('.')[0:-1]) + '.' + suff for suff in reqested_ds['dataset_identifier'].split('.')[-1].split('-')]
            datasets = dataset_mapping[dataset_mapping['identifier'].isin(child_identifiers)]
            all_datasets.append(datasets)

        elif is_dataset(reqested_ds):
            datasets = dataset_mapping[dataset_mapping['dataset_name'] == reqested_ds["dataset_name"]]
            all_datasets.append(datasets)
        else:
            print(f"Could not find dataset for request: {reqested_ds['dataset_name']}")
            print("Input type error")

    all_datasets = pd.concat(all_datasets, ignore_index=True)
    return all_datasets


def main(request_data, minio_host, minio_access_key, minio_secret_key, hostname, username, private_key_path, dataset_mapping, drep_dir):

    request_id = request_data["request_id"]
    requester_id = request_data["requester_id"]
    request_body = request_data["datasets"]

    datasets = extract_datasets(request_body)

    if len(datasets) != 0:

        try:
            ssh = connect_ssh(hostname, username, private_key_path)

            # Initialize Minio client
            client = Minio(
                minio_host,  # MinIO host and port
                access_key=minio_access_key,
                secret_key=minio_secret_key,
                secure=False  # Force HTTP instead of HTTPS
            )
            bucket_name = f"{request_id}-{requester_id}"  # <REQUEST_ID>-<REQUESTER_DS_USERNAME>
            minio_create_bucket(client, bucket_name)

        except Exception as e:
            print(e)
            ssh.close()
            return

        for _, row in datasets.iterrows():

            dataset_name = row['dataset_name']
            dataset_identifier = row['identifier']
            crep_dataset_dir = row['directory']
            # drep_dataset_dir = os.path.join(drep_dir, dataset_identifier + get_extension(crep_dataset_dir))
            drep_dataset_dir = os.path.join(drep_dir, dataset_name.replace(' ', '') + get_extension(crep_dataset_dir))

            print('Dataset requested:',dataset_name)
            print('Dataset CREP:', crep_dataset_dir)
            print('Dataset DREP:', drep_dataset_dir)

            if not is_dataset_exist(ssh, drep_dataset_dir):
                copy_directory_using_ssh(ssh, crep_dataset_dir, drep_dataset_dir)
            else:
                print('Dataset already exist in DREP')

            try:
                object_name = os.path.basename(drep_dataset_dir)
                source_file = drep_dataset_dir
                # minio_upload_file_to_bucket(client, bucket_name, source_file, object_name )
                stream_and_upload_to_minio(ssh, client, bucket_name, source_file, object_name)

            except Exception as e:
                print(e)

            print()

        ssh.close()
    print("finished")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create MinIO bucket and upload dataset.")
    parser.add_argument("--json_file", type=str, required=False, default= 'sources/dataset-download-request-sample.json', help="Path to JSON request file.")
    parser.add_argument("--minio_host", type=str, required=False, default='192.168.159.128:31667', help="MinIO host URL.")
    parser.add_argument("--minio_access_key", type=str, required=False, default=os.getenv("MINIO_ACCESS_KEY"), help="MinIO access key.")
    parser.add_argument("--minio_secret_key", type=str, required=False, default=os.getenv("MINIO_SECRET_KEY"), help="MinIO secret key.")
    parser.add_argument("--hostname", type=str, default="streambase3.disi.unitn.it", help="SSH hostname.")
    parser.add_argument("--username", type=str, default="m.bayanjargal", help="SSH username.")
    parser.add_argument("--private_key_path", type=str, default="/Users/munkhdelger/.ssh/id_rsa_streambase", help="Path to SSH private key file.")
    parser.add_argument("--mapping_file", type=str, default="sources/dataset_dir_mapping.csv", help="Path to dataset directory mapping file.")
    parser.add_argument("--drep_dataset_dir", type=str, default="/datascientia_repository/DREP/dataset", help="DREP dataset directory path.")

    args = parser.parse_args()

    with open(args.json_file, "r") as file:
        request_data = json.load(file)

    dataset_mapping = pd.read_csv(args.mapping_file)
    dataset_mapping = dataset_mapping[dataset_mapping['identifier'] != "Unknown"]

    main(request_data, args.minio_host, args.minio_access_key, args.minio_secret_key,
         args.hostname, args.username, args.private_key_path, dataset_mapping, args.drep_dataset_dir)