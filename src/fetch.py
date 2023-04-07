from hashlib import sha256
from shutil import unpack_archive, rmtree
from git import Repo
import os
import requests
import utils


def http_download(url, expected_hash=None):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    if expected_hash:
        actual_hash = sha256(response.content).hexdigest()
        if expected_hash != actual_hash:
            rmtree(file_name)
            utils.error(
                "hash mismatch",
                f"expected hash:\t{expected_hash}"
                f"actual hash:\t{actual_hash}"
                f"File {file_name} may be corrupted",
            )

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
