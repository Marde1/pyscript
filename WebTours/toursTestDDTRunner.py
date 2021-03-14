# -*- conding:utf-8 -*-

import unittest
import HTMLTestRunnerNew
from WebTours.TestCaseDDT import TestCaseDDT

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTest(loader.loadTestsFromTestCase(TestCaseDDT))

