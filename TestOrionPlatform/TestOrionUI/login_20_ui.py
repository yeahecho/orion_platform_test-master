import datetime
import time
# from aiofiles import os
#
# import os
# from nose import run
from selenium import webdriver
import unittest
import csv


def readCsv(row, col):
    rows = []
    with open('UserList.csv') as f:  ## open the file
        reader = csv.reader(f)
        next(reader, None)
        for iter in reader:
            rows.append(iter)
    return ''.join(rows[row][
                       col])  ##.decode('gb2312') ##If the file form has Chinese, you need to change to gd2312(表格有中文，需要改为gd2312)


class TestLoginOrion(unittest.TestCase):
    def readCsv(row, col):
        rows = []
        with open('UserList.csv') as f:  ## open the file
            reader = csv.reader(f)
            next(reader, None)
            for iter in reader:
                rows.append(iter)
        return ''.join(rows[row][
                           col])  ##.decode('gb2312') ##If the file form has Chinese, you need to change to gd2312(表格有中文，需要改为gd2312)

    @classmethod
    def setUpClass(cls):  ## cls:for class,
        # test data
        cls.driver = webdriver.Chrome("/Users/guoec/Downloads/chromedriver")
        # self.driver.get = self.driver.get("https://orioncloud.io/dashboard")
        cls.driver.get = cls.driver.get("http://192.168.88.216:8080/orion-dashboard-boot/#/login")

        cls.driver.implicitly_wait(30)
        cls.verificationErrors = []
        cls.accept_next_alert = True

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def login(self, username, password):
        self.driver.find_element_by_xpath(
            "//*[@id='m_login']/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input").clear()
        self.driver.find_element_by_xpath(
            "//*[@id='m_login']/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input").send_keys(username)
        time.sleep(1)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="m_login_signin_submit"]').click()

    def divText_null(self):
        divText_null = self.driver.find_element_by_xpath('//*[@id="password-error"]').text
        # print(divText_null)
        return divText_null

    def divText_invalid(self):
        divText_invalid = self.driver.find_element_by_xpath('//*[@id="userName-error"]').text
        # print(divText_invalid)
        return divText_invalid

    def divText(self):
        divText = self.driver.find_element_by_xpath(
            '//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[1]/form/app-alert/div/span').text
        # print(divText)
        return divText

    def test_username_password_null(self):
        self.login(readCsv(0, 0), readCsv(0, 1))
        # print(self.divText_null(), readCsv(0, 2))
        self.assertEqual(self.divText_null(), readCsv(0, 2))

    def test_password_null(self):
        self.login(readCsv(1, 0), readCsv(1, 1))
        self.assertEqual(self.divText_null(), readCsv(1, 2))

    def test_username_null(self):
        self.login(readCsv(2, 0), readCsv(2, 1))
        # print(self.divText(), readCsv(2, 2))
        self.assertEqual('None', readCsv(2, 2))

    def test_username_format(self):
        self.login(readCsv(3, 0), readCsv(3, 1))
        # print(self.divText(), readCsv(3, 2))
        self.assertEqual(self.divText(), readCsv(3, 2))

    def test_username_invalid(self):
        self.login(readCsv(4, 0), readCsv(4, 1))
        # print(self.divText_invalid(), readCsv(4, 2))
        self.assertEqual(self.divText_invalid(), readCsv(4, 2))

    def test_password_format(self):
        self.login(readCsv(5, 0), readCsv(5, 1))
        # print(self.divText(), readCsv(5, 2))
        self.assertEqual(self.divText(), readCsv(5, 2))

    # def getNowTime(self):
    #     return time.strftime('%y-%m-%d %H_%M_%S', time.localtime(time.time()))
    #
    # def run(self):
    #     fileName = os.path.join(os.path.dirname(__file__), 'report', self.getNowTime() + 'report.html')
    #     fp = open(fileName, 'wb')
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
    #                                            title='UI Automation Test Report',
    #                                            description='UI Automation Test Report Details')
    #     runner.run()
    #


if __name__ == '__main__':
    unittest.main(verbosity=2)

    # path = os.path.dirname(__file__)
    # outfile = os.path.join(path, 'login_ui.py')
    # run(argv=['nosetests', '-v', '--with-html-output',
    #           '--html-out-file= ' + str(datetime.date.today()) + 'login(UI-test) Report.html',
    #           outfile], plugins=[HtmlOutput()])

