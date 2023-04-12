import subprocess


# commands as a list of strings to be executed
def service_commands(commands):
    for command in commands:
        subprocess.run(command, start_new_session=True)
