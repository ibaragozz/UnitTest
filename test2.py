import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_sub(self):
        self.assertEqual(3 - 2, 1)

if __name__ == '__main__':
    unittest.test2()