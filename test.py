import unittest
from main import add, sub, mul, div

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertNotEqual(add(3, 7), 9)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertNotEqual(sub(3, 7), 4)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50)
        self.assertNotEqual(mul(3, 7), 20)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)
        self.assertNotEqual(div(21, 7), 5)


if __name__ == '__main__':
    unittest.main()