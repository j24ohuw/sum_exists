import unittest
from coding_challenge import sum_exists


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.arr_1 = [i for i in range(1, 5)]
        self.arr_2 = [-1, 1]

    def test_case_1(self):
        self.assertFalse(sum_exists(self.arr_1, 1))

    def test_case_2(self):
        self.assertTrue(sum_exists(self.arr_1, 5))

    def test_case_3(self):
        self.assertFalse(sum_exists(self.arr_2, 2))

    def test_case_4(self):
        self.assertTrue(sum_exists([1, 1], 2))

    def test_case_5(self):
        self.assertRaises(ValueError, sum_exists, [''], 0)

    def test_case_6(self):
        self.assertTrue(sum_exists([-1, 1], 0))

    def test_case_7(self):
        self.assertTrue(sum_exists([2, 4, 7, -3, 5, 1000000000000], 1000000000000 -3))

    def test_case_8(self):
        self.assertTrue(sum_exists([2, 4, 7, -3, 5, 1000000000000], 1000000000000 + 5))


if __name__ == '__main__':
    unittest.main()
