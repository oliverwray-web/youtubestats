# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import pandas as pd
import kagglehub
from datetime import datetime
from kagglehub import KaggleDatasetAdapter
from azure.storage.blob import BlobServiceClient

# Set the path to the file you'd like to load
file_path = "GBvideos.csv"

# Download latest version
path = kagglehub.dataset_download("datasnaek/youtube-new")

print("Path to dataset files:", path)

df = pd.read_csv('C:\\Users\\OliverWray\\.cache\\kagglehub\\datasets\\datasnaek\\youtube-new\\versions\\115\\GBvideos.csv', encoding='latin1', on_bad_lines='skip', lineterminator='\n', quotechar='"')
print ("First 5 records:", df.head())

def upload_to_azure_blob(local_file_path, connection_string, container_name, blob_name):
  # Create the BlobServiceClient object
  blob_service_client = BlobServiceClient.from_connection_string(connection_string)

  # Get a client to interact with the specific container and blob
  blob_client = blob_service_client.get_blob_client(container=container_name, blob = blob_name)

  print(f"Uploading {local_file_path} to container '{container_name}' as '{blob_name}'...")

  # Open the local file in binary read mode and upload it
  with open(local_file_path, "rb") as data:
    # overwrite=True ensures that if a file with the same name exists, it gets replaced
    blob_client.upload_blob(data, overwrite=True)

  print("Upload successful!")

date = datetime.today().strftime('%Y-%m-%d')

file_name = "C:\\Users\\OliverWray\\.cache\\kagglehub\\datasets\\datasnaek\\youtube-new\\versions\\115\\GBvideos.csv"
connection_string = ""
container_name = "bob20"
blob_name = f"{date}_name.csv"
print(blob_name)
upload_to_azure_blob(file_name, connection_string, container_name, blob_name)