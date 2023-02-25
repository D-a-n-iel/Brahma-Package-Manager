import unittest
import os
import sys

sys.path.append(".")

from src import parse
from src import fetch
from src import patch
from src import build
from src import install


class UnitTests(unittest.TestCase):
    def test_http_download(self):
        file_name = fetch.http_download(
            "https://ftp.gnu.org/gnu/hello/hello-2.12.tar.gz"
        )
        self.assertTrue(os.path.isfile(file_name))

        # cleanup
        os.remove(file_name)


if __name__ == "__main__":
    unittest.main()
