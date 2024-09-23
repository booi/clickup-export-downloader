import csv
import requests
import json
import os
import argparse
from urllib.parse import urlparse

# Function to download a file from a URL
def download_file(url, file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return file_path

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Download attachments from a CSV file.')
    parser.add_argument('csv_file', help='Path to the CSV file')
    parser.add_argument('attachments_directory', help='Path to the attachments directory')
    args = parser.parse_args()

    csv_file_path = args.csv_file
    attachments_directory = os.path.realpath(args.attachments_directory)
    print(f"attachments_directory: {attachments_directory}")

    # Create a directory to save the downloaded files
    os.makedirs(attachments_directory, exist_ok=True)

    # Read the CSV file and download attachments
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            attachments = json.loads(row['Attachments'])
            for attachment in attachments:
                attachment_url = attachment['url']

                # Example: https://t36020761.p.clickup-attachments.com/t36020761/558c3e42-f426-42cf-bb34-9a2aae5b841c/image.png"}]

                if attachment_url:
                    parsed_url = urlparse(attachment_url)
                    file_path  = os.path.join(attachments_directory, parsed_url.path[1:])
                    try:
                        print(f"Downloading {attachment_url} to {file_path}")
                        download_file(attachment_url, file_path)
                    except Exception as e:
                        print(f"Failed to download {attachment_url}: {e}")

if __name__ == '__main__':
    main()