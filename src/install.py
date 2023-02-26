import subprocess


# commands as a list of strings to be executed
def install_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)
