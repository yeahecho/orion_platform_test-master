from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import datetime
import HtmlTestRunner


class TestOrionUI(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome("chromedriver")
       self.driver.implicitly_wait(30)
       self.base_url = "http://192.168.88.216:8080/orion-dashboard-boot/#/login"
       self.taskname = "NBAI." + str(datetime.date.today())
       self.task_file_path = '/home/mikeli/Downloads/tasks/'
       self.task_file_name = ('orion-word2vec-master.zip')
       self.verificationErrors = []
       self.accept_next_alert = True

    def testOrionUI(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input').send_keys('rex.miller@hotmail.ca')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[1]/form/div[2]/input').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="m_login"]/div[1]/div[2]/div[1]/div/div[1]/form/div[2]/input').send_keys('111111')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="m_login_signin_submit"]').click()
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="m_ver_menu"]/ul/li[4]/a/span/span/span').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="serviceType"]/option[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="serviceType"]/option[2]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="1"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="time"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="time"]').send_keys('1')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="m_modal_price"]/div/div/div[3]/button[1]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deposit"]').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deposit"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deposit"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deposit"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="deposit"]').send_keys('100')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="m_task_tab_2"]/div/div[4]/div[1]/form/div[3]/div/button/span').click()
        time.sleep(1)


        driver.find_element_by_name("taskname").click()
        time.sleep(1)
        driver.find_element_by_name("taskname").clear()
        time.sleep(1)
        driver.find_element_by_name("taskname").send_keys(self.taskname)
        time.sleep(1)

        driver.find_element_by_id('gpu_count').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="gpu_count"]/option[1]').click()
        time.sleep(1)


        driver.find_element_by_xpath('//*[@id="m_task_tab_3"]/form/div[1]/div[5]/div/label/span[1]').click()
        time.sleep(1)

        driver.find_element_by_id("scriptUrl").send_keys('/home/mikeli/Downloads/tasks/word2vec_orion.zip')
        time.sleep(1)

        driver.find_element_by_xpath('//*[@id="m_task_tab_3"]/form/div[2]/div/div/div[2]/button').click()
        time.sleep(1)

        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Output URL'])[1]/following::button[1]").click()  # production
        # time.sleep(180)
        #######  #ddd

        for element in self.driver.find_elements_by_xpath('//*[@id="m_task_tab_4"]/div/div[1]/div[3]/div[4]/a/span'):


       # btnDownload = driver.find_element_by_css_selector('#m_task_tab_4 > div > div.task_progress > div.m-wizard__steps > div:nth-child(4) > a > span')
            colorString = element.value_of_css_property('background-color')
            stringExpected = "#ddd"
            colorString02 = str(colorString)
            print(colorString)
            if colorString02 != stringExpected:
                driver.find_element_by_xpath('//*[@id="m_task_tab_4"]/div/div[2]/div/button[1]').click()


    def tearDown(self):
        pass

if __name__ == "__main__":
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./TestReport'))
