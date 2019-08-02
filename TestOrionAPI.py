__author__ = 'mike'

import unittest
from HTML import HTMLStyle
from test_get_access_token import TestGetAccessToken
from test_create_order import TestGetOderId
from test_get_user_profile import TestGetWalletId
from test_pay_to_leger import TestGetTaskId
from test_upload_and_submit_task import TestUploadScript


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([

            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetAccessToken),

            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetOderId),

            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetWalletId),

            unittest.defaultTestLoader.loadTestsFromTestCase(TestGetTaskId),

            unittest.defaultTestLoader.loadTestsFromTestCase(TestUploadScript),
        ])

        outfile = open("TestReport_API/TestReport_OrionAPI.html", "w")

        runner1 = HTMLStyle(
            stream=outfile,
            title='API Test Report',
            description='Orion API Tests'
        )

        runner1.run(smoke_test)


if __name__ == '__main__':
    unittest.main()
