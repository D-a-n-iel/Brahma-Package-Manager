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
