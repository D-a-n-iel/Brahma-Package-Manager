import unittest
import os
import sys
from shutil import rmtree

sys.path.append(".")

from src import parse
from src import fetch
from src import patch
from src import build
from src import install
from src import utils


class ParseTests(unittest.TestCase):
    def test_parse_config(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            config_file = open("hello_world.json", "r")
            config = parse.parse_config(config_file)
            config_file.close()
            self.assertTrue(config["package"]["name"] == "hello")


class FetchTests(unittest.TestCase):
    def test_http_download(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            file_name = fetch.http_download(
                "https://ftp.gnu.org/gnu/hello/hello-2.12.tar.gz"
            )
            self.assertTrue(os.path.isfile(file_name))

            # cleanup
            os.remove(file_name)

    def test_extract(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            dir_name = fetch.extract("test_archive.tar.gz")
            self.assertTrue(os.path.isdir(dir_name))

            # cleanup
            rmtree(dir_name)


class PatchTests(unittest.TestCase):
    """TODO"""


class BuildTests(unittest.TestCase):
    """TODO"""


class InstallTests(unittest.TestCase):
    def test_file_copy(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            file_name = ["hello_world.json"]
            copied_dest = "new_directory"
            install.file_copy(file_name, copied_dest)
            self.assertTrue(os.path.isdir(copied_dest))
            self.assertTrue(os.path.isfile(os.path.join(copied_dest, file_name[0])))

            # cleanup
            rmtree(copied_dest)

    def test_file_copy_multiple(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            file_names = ["hello_world.json", "test_archive.tar.gz"]
            copied_dest = "new_directory"
            install.file_copy(file_names, copied_dest)
            self.assertTrue(os.path.isdir(copied_dest))
            for file_name in file_names:
                self.assertTrue(os.path.isfile(os.path.join(copied_dest, file_name)))

            # cleanup
            rmtree(copied_dest)


if __name__ == "__main__":
    unittest.main()
