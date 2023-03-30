from hashlib import sha256
from shutil import unpack_archive
from git import Repo
import sys
import os
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


def git_fetch(url, branch=None):
    file_name = url.split("/")[-1]
    if not branch:
        Repo.clone_from(url, file_name)
    else:
        Repo.clone_from(url, file_name, branch=branch)
    return file_name


def extract(archive):
    previous_dirs = os.listdir()
    unpack_archive(archive)
    current_dirs = os.listdir()
    for directory in current_dirs:
        if directory not in previous_dirs:
            return directory
