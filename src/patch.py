import subprocess

# Given a pair of strings, every match of the first should
# be replaced with the second in the entire source code
def replace_matches(str1, str2):
    """TODO"""

# Given a source path and a destination, a symlink should
# be created
def create_symlink(src, dst):
    """TODO"""

# commands as a list of strings to be executed
def patch_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)
