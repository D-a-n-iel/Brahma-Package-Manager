import json


def get_config(path_to_config):
    config_file = open(path_to_config, "r")
    config = parse_config(config_file)
    config_file.close()
    return config


def parse_config(config):
    return json.load(config)
