import sys
from src import parse
from src import fetch
from src import patch
from src import build
from src import install


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
    # Program should be run with a config file as argument
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "[FILE]")
        sys.exit("Error: incorrect usage")

    config_file = open(sys.argv[1], "r")
    config = parse.parse_config(config_file)
    config_file.close()

    if "package" in config:
        install_package(config["package"]["definition"])
    else:
        """TODO handle system and service cases"""
