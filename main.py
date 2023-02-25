import sys
from src import parse
from src import fetch
from src import patch
from src import build
from src import install


if __name__ == "__main__":
    # Program should be run with a config file as argument
    if len(sys.argv) != 2:
        print("Usage: python", sys.argv[0], "[FILE]")
        sys.exit("Error: incorrect usage")

    # config_file = open(sys.argv[1], "r")
    # config = parse.parse_config(config_file)
    # config_file.close()

    # source = config["package"]["definition"]["source"]
    # fetch.http_download(source["http-get"], source["hash"])
