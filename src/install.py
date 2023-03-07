import subprocess
import os
import shutil


# commands as a list of strings to be executed
def install_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)


# files as a list of strings representing paths
# each file should be copied to the destination directory
def file_copy(files, destination):
    os.makedirs(destination, exist_ok=True)

    for file_path in files:
        file_name = os.path.basename(file_path)
        destination_path = os.path.join(destination, file_name)
        shutil.copy(file_path, destination_path)
