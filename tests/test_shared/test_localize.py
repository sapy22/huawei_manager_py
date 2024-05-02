import unittest
from src.shared.localize import lc_col




class TestLocalize(unittest.TestCase):
    def test_col_0(self):
        self.assertEqual(lc_col(3, 0), 2)
    
    def test_col_1(self):
        self.assertEqual(lc_col(3, 1), 1)

    def test_col_2(self):
        self.assertEqual(lc_col(3, 2), 0)
    


if __name__ == '__main__':
    unittest.main()