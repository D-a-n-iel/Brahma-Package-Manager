import sys
import os
from src import parse
from src import fetch
from src import patch
from src import build
from src import install
from src import utils


def install_package(definition):
    if "source" in definition:
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
            fetch.git_fetch(git["url"])

        else:
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

    path_to_config = utils.find_in_sys_path(sys.argv[1] + ".json")
    config_file = open(path_to_config, "r")
    config = parse.parse_config(config_file)
    config_file.close()

    if "package" in config:
        definition = config["package"]["definition"]
        # TODO: Make queue from DFS search of dependency graph
        install_package(definition)
    else:
        """TODO handle system and service cases"""
