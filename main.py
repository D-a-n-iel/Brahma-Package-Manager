import sys
from src import parse
from src import fetch
from src import patch
from src import build
from src import install
from src import utils


def install_package(definition):
    print(definition)
    if "source" in definition:
        try:
            source = definition["source"]
            if "http-get" in source:
                http = source["http-get"]
                if "hash" in http:
                    fetch.http_download(http["url"], http["hash"])
                else:
                    print(
                        """Warning: Fetching source with HTTP
                        but not verifying integrity with hash"""
                    )
                    fetch.http_download(http["url"])

            elif "git-fetch" in source:
                git = source["git-fetch"]
                if "branch" in git:
                    fetch.git_fetch(git["url"], git["branch"])
                else:
                    fetch.git_fetch(git["url"])
        except KeyError:
            sys.exit("Error: malformed source section")

    if "patch" in definition:
        """TODO apply patches to source"""

    if "build" in definition:
        """TODO build"""

    if "install" in definition:
        """TODO install"""


if __name__ == "__main__":
    # Program should be run with a config filename as argument
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "[CONFIG_NAME]")
        sys.exit("Error: incorrect usage")

    path_to_config = utils.find_in_sys_path(sys.argv[1])
    config = parse.get_config(path_to_config)

    if "package" in config:
        install_stack = utils.dependency_bfs(config)
        while install_stack:
            install_package(install_stack.pop()["package"]["definition"])
    else:
        """TODO handle system case"""
