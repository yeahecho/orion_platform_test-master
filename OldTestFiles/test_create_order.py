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


class TestCreateOrder(unittest.TestCase):
    report_data = []

    def setUp(self):
        base_api = BaseApi()
        self.url = "http://192.168.88.216:8080/orionboot/orders/create"
        self.access_token = base_api.get_token()
        self.acce_token_wrong = "yJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiw"
        base_api = BaseApi()
        # test data
        # # test data: access_token
        self.valid_token = base_api.get_token()
        self.invalid_used_token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJrLW95WTVHcG54Um1mcVdGUlFwZWtTaDBiN1N2T0hnVTQ3dTNac1VWWldBIn0.eyJqdGkiOiJjNWJiZDFjOS1kYmJhLTQ5MzctODlkYy05NGVjZmU3YjUyYzUiLCJleHAiOjE1NTIzMjg4NjcsIm5iZiI6MCwiaWF0IjoxNTUyMzI3MDY3LCJpc3MiOiJodHRwOi8vMTkyLjE2OC44OC4yMjA6ODA4MS9hdXRoL3JlYWxtcy9vcmlvbiIsImF1ZCI6ImFjY291bnQiLCJzdWIiOiJkNWEyZjhmMi03ZWRiLTQ2YTgtOWE4MS1kZmRkYjgxYTQyNDAiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJyZXN0LXNlcnZpY2UiLCJhdXRoX3RpbWUiOjAsInNlc3Npb25fc3RhdGUiOiIxNDVjMzNhNC04MzUwLTQ1YzAtOGJmYy0yOWI1ZGM2MDI3NGIiLCJhY3IiOiIxIiwiYWxsb3dlZC1vcmlnaW5zIjpbIioiXSwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwidW1hX2F1dGhvcml6YXRpb24iLCJwYXltZW50X2dhdGV3YXlfdXNlciJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoicHJvZmlsZSBlbWFpbCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiencgdyIsInByZWZlcnJlZF91c2VybmFtZSI6IjQ2NjgyMjI2QHFxLmNvbSIsImdpdmVuX25hbWUiOiJ6dyIsImZhbWlseV9uYW1lIjoidyIsImVtYWlsIjoiNDY2ODIyMjZAcXEuY29tIn0.RBHLlI9pT8u9wBE09uI-3GGGFDTV3bYWN6DzRltv8l9D_wiocjKAMhQ6QwNLJn2g647Tag12lQvcsaTsVRJMCz83zA3LnboH6MuqkCIDzz-875XxBebueaSugzyl10tpPm104C17HMxdKVy-zSTMwvf9mEUllaXLtQMHXYoM2oI8uUjHtnXCiJomgOGbAHGSK6H3ZCPwQGwyuhHv8wBAZbyZwR8oWH7cx8qhbRekWlVTd_pjKj97pE8uDDYsUjaIRy2v4NmADASy8-9mlarMz4BkMmEXkEoPJZv2BJ44TKIr4OAWSy5mLxAr4s1tNetbiNP2ryWh_VslZU8P5_xOtQ"
        self.invalid_none_token = ""
        self.invalid_token = []
        self.invalid_token.append(Xeger(limit=100).xeger(r'[a-z]+[A-Z]+[0-9]'))
        self.invalid_token.append(Xeger(limit=10).xeger(r'[a-z]+[A-Z]+[0-9]'))

        # data of the test report0.
        self.report_header = ['Test Steps', 'Test Data', 'Expected Result', 'Tested Result', 'Note']
        # get class name as report and sheet name, because class name is API test
        self.report_name = self.__class__.__name__
        self.report_sheet_name = self.__class__.__name__

    # @unittest.skip(" to open ")
    def test_create_order_id(self):
        payload = {
            "order": {"lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                      "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                          "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                          "zip": "H3A", "phone": 5141231234,
                                          "firstName": "Ting", "lastName": "Yu", "note": "note", "isDefault": False}},
            "shopId": 403}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.valid_token,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", self.url, json=payload, headers=headers)
        result = response.json()['order']['active']
        # self.assertEqual(result, 1)

        # for test report
        if self_definition_report:
            expection_result = 1
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
            expection_result = 1
            test_result = result
            self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to open ")
    def test_order_id_invalid_used_token(self):
        payload = {
            "order": {"lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                      "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                          "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                          "zip": "H3A", "phone": 5141231234,
                                          "firstName": "Ting", "lastName": "Yu", "note": "note", "isDefault": False}},
            "shopId": 403}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.invalid_used_token,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", self.url, json=payload, headers=headers)
        status_code = response.status_code
        # self.assertEqual(status_code, 401)

        # for test report
        if self_definition_report:
            expection_result = "unauthorization"
            test_result = status_code
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
            expection_result = "unauthorization"
            test_result = status_code
            self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to open ")
    def test_order_id_none_token(self):
        payload = {
            "order": {"lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                      "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                          "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                          "zip": "H3A", "phone": 5141231234,
                                          "firstName": "Ting", "lastName": "Yu", "note": "note", "isDefault": False}},
            "shopId": 403}
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + self.invalid_none_token,
            'cache-control': "no-cache"
        }

        response = requests.request("POST", self.url, json=payload, headers=headers)
        status_code = response.status_code
        # self.assertEqual(status_code, 401)

        # for test report
        if self_definition_report:
            expection_result = "unauthorization"
            test_result = status_code
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
            expection_result = "unauthorization"
            test_result = status_code
            self.assertEqual(test_result, expection_result)

    # @unittest.skip(" to open ")
    def test_order_id_invalid_token(self):
        for index in range(len(self.invalid_token)):
            payload = {
                "order": {
                    "lineItemInOrderList": [{"product": {"id": 1}, "quantity": 2, "ledgerLineItemOrder": {"id": 1}}],
                    "shippingAddress": {"province": {"code": "QC"}, "country": {"code": "CA"},
                                        "address1": "1625 Maisonneuve", "address2": "", "city": "Montreal",
                                        "zip": "H3A", "phone": 5141231234,
                                        "firstName": "Ting", "lastName": "Yu", "note": "note", "isDefault": False}},
                "shopId": 403}
            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + self.invalid_token[index],
                'cache-control': "no-cache"
            }

            response = requests.request("POST", self.url, json=payload, headers=headers)
            status_code = response.status_code
            # self.assertEqual(status_code, 401)

            # for test report
            if self_definition_report:
                expection_result = "unauthorization"
                test_result = status_code
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
                expection_result = "unauthorization"
                test_result = status_code
                self.assertEqual(test_result, expection_result)

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
    # outfile = os.path.join(path, 'test_register_keycloak_user.py')
    # report_path_html = './test_normal_report_format_html/'
    # report_file_name = report_path_html + __file__ + strftime("-%Y-%m-%d %H-%M", gmtime()) + '-report.html'
    # run(argv=['nosetest', '-v', '--with-html-output', '--html-out-file=report.html', outfile], plugins=[HtmlOutput()])

if __name__ == '__main__':
    unittest.main()
