import unittest
import unittest_pow as userPow

class mainTest(unittest.TestCase):
    def testValue(self):
        self.assertEqual(userPow.pow(2, 5), 32)
        self.assertEqual(userPow.pow(2, 2), 4)
        self.assertEqual(userPow.pow(5, 2), 25)
    def testErrors(self):
        self.assertRaises(ValueError, userPow.pow, 'a', 2)
        self.assertRaises(ValueError, userPow.pow, 2, 'a')
    
if __name__ == "__main__":
    unittest.main()