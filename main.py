import sys
from src import parse
from src import fetch
from src import patch
from src import build
from src import install
from src import utils


def fetching_step(source):
    try:
        if "http-get" in source:
            http = source["http-get"]
            if "hash" in http:
                archive_name = fetch.http_download(http["url"], http["hash"])
                return fetch.extract(archive_name)
            else:
                print(
                    """Warning: Fetching source with HTTP
                    but not verifying integrity with hash"""
                )
                archive_name = fetch.http_download(http["url"])
                return fetch.extract(archive_name)

        elif "git-fetch" in source:
            git = source["git-fetch"]
            if "branch" in git:
                return fetch.git_fetch(git["url"], git["branch"])
            else:
                return fetch.git_fetch(git["url"])
    except KeyError:
        sys.exit("Error: malformed source section")


def building_step(build_proc, build_dir):
    try:
        with utils.cd(build_dir):
            if "system" in build_proc:
                system = build_proc["system"]
                if system == "gnu_build_system":
                    print(build_proc)
                    if "prefix" in build_proc:
                        build.run_gnu_build_system(build_proc["prefix"])
                    else:
                        build.run_gnu_build_system()

            if "commands" in build_proc:
                commands = build_proc["commands"]
                build.run_build_commands(commands)
    except KeyError:
        sys.exit("Error: malformed build section")


def install_package(definition):
    if "source" in definition:
        build_dir = fetching_step(definition["source"])

    if "patch" in definition:
        """TODO apply patches to source"""

    if "build" in definition:
        building_step(definition["build"], build_dir)

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
