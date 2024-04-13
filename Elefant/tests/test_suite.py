import unittest

import HtmlTestRunner

from Elefant.tests.test_home_page import TestHomePage
from Elefant.tests.test_negative_login import TestNegativeLogin
from Elefant.tests.test_positive_login import TestPositiveLogin
from Elefant.tests.test_search_page import TestSearchPage

class TestElefantSuite(unittest.TestCase):

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHomePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestSearchPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestPositiveLogin),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestNegativeLogin)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title="Elefant Tests Report",
            report_name="Test Results"
        )

        runner.run(test_suite)
