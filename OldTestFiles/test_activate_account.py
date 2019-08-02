import unittest
import requests
import json
import sys
from xeger import Xeger
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


class TestActivateAccount(unittest.TestCase):
    report_data = []

    def get_register_response(self):
        url = "http://192.168.88.216:8080/orionboot/keycloak_user"
        valid_email_address = Xeger(limit=8).xeger(r'test[.][a-z]+[.][0-9]+@[a-z]{4}[.]com')
        valid_password = Xeger(limit=8).xeger(r'[a-z]{3}[0-9]+')
        first_name = Xeger(limit=8).xeger(r'[a-z]+')
        last_name = Xeger(limit=8).xeger(r'[a-z]+')

        headers = {'Content-Type': "application/json"}
        payload = {
            "email": valid_email_address,
            "firstName": first_name,
            "lastName": last_name,
            "credentials": [
                {
                    "value": valid_password
                }
            ]
        }
        print(valid_email_address)
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return response

    def setUp(self):
        # url
        self.url = "http://192.168.88.216:8080/orionboot/customer/activate"

        # test data: activate code and user id
        register_response = TestActivateAccount().get_register_response()
        self.valid_user_id = register_response.json()["id"]
        self.valid_activate_code = register_response.json()["activateCode"]

        # test data: invalid activate code
        self.invalid_activate_code = ['kkk', '1234', '#$@']

        # test data: invalid user id
        self.invalid_user_id_character = ['xi', '1234', '@#$@#$@']
        self.invalid_user_id_integer_number = [87777, -87777, 0]
        self.invalid_user_id_float_number = [12.34, -12.34]

        # data of the test report
        # self.report_data = []
        # format of the test report
        # self.report_header = ['Test Case#', 'Test Title', 'Test Summary', 'Test Steps', 'Test Data', 'Expected Result',
        #                       'Tested Result', 'Status', 'Note']
        self.report_header = ['Test Steps', 'Test Data', 'Expected Result', 'Tested Result', 'Note']
        # get class name as report and sheet name, because class name is API test
        self.report_name = self.__class__.__name__
        self.report_sheet_name = self.__class__.__name__

    # @unittest.skip(" to open ")
    def test_activate_account_with_valid_arguments(self):
        querystring = {"activateCode": self.valid_activate_code, "id": self.valid_user_id}
        payload = ""
        headers = {}

        response = requests.get(self.url, data=payload, headers=headers, params=querystring)
        # print(response.text)
        # self.assertEqual(response.json()["message"], "Success")

        if self_definition_report:
            # for test report
            expection_result = "Success"
            test_result = response.json()["message"]
            test_data = str(querystring)
            # status = 'pass'
            note = 'None'
            try:
                self.assertEqual(test_result, expection_result)
            except AssertionError as e:
                # status = 'unknown'
                note = response.text

            test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
            self.report_data.append(test_case_data)

        else:
            expection_result = "Success"
            test_result = response.json()["message"]
            self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to open ")
    def test_activate_account_with_invalid_activate_code(self):
        for index in range(len(self.invalid_activate_code)):
            querystring = {"activateCode": self.invalid_activate_code[index], "id": self.valid_user_id}
            payload = ""
            headers = {}

            response = requests.get(self.url, data=payload, headers=headers, params=querystring)
            # print(response.text)
            # self.assertEqual(response.text, "failed to activate account")


            # for test report
            if self_definition_report:
                expection_result = "failed to activate account"
                test_result = response.text
                test_data = str(querystring)
                # status = 'pass'
                note = 'None'
                try:
                    self.assertEqual(test_result, expection_result)
                except AssertionError as e:
                    # status = 'unknown'
                    note = response.text

                test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
                self.report_data.append(test_case_data)
            else:
                expection_result = "failed to activate account"
                test_result = response.text
                self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to do: return html 400 ")
    def test_activate_account_with_invalid_user_id_by_character(self):
        for index in range(len(self.invalid_user_id_character)):
            querystring = {"activateCode": self.valid_activate_code[index], "id": self.invalid_user_id_character}
            payload = ""
            headers = {}

            response = requests.get(self.url, data=payload, headers=headers, params=querystring)
            # print(response.text)
            # print(response.status_code)
            # self.assertEqual(response.status_code, 400)


            # for test report
            if self_definition_report:
                expection_result = "failed to activate account"
                test_result = response.text
                test_data = str(querystring)
                # status = 'pass'
                note = 'None'
                try:
                    self.assertEqual(test_result, expection_result)
                except AssertionError as e:
                    # status = 'unknown'
                    note = response.text

                test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
                self.report_data.append(test_case_data)
            else:
                expection_result = "failed to activate account"
                test_result = response.text
                self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to open")
    def test_activate_account_with_invalid_user_id_by_integer_number(self):
        for index in range(len(self.invalid_user_id_integer_number)):
            querystring = {"activateCode": self.valid_activate_code, "id": self.invalid_user_id_integer_number[index]}
            payload = ""
            headers = {}

            response = requests.get(self.url, data=payload, headers=headers, params=querystring)
            # print(response.text)
            # print(response.status_code)
            # self.assertEqual(response.json()["Exception"], "java.lang.NullPointerException")


            # for test report
            if self_definition_report:
                expection_result = "failed to activate account"
                test_result = response.json()["Exception"]
                test_data = str(querystring)
                # status = 'pass'
                note = 'None'
                try:
                    self.assertEqual(test_result, expection_result)
                except AssertionError as e:
                    # status = 'unknown'
                    note = str(e) + ':' + 'test response:' + response.text

                test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
                self.report_data.append(test_case_data)
            else:
                expection_result = "failed to activate account"
                test_result = response.json()["Exception"]
                self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to do: return html 400 ")
    def test_activate_account_with_invalid_user_id_by_float_number(self):
        for index in range(len(self.invalid_user_id_float_number)):
            querystring = {"activateCode": self.valid_activate_code, "id": self.invalid_user_id_float_number[index]}
            payload = ""
            headers = {}

            response = requests.get(self.url, data=payload, headers=headers, params=querystring)
            # print(response.text)
            # print(response.status_code)
            # self.assertEqual(response.status_code, 400)


            # for test report
            if self_definition_report:
                expection_result = "failed to activate account"
                test_result = response.text
                test_data = str(querystring)
                # status = 'pass'
                note = 'None'
                try:
                    self.assertEqual(test_result, expection_result)
                except AssertionError as e:
                    # status = 'unknown'
                    note = response.text

                test_case_data = [sys._getframe().f_code.co_name + "()", test_data, expection_result, test_result, note]
                self.report_data.append(test_case_data)
            else:
                expection_result = "failed to activate account"
                test_result = response.text
                self.assertEqual(test_result, expection_result)

    def tearDown(self):
        # pass
        # print(self.report_data)
        if self_definition_report:
            excel_report.generate_excel_format_test_report(self.report_header, self.report_data,
                                                       self.report_name, self.report_sheet_name)


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

