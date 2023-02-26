from hashlib import sha256
from shutil import unpack_archive
import sys
import requests


def http_download(url, expected_hash=None):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    if expected_hash:
        actual_hash = sha256(response.content).hexdigest()
        if expected_hash != actual_hash:
            print("Expected hash:\t", expected_hash)
            print("Actual hash:\t", actual_hash)
            print("File", file_name, "may be corrupted")
            sys.exit("Error: hash mismatch")

    with open(file_name, "wb") as output_file:
        output_file.write(response.content)

    return file_name


# Download file with git protocol
# Library candidate to use: GitPython
# def git_download(url):


def extract(archive):
    extracted_dir_name = archive.split(".")[0]
    unpack_archive(archive, extract_dir=extracted_dir_name)

    return extracted_dir_name
