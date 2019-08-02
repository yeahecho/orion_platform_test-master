__author__ = 'mike'

import unittest

from TestOrionAPI.HTML import HTMLStyle
from TestOrionAPI.test_get_access_token import TestGetAccessToken
from TestOrionAPI.test_create_order import TestGetOderId
from TestOrionAPI.test_get_user_profile import TestGetWalletId
from TestOrionAPI.test_pay_to_leger import TestGetTaskId
from TestOrionAPI.test_upload_and_submit_task import TestUploadScript


class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([

            unittest.defaultTestLoader.loadTestsFromTestCase(
                TestOrionAPI.test_get_access_token.TestGetAccessToken),

            unittest.defaultTestLoader.loadTestsFromTestCase(
                TestOrionAPI.test_create_order.TestGetOderId),

            unittest.defaultTestLoader.loadTestsFromTestCase(
                TestOrionAPI.test_get_user_profile.TestGetWalletId),

            unittest.defaultTestLoader.loadTestsFromTestCase(
                TestOrionAPI.test_pay_to_leger.TestGetTaskId),

            unittest.defaultTestLoader.loadTestsFromTestCase(
                TestOrionAPI.test_upload_and_submit_task.TestUploadScript),
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
