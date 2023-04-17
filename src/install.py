import subprocess
import os
import shutil


# commands as a list of strings to be executed
def install_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)


def gnu_make_install():
    subprocess.run("make install", shell=True)


def file_copy(source, destination):
    shutil.copy(source, destination)


def make_executable(path):
    os.chmod(path, 0o755)
