import unittest
from NData.NMarkdown import NMarkdown


class TestNMarkdown(unittest.TestCase):
    def test_init(self):
        m = NMarkdown()

    def test_read_info(self):
        m = NMarkdown()
        m.read_info("gl.mk")
