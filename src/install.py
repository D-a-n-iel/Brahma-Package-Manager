import subprocess


# commands as a list of strings to be executed
def install_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)

# files as a list of strings representing paths
# each file should be copied to the destination directory
def file_copy(files, destination):
    """TODO"""
