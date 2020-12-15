import unittest

from service_b.core import get_avg_min_max


class TestGetAvgMinMax(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(get_avg_min_max([]), (None, None, None))

    def test_none_list(self):
        self.assertEqual(get_avg_min_max(None), (None, None, None))

    def test_single_item_list(self):
        self.assertEqual(get_avg_min_max([1]), (1, 1, 1))

    def test_two_items(self):
        self.assertEqual(get_avg_min_max([2, 1]), (1.5, 1, 2))

    def test_three_items(self):
        self.assertEqual(get_avg_min_max([2, 1, 2]), (1.6666666666666667, 1, 2))
