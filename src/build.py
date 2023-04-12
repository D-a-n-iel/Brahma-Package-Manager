import subprocess
import os
import sys


def run_gnu_build_system(prefix=None):
    autotools_commands = []
    if os.path.isfile("configure"):
        if not prefix:
            autotools_commands.append("./configure")
        else:
            os.mkdir(prefix)
            if "/" not in prefix:
                prefix = os.path.join(os.getcwd(), prefix)
            autotools_commands.append("./configure --prefix=" + prefix)

    autotools_commands.append("make")

    for command in autotools_commands:
        subprocess.run(command, shell=True)


# commands as a list of strings to be executed
def run_build_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)
