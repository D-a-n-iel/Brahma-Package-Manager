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
                utils.warning(
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
        utils.error("malformed source section")


def patching_step(patch_steps, patch_dir):
    try:
        with utils.cd(patch_dir):
            if "replace-matches" in patch_steps:
                for x in patch_steps["replace-matches"]:
                    patch.replace_matches(patch_dir, x["str1"], x["str2"])
            if "create-symlinks" in patch_steps:
                for x in patch_steps["replace-matches"]:
                    patch.create_symlink(x["src"], x["dst"])
            if "commands" in patch_steps:
                patch.patch_commands(patch_steps["commands"])
    except KeyError:
        utils.error("Error: malformed patch section")


def building_step(build_steps, build_dir):
    try:
        with utils.cd(build_dir):
            if "system" in build_steps:
                system = build_steps["system"]
                if system == "gnu_build_system":
                    print(build_steps)
                    if "prefix" in build_steps:
                        build.run_gnu_build_system(build_steps["prefix"])
                    else:
                        build.run_gnu_build_system()

            if "commands" in build_steps:
                commands = build_steps["commands"]
                build.run_build_commands(commands)
    except KeyError:
        utils.error("Error: malformed build section")


def install_package(definition):
    if "source" in definition:
        src_dir = fetching_step(definition["source"])

    if "patch" in definition:
        patching_step(definition["patch"], src_dir)

    if "build" in definition:
        building_step(definition["build"], src_dir)

    if "install" in definition:
        """TODO install"""


if __name__ == "__main__":
    # Program should be run with a config filename as argument
    argv = sys.argv
    if len(argv) == 2:
        config_arg = argv[1]
        service_operation = None
    elif len(argv) == 4:
        config_arg = argv[3]
        service_operation = argv[2]
    else:
        utils.error(
            "incorrect usage",
            f"Usage:\tpython {argv[0]} [config]\n"
            f"\tpython {argv[0]} service [start|stop|restart] [config]",
        )

    path_to_config = utils.find_in_sys_path(config_arg)
    config = parse.get_config(path_to_config)

    if service_operation:
        service = config["package"]["definition"].get("service", [])
        try:
            if service_operation == "start":
                service.service_commands(service["start_commands"])
            elif service_operation == "stop":
                service.service_commands(service["stop_commands"])
            elif service_operation == "restart":
                service.service_commands(service["start_commands"])
                service.service_commands(service["stop_commands"])
            else:
                utils.error(
                    f"unknown service operation {service_operation}",
                    "Available options: [start|stop|restart]",
                )
        except KeyError:
            utils.error(
                f"failed to run service operation {service_operation}",
                "Fields missing from configuration file",
            )

    else:
        if "package" in config:
            install_stack = utils.dependency_bfs(config)
            while install_stack:
                install_package(install_stack.pop()["package"]["definition"])
        else:
            """TODO handle system case"""
