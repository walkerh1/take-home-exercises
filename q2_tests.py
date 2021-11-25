import unittest
from q2 import max_money


class TestMaxMoney(unittest.TestCase):

    def test_small_n_and_k(self):
        self.assertEqual(max_money(3,3), 5)
        self.assertEqual(max_money(2,1), 2)
        self.assertEqual(max_money(100,21), 5049)
        self.assertEqual(max_money(100,20), 5050)

    def test_large_n_and_k(self):
        self.assertEqual(max_money(80000, 3200040000), 200039978)

    def test_lower_bound_n_and_k(self):
        self.assertEqual(max_money(1,1), 0)

    def test_upper_bound_n_and_k(self):
        self.assertEqual(max_money(2*(10**9), 4*(10**15)), 91)


if __name__ == '__main__':
    unittest.main()
