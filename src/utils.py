import os
from contextlib import contextmanager


# allows using a with block to operate in some path
@contextmanager
def cd(path):
    previous_path = os.getcwd()
    os.chdir(os.path.expanduser(path))
    try:
        yield
    finally:
        os.chdir(previous_path)


def find_in_sys_path(name):
    for files in os.listdir("."):
        if name in files:
            return os.path.join(".", name)

    sys_search_paths = os.environ["XDG_CONFIG_HOME"].split(":")
    for sys_path in sys_search_paths:
        for root, _, files in os.walk(sys_path):
            if name in files:
                return os.path.join(root, name)
