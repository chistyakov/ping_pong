import unittest

from base import anything
from service_a.core import append_new_digit


class TestAppendNewDigit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(append_new_digit([]), [anything])

    def test_none_list(self):
        self.assertEqual(append_new_digit(None), [anything])

    def test_single_item_list(self):
        self.assertEqual(append_new_digit([1]), [1, anything])
