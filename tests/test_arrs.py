import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], 0, "test"), "test")  # Новый тест
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")  # Новый тест 2


    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([], 0), [])  # Новый тест 3
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])  # Новый тест 4
        self.assertEqual(arrs.my_slice([1, 2, 3], 0, -1), [1, 2])  # Новый тест 5
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, -1), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -5), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], -2), [2, 3])
