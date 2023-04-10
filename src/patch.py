import subprocess
import os


def replace_matches(src_dir, str1, str2):
    for root, _, names in os.walk(src_dir):
        for name in names:
            path = os.path.join(root, name)
            text = open(path).read()
            if str1 in text:
                open(path, "w").write(text.replace(str1, str2))


def create_symlink(src, dst):
    os.symlink(src, dst)


# commands as a list of strings to be executed
def patch_commands(commands):
    for command in commands:
        subprocess.run(command, shell=True)
