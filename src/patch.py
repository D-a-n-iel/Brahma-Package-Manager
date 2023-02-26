import subprocess


# commands as a list of strings to be executed
def apply_patches(commands):
    for command in commands:
        subprocess.run(command, shell=True)
