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


if __name__ == "__main__":
    unittest.main()
