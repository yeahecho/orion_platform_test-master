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


class TestUploadAndSubmitTask(unittest.TestCase):
    report_data = []

    def setUp(self):
        base_api = BaseApi()
        # url
        self.url = "http://192.168.88.216:8080/orionboot/uploadScript"
        # test data
        self.valid_token = base_api.get_token()
        self.order_id = base_api.get_order_id(self.valid_token)
        self.wallet_address = base_api.get_wallet_address(self.valid_token)
        self.task_id = base_api.get_task_id(self.valid_token, self.order_id, self.wallet_address)
        self.task_file = './word2vec_orionTestVersion.zip'
        self.task_name = "NUBIA10000"
        self.valid_duration = "3600"
        self.gpu_count = ["1", "2", "4"]
        self.ledger_ip = "192.168.88.152:8080"
        self.unit_fee = "5000000000000000"
        # invalid test data
        self.invalid_token = []
        self.invalid_token.append(Xeger(limit=100).xeger(r'[a-z]+[A-Z]+[0-9]'))
        self.invalid_token.append(Xeger(limit=10).xeger(r'[a-z]+[A-Z]+[0-9]'))
        self.invalid_wallet_address = '0x51eF2397CA6YYYYYYYYYYYYY17d2372cB00Fd1f2'
        self.invalid_order_id = "987766665"
        self.order_id_invalid = 2000
        self.invalid_task_id = "67889999999"
        self.invalid_duration_negative = "-3600"
        self.invalid_duration_float = "36.99"
        self.invalid_duration_zero = "0"
        self.invalid_gpu_count = "-9"

        # data of the test report
        self.report_header = ['Test Steps', 'Test Data', 'Expected Result', 'Tested Result', 'Note']
        # get class name as report and sheet name, because class name is API test
        self.report_name = self.__class__.__name__
        self.report_sheet_name = self.__class__.__name__

        self.web_kit_form_boundary = "----WebKitFormBoundary7MA4YWxkTrZu0gW"

    # @unittest.skip("to open")
    def test_upload_submit_success(self):
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"" + self.task_file + "\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n" + self.valid_duration + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\n" + self.task_name + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n" + str(
            self.order_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n" + \
                  self.gpu_count[
                      0] + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n" + self.ledger_ip + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n" + str(
            self.task_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n" + self.unit_fee + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"" + self.task_file + "\"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n"+self.valid_duration+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\n"+self.task_name+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n"+self.order_id+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n"+self.gpu_count[0]+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n"+self.ledger_ip+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n"+self.task_id+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n"+self.unit_fee+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"D:\\Nubula stage\\orion_platform_test\\word2vec_orionTestVersion.zip\"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n3600\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\ntest996\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n"+str(self.order_id)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n192.168.88.152:8080\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n"+str(self.task_id)+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n500000000000000000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        # payload_upload_submit_task = ("------" + self.web_con + "name=\"data\"; filename=" + self.task_file_path + "\r\nContent-Type: application/zip\r\n\r\n\r\n"
        #                               "------" + self.web_con + "name=\"duration\"\r\n\r\n3600\r\n"
        #                               "------" + self.web_con + "name=\"taskName\"\r\n\r\n" + self.task_name + "\r\n"
        #                               "------" + self.web_con + "name=\"Id\"\r\n\r\n" + self.order_id + "\r\n"
        #                               "------" + self.web_con + "name=\"gpu_count\"\r\n\r\n1\r\n"
        #                               "------" + self.web_con + "name=\"ledger_ip\"\r\n\r\n192.168.88.152:8080\r\n"
        #                               "------" + self.web_con + "name=\"task_id\"\r\n\r\n" + self.task_id + "\r\n"
        #                               "------" + self.web_con + "name=\"unit_fee\"\r\n\r\n500000000000000000\r\n"
        #                               "------" + self.boundary + "--")
        # payload = ("--" + self.web_kit_form_boundary + "name=\"data\"; filename=" + self.task_file + "\r\nContent-Type: application/zip\r\n\r\n\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"duration\"\r\n\r\n3600\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"taskName\"\r\n\r\n" + self.task_name + "\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"Id\"\r\n\r\n" + str(self.order_id) + "\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"gpu_count\"\r\n\r\n" + self.gpu_count[0] + "\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"ledger_ip\"\r\n\r\n"+ self.ledger_ip + "\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"task_id\"\r\n\r\n" + str(self.task_id) + "\r\n"
        #            "--" + self.web_kit_form_boundary + "name=\"unit_fee\"\r\n\r\n" + self.unit_fee + "\r\n"
        #            "--" + self.web_kit_form_boundary + "--")

        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer " + self.valid_token
        }
        response = requests.request("POST", self.url, data=payload, headers=headers)
        # print(response.text)
        result = response.json()['code']
        # self.assertEqual(result, "200300")

        # for test report
        if self_definition_report:
            expection_result = '200300'
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
            expection_result = '200300'
            test_result = result
            self.assertEqual(result, expection_result)

    # @unittest.skip("to open")
    def test_upload_submit_multiple_time(self):
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"D:\\Nubula stage\\orion_platform_test\\word2vec_orionTestVersion.zip\"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n3600\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\ntest996\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n1023\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n192.168.88.152:8080\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n154\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n500000000000000000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer " + self.valid_token
        }
        response = requests.request("POST", self.url, data=payload, headers=headers)

        result = response.json()["message"]
        # self.assertEqual(result, "Failed, task has been submitted.")

        # for test report
        if self_definition_report:
            expection_result = "Failed, task has been submitted."
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
            expection_result = '200300'
            test_result = result
            self.assertEqual(result, expection_result)

    # @unittest.skip("to open")
    def test_upload_submit_invalid_token(self):
        for index in range(len(self.invalid_token)):
            # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"D:\\Nubula stage\\orion_platform_test\\word2vec_orionTestVersion.zip\"\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n3600\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\ntest996\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n1023\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n192.168.88.152:8080\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n154\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n500000000000000000\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
            payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"" + self.task_file + "\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n" + self.valid_duration + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\n" + self.task_name + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n" + str(
                self.order_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n" + \
                      self.gpu_count[
                          0] + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n" + self.ledger_ip + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n" + str(
                self.task_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n" + self.unit_fee + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
            headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'Authorization': "Bearer " + self.invalid_token[index]
            }
            response = requests.request("POST", self.url, data=payload, headers=headers)

            result = response.text
            # self.assertEqual(result, 'Unauthorization')

            # for test report
            if self_definition_report:
                expection_result = 'Unauthorization'
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
                expection_result = '200300'
                test_result = result
                self.assertEqual(result, expection_result)

    # @unittest.skip("to open")
    def test_pay_leger_invalid_order_id(self):
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"data\"; filename=\"" + self.task_file + "\r\nContent-Type: application/zip\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"duration\"\r\n\r\n" + self.valid_duration + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"taskName\"\r\n\r\n" + self.task_name + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Id\"\r\n\r\n" + str(
            self.invalid_order_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"gpu_count\"\r\n\r\n" + \
                  self.gpu_count[
                      0] + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ledger_ip\"\r\n\r\n" + self.ledger_ip + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"task_id\"\r\n\r\n" + str(
            self.task_id) + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"unit_fee\"\r\n\r\n" + self.unit_fee + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Bearer " + self.valid_token
        }
        response = requests.request("POST", self.url, data=payload, headers=headers)
        # print(response.text)
        result = response.json()["Exception"]
        # self.assertEqual(result, "java.lang.NullPointerException")

        # for test report
        if self_definition_report:
            expection_result = "java.lang.NullPointerException"
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
            expection_result = '200300'
            test_result = result
            self.assertEqual(result, expection_result)

    @unittest.skip('no need to test here, because it is controlled by front-end')
    def test_unit_fee(self):
        pass

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
