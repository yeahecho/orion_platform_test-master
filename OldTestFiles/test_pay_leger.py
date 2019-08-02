import unittest
import requests
from xeger import Xeger
import sys
from nose import run
from htmloutput.htmloutput import HtmlOutput
import os
from time import gmtime, strftime
from OldTestFiles.base_api import BaseApi
import orion_platform_test_library.generator_excel_format_test_report as excel_report

# if we need self-definition report in format excel, let self_definition_report equal True
# # attention: when the value is True, all of test case will be passed, although some case shall be fail,
# # so, all error of the fail case will be write into self-definition report
# # if you want all of the case test report( pass and fail ), let self_definition_report equal False
self_definition_report = False


class TestPayToLeger(unittest.TestCase):
    report_data = []

    def setUp(self):
        base_api = BaseApi()
        # url
        self.url = "http://192.168.88.216:8080/orionboot/orionPay"
        # test data
        # # test data: access_token
        self.valid_token = base_api.get_token()
        self.invalid_token = []
        self.invalid_token.append(Xeger(limit=100).xeger(r'[a-z]+[A-Z]+[0-9]'))
        self.invalid_token.append(Xeger(limit=10).xeger(r'[a-z]+[A-Z]+[0-9]'))
        self.order_id = base_api.get_order_id(self.valid_token)
        self.order_id_invalid = 2000
        self.wallet_address = base_api.get_wallet_address(self.valid_token)
        self.wallet_address_invalid = "oxfweqrqwerqwrqwrqw"

        # data of the test report
        self.report_header = ['Test Steps', 'Test Data', 'Expected Result', 'Tested Result', 'Note']
        # get class name as report and sheet name, because class name is API test
        self.report_name = self.__class__.__name__
        self.report_sheet_name = self.__class__.__name__

    def test_pay_leger_success(self):
        payload = {
            "orderId": self.order_id,
            "subtotal": "1234",
            "walletAddress": self.wallet_address,
            "ledgerIp": "192.168.88.152:8080",
            "paymentType": 5
        }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.valid_token,
            'cache-control': "no-cache",
            'Postman-Token': "6b9c58cd-e123-49ef-99dd-9be76b0ba650"
        }

        response = requests.request("POST", self.url, json=payload, headers=headers)
        # print(response.json())
        result = response.json()['payment']['resource']
        # self.assertEqual(result, 'payment')

        # for test report
        if self_definition_report:
            expection_result = 'payment'
            test_result = result
            test_data = str(payload)
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
            expection_result = 'payment'
            test_result = result
            self.assertEqual(test_result, expection_result)

    def test_pay_leger_invalid_token(self):
        for index in range(len(self.invalid_token)):
            payload = {
                "orderId": self.order_id,
                "subtotal": "1234",
                "walletAddress": self.wallet_address,
                "ledgerIp": "192.168.88.152:8080",
                "paymentType": 5
            }
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + self.invalid_token[index],
                'cache-control': "no-cache",
                'Postman-Token': "6b9c58cd-e123-49ef-99dd-9be76b0ba650"
            }

            response = requests.request("POST", self.url, json=payload, headers=headers)
            status_code = response.status_code
            # self.assertEqual(status_code, 401)

            # for test report
            if self_definition_report:
                expection_result = 'unauthorization'
                test_result = status_code
                test_data = str(payload)
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
                expection_result = 'unauthorization'
                test_result = status_code
                self.assertEqual(test_result, expection_result)

    def test_pay_leger_invalid_order_id(self):
        payload = {
            "orderId": self.order_id_invalid,
            "subtotal": "1234",
            "walletAddress": self.wallet_address,
            "ledgerIp": "192.168.88.152:8080",
            "paymentType": 5
        }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.valid_token,
            'cache-control': "no-cache",
            'Postman-Token': "6b9c58cd-e123-49ef-99dd-9be76b0ba650"
        }

        response = requests.request("POST", self.url, json=payload, headers=headers)
        status_code = response.status_code
        # self.assertEqual(status_code, 200)

        # for test report
        if self_definition_report:
            expection_result = 'order id invalid'
            test_result = status_code
            test_data = str(payload)
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
            expection_result = 'order id invalid'
            test_result = status_code
            self.assertEqual(test_result, expection_result)

    def test_pay_leger_wrong_wallet_address(self):
        payload = {
            "orderId": self.order_id,
            "subtotal": "1234",
            "walletAddress": self.wallet_address_invalid,
            "ledgerIp": "192.168.88.152:8080",
            "paymentType": 5
        }
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.valid_token,
            'cache-control': "no-cache",
            'Postman-Token': "6b9c58cd-e123-49ef-99dd-9be76b0ba650"
        }

        response = requests.request("POST", self.url, json=payload, headers=headers)
        status_code = response.status_code
        # self.assertEqual(status_code, 200)

        # for test report
        if self_definition_report:
            expection_result = 'wrong wallet address'
            test_result = status_code
            test_data = str(payload)
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
            expection_result = 'wrong wallet address'
            test_result = status_code
            self.assertEqual(test_result, expection_result)

    def tearDown(self):
        if self_definition_report:
            excel_report.generate_excel_format_test_report(self.report_header, self.report_data, self.report_name,
                                                       self.report_sheet_name)


# for generate normal report in html format
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
