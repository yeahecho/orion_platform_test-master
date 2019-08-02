import unittest
import requests
import sys
from nose import run
from htmloutput.htmloutput import HtmlOutput
import os
from time import gmtime, strftime
import orion_platform_test_library.generator_excel_format_test_report as excel_report

# if we need self-definition report in format excel, let self_definition_report equal True
# # attention: when the value is True, all of test case will be passed, although some case shall be fail,
# # so, all error of the fail case will be write into self-definition report
# # if you want all of the case test report( pass and fail ), let self_definition_report equal False
self_definition_report = False


class TestGetAccessTokenFromOrio(unittest.TestCase):
    report_data = []

    def setUp(self):
        self.url = "http://192.168.88.216:8080/orionboot/get_access_token"

        # test data: username and password
        self.valid_username = "mikesiwer01@gmail.com"
        self.valid_password = "a123456"

        self.invalid_username = ['mao@gmail.com', 'mao@@-----@@gmail.com', '@gmail.com', 'mao..@gmail.com',
                                 'mao..gmail.com']
        self.invalid_username_none = None
        self.invalid_password = ['1t54', '1111', 'ddddd', '123456', 'aabcde', 'abc123', '######$$$$%#@#',
                                 'ljsadflkjl(*&&^%%23123132',
                                 ';kjfdsalkjf;lksajfdlkjsalkfdjsakljfdlksajfdlksajdfk1219873287273987217398']
        self.invalid_password_none = None

        # data of the test report
        self.report_header = ['Test Steps', 'Test Data', 'Expected Result', 'Tested Result', 'Note']
        # get class name as report and sheet name, because class name is API test
        self.report_name = self.__class__.__name__
        self.report_sheet_name = self.__class__.__name__

    # @unittest.skip("to open")
    def test_get_access_token_with_valid_argument(self):
        headers = {'Content-Type': "application/json"}
        payload = {"userName": self.valid_username, "password": self.valid_password}

        response = requests.post(self.url, json=payload, headers=headers)
        # print(response.text)
        # self.assertIsNotNone(response.json()["access_token"])

        # for test report
        if self_definition_report:
            expection_result = "access token"
            test_result = response.json()["access_token"]
            test_data = str(payload)
            # status = 'pass'
            note = 'None'
            try:
                self.assertIsNotNone(test_result)
            except AssertionError as e:
                # status = 'unknown'
                note = response.text

            test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
            self.report_data.append(test_case_data)
        else:
            test_result = response.json()["access_token"]
            self.assertIsNotNone(test_result)

    # @unittest.skip("to open")
    def test_get_access_token_with_invalid_user_name(self):
        for index in range(len(self.invalid_username)):
            headers = {'Content-Type': "application/json"}
            payload = {"userName": self.invalid_username[index], "password": self.valid_password}

            response = requests.post(self.url, json=payload, headers=headers)
            # print(response.text)
            # self.assertIsNotNone(response.json()["access_token"])

            # for test report
            if self_definition_report:
                expection_result = None
                test_result = response.json()["access_token"]
                test_data = str(payload)
                # status = 'pass'
                note = 'None'
                try:
                    self.assertEqual(expection_result, test_result)
                except AssertionError as e:
                    # status = 'unknown'
                    note = response.text

                test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
                self.report_data.append(test_case_data)
            else:
                expection_result = None
                test_result = response.json()["access_token"]
                self.assertEqual(expection_result, test_result)

    # @unittest.skip("to open")
    def test_get_access_token_with_invalid_user_name_none(self):

        headers = {'Content-Type': "application/json"}
        payload = {"userName": self.invalid_username_none, "password": self.valid_password}

        response = requests.post(self.url, json=payload, headers=headers)
        print(response.text)
        # self.assertEqual(response.json()["Message"], "username required")

        # for test report
        if self_definition_report:
            expection_result = "username required"
            test_result = response.json()["Message"]
            test_data = str(payload)
            # status = 'pass'
            note = 'None'
            try:
                self.assertEqual(expection_result, test_result)
            except AssertionError as e:
                # status = 'unknown'
                note = response.text

            test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
            self.report_data.append(test_case_data)
        else:
            expection_result = "username required"
            test_result = response.json()["Message"]
            self.assertEqual(expection_result, test_result)

    # @unittest.skip("to open")
    def test_get_access_token_with_invalid_password(self):
        for index in range(len(self.invalid_password)):
            headers = {'Content-Type': "application/json"}
            payload = {"userName": self.valid_username, "password": self.invalid_password[index]}

            response = requests.post(self.url, json=payload, headers=headers)
            print(response.text)
            # self.assertIsNotNone(response.json()["access_token"])

            # for test report
            if self_definition_report:
                expection_result = None
                test_result = response.json()["access_token"]
                test_data = str(payload)
                # status = 'pass'
                note = 'None'
                try:
                    self.assertEqual(expection_result, test_result)
                except AssertionError as e:
                    # status = 'unknown'
                    note = response.text

                test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
                self.report_data.append(test_case_data)
            else:
                expection_result = None
                test_result = response.json()["access_token"]
                self.assertEqual(expection_result, test_result)

    # @unittest.skip("to open")
    def test_get_access_token_with_invalid_password_none(self):
        headers = {'Content-Type': "application/json"}
        payload = {"userName": self.valid_username, "password": self.invalid_password_none}

        response = requests.post(self.url, json=payload, headers=headers)
        print(response.text)
        self.assertEqual(response.json()["Message"], "password required")

        # for test report
        if self_definition_report:
            expection_result = "password required"
            test_result = response.json()["Message"]
            test_data = str(payload)
            # status = 'pass'
            note = 'None'
            try:
                self.assertEqual(expection_result, test_result)
            except AssertionError as e:
                # status = 'unknown'
                note = response.text

            test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
            self.report_data.append(test_case_data)
        else:
            expection_result = "password required"
            test_result = response.json()["Message"]
            self.assertEqual(expection_result, test_result)

    def tearDown(self):
        if self_definition_report:
            excel_report.generate_excel_format_test_report(self.report_header, self.report_data, self.report_name,
                                                           self.report_sheet_name)


if self_definition_report == False:
    # for generate normal report in html format
    path = os.path.dirname(__file__)
    outfile = os.path.join(path, __file__)
    report_file_name = '--html-out-file=./test_normal_report_format_html/' + __file__[36:-3] + strftime(
        "-%Y-%m-%d %H-%M",
        gmtime()) + '-report.html'
    run(argv=['nosetest', '-v', '--with-html-output', report_file_name, outfile],
        plugins=[HtmlOutput()])
    # report_file_name = __file__ + strftime("-%Y-%m-%d %H-%M", gmtime()) + '-report.html'
    # run(argv=['nosetest', '-v', '--with-html-output', '--html-out-file=' + report_file_name, outfile],
    #     plugins=[HtmlOutput()])
if __name__ == '__main__':
    unittest.main()
