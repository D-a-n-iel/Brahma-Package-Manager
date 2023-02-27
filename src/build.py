import subprocess

# ./configure; make; make install
def run_gnu_build_system():
    """TODO"""


# commands as a list of strings to be executed
def run_build_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)
