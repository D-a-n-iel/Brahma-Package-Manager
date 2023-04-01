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
        test_file_path = os.path.join(test_path, "hello_world.json")
        with utils.cd(test_path):
            config = parse.get_config(test_file_path)
            self.assertTrue(config["package"]["name"] == "hello")


# These are wrapper functions to widely used and tested python
# libraries, what is being tested here is not their correctness,
# but the wrapper functions'. ensuring their output is located in the
# expected path.
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

    def test_git_fetch(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            dir_name = fetch.git_fetch(
                "https://github.com/DDAVID22291/Brahma-Package-Manager"
            )
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


class UtilsTests(unittest.TestCase):
    def test_cd(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        with utils.cd(test_path):
            self.assertEqual(os.getcwd(), test_path)

    def test_find_in_sys_path_full_path(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_file = "hello_world.json"
        with utils.cd(test_path):
            utils.find_in_sys_path(os.path.join(test_path, test_file))

    def test_find_in_sys_path_name(self):
        test_path = os.path.dirname(os.path.realpath(__file__))
        test_file = "hello_world.json"
        with utils.cd(test_path):
            self.assertEqual(utils.find_in_sys_path("hello_world"), "./" + test_file)


if __name__ == "__main__":
    unittest.main()
