# -*- coding:utf-8 -*-

import unittest
from demo.Calc import Calc as c

class CalcTestCase(unittest.TestCase):

    def test_2_add_2(self):
        print("test_2_add_2")
        self.assertEqual(4,c.add(2,2))

    def test_1_add_0(self):
        print("test_1_add_0")
        self.assertEqual(1,c.add(1,0))

    def test_1_minus_5(self):
        print("test_1_minus_5")
        self.assertEqual(-4,c.minus(1,5))

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(CalcTestCase('test_1_minus_5'))

    runner = unittest.TextTestRunner()
    runner.run(suite)