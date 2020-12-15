import unittest

from common.url import build_url


class TestBuildUrl(unittest.TestCase):
    def test_no_slashes(self):
        self.assertEqual(
            build_url(base_url="https://example.com", path="foobar"),
            "https://example.com/foobar",
        )

    def test_tailing_slash_base_url(self):
        self.assertEqual(
            build_url(base_url="https://example.com/", path="foobar"),
            "https://example.com/foobar",
        )

    def test_leading_slash_path(self):
        self.assertEqual(
            build_url(base_url="https://example.com/", path="foobar"),
            "https://example.com/foobar",
        )
