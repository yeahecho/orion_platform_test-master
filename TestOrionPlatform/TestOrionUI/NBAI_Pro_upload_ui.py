

# from htmloutput import HtmlOutput
import os

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest, time
import datetime
# from TestOrionPlatform import NBAI_Pro_base_ui
from TestOrionPlatform.TestOrionUI import NBAI_Pro_base_ui


class OrionProUploadUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("FilesOfAPI/chromedriver")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.valid_username = 'rex.miller@hotmail.ca'
        self.valid_password = 'a123456'

        # self.valid_username = "nit8688@gmail.com"
        # self.valid_password = "111111"

        self.task_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './FilesOfAPI'))
        self.task_file_name = ('/orion-word2vec-master.zip')
        self.taskname = "NBAI-" + str(datetime.date.today()) + str("-UI-test3")
        self.message = "4"

    def test_upload_ui(self):
        driver = self.driver
        driver.get("http://nbai.io/")
        # driver.get("http://192.168.88.216:8080/orion-dashboard-boot/")
        driver.maximize_window()
        driver.find_element_by_xpath('//*[@id="loginUserLog"]').click()
        time.sleep(2)

        # login
        driver.find_element_by_xpath('/html/body').click()
        login_page = NBAI_Pro_base_ui.login_base(self.driver)  # 引入登录文件，文件名+class名
        login_page.login(self.driver, self.valid_username, self.valid_password)
        time.sleep(5)

        self.driver.execute_script("scroll(0, 0);")  # To page top
        time.sleep(3)

        driver.find_element_by_xpath("//*[@id='m_ver_menu']/ul/li[4]/a/span/span/span").click()
        driver.find_element_by_xpath("//*[@id='m_header_topbar']/div/ul/li[2]/select").click()
        time.sleep(3)

        driver.find_element_by_id("serviceType").click()
        Select(driver.find_element_by_id("serviceType")).select_by_visible_text("Micro")  ##for "Micro"
        # Select(driver.find_element_by_id("serviceType")).select_by_visible_text("Classic")  ##for "Classic"
        # Select(driver.find_element_by_id("serviceType")).select_by_visible_text("Premium")   ##for "Premium"
        time.sleep(3)

        driver.find_element_by_id("serviceType").click()
        driver.find_element_by_id("1").click()  ##for "Micro"
        # driver.find_element_by_id("2").click()  ##for "Classic"
        # driver.find_element_by_id("3").click()   ##for "Premium"

        time.sleep(3)

        # driver.find_element_by_id("serviceType").click()
        # driver.find_element_by_id("serviceType").click()
        # driver.find_element_by_id("2").click()
        # time.sleep(1)

        driver.find_element_by_id("time").click()
        driver.find_element_by_id("time").clear()
        driver.find_element_by_id("time").send_keys("1")
        time.sleep(1)

        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Total Cost:'])[1]/following::button[1]").click()
        time.sleep(3)
        driver.find_element_by_id("deposit").click()
        driver.find_element_by_id("deposit").clear()
        time.sleep(1)
        driver.find_element_by_id("deposit").send_keys("1000")
        # driver.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='Make a deposit to run more AI tasks.'])[1]/following::span[1]").click()
        driver.find_element_by_xpath('//*[@id="m_task_tab_2"]/div/div[4]/div[1]/form/div[3]/div/button').click()
        time.sleep(2)

        js = "var q=document.documentElement.scrollTop=1000000"  ##To page bottom
        driver.execute_script(js)
        time.sleep(1)

        driver.find_element_by_name("taskname").click()
        driver.find_element_by_name("taskname").clear()
        driver.find_element_by_name("taskname").send_keys(self.taskname)
        time.sleep(3)

        driver.find_element_by_id("gpu_count").click()
        Select(driver.find_element_by_id("gpu_count")).select_by_visible_text("1")
        driver.find_element_by_id("gpu_count").click()
        time.sleep(3)

        # driver.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='Upload Script*'])[1]/following::span[1]").click()
        # driver.find_element_by_id("scriptUrl").clear()
        # time.sleep(10)
        driver.find_element_by_id("scriptUrl").send_keys(self.task_file_path + self.task_file_name)
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Output URL'])[1]/following::button[1]").click()
        time.sleep(100)

        title = driver.find_element_by_xpath("//*[@id='m_task_tab_4']/div/div[1]/div[3]/div[4]/a/span/span").text
        self.assertEqual(title, self.message)

    # path = os.path.dirname(__file__)
    # outfile = os.path.join(path, 'NBAI_dev_upload_ui.py')
    # run(argv=['nosetests', '-v', '--with-html-output', '--html-out-file=20190522-dev-upload(UI-test) Report.html',
    #           outfile], plugins=[HtmlOutput()])

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
