import os
from src import parse
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
    if os.path.isfile(name):
        return name

    for files in os.listdir("."):
        if name + ".json" in files:
            return os.path.join(".", name + ".json")

    config_path = os.path.join(os.environ["XDG_CONFIG_HOME"], "brahma-configs")
    for root, _, files in os.walk(config_path):
        if name + ".json" in files:
            return os.path.join(root, name + ".json")


# TODO: modify BFS to re-append previously visited nodes
def dependency_bfs(config):
    config_list = []

    def bfs(visited, package):
        visited.append(package["package"]["name"])
        queue = []
        queue.append(package)

        while queue:
            current = queue.pop(0)
            config_list.append(current)

            for dep in current["package"]["definition"].get("depends", []):
                if dep not in visited:
                    visited.append(dep)
                    queue.append(parse.get_config(find_in_sys_path(dep)))

    bfs([], config)
    return config_list
