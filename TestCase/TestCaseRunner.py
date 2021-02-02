import unittest
from TestCase.CalcTestCase import CalcTestCase

if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(CalcTestCase('test_1_minus_5'))

    runner = unittest.TextTestRunner()
    runner.run(suite)