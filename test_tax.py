import unittest

from tax import include_tax


class TestTax(unittest.TestCase):
    def test_100円の税込み金額は108円(self):
        self.assertEqual(include_tax(100), 108)

    def test_128円の税込み金額は138円(self):
        self.assertEqual(include_tax(128), 138)

if __name__ == '__main__':
    unittest.main()
