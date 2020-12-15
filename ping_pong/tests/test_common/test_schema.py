import unittest

from common.schema import is_digit_valid


class TestIsDigitValid(unittest.TestCase):
    def test_gt_10(self):
        self.assertEqual(
            is_digit_valid(11),
            True,
        )

    def test_eq_10(self):
        self.assertEqual(
            is_digit_valid(10),
            True,
        )

    def test_lt_10_divisible_by_3(self):
        self.assertEqual(
            is_digit_valid(9),
            False,
        )

    def test_gt_10_divisible_by_3(self):
        self.assertEqual(
            is_digit_valid(12),
            True,
        )
