import subprocess
import os
import sys


def run_gnu_build_system():
    autotools_commands = []
    if os.path.isfile("configure"):
        autotools_commands.append("./configure")
    autotools_commands.append("make")

    for command in autotools_commands:
        subprocess.run(command, shell=True)


# commands as a list of strings to be executed
def run_build_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)
