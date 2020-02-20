import unittest

import unittest_pow


class test(unittest.TestCase):
    def testAssert(self):
        self.assertEqual(unittest_pow.pow(2, 3), 8)
        self.assertEqual(unittest_pow.pow(4, 2), 16)
        self.assertEqual(unittest_pow.pow(2, 0), 1)
        self.assertEqual(unittest_pow.pow(123456789, 0), 1)
    def testErrors(self):
        self.assertRaises(ValueError, unittest_pow.pow, "a", 2)
        self.assertRaises(ValueError, unittest_pow.pow, 2, "a")

if __name__ == "__main__":
    unittest.main()