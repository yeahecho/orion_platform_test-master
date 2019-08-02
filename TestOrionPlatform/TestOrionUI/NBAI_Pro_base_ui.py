

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class login_base(object):
    def __init__(self, driver):
        self.driver = driver
        # self.wait = WebDriverWait(self.driver, 15)

    def login(self, driver, username, password):
        self.driver.get = driver.get
        # driver.get("https://nbai.io/dashboard")
        # driver.get("http://192.168.88.216:8080/orion-dashboard-boot/#/login")

        self.driver.maximize_window()
        time.sleep(2)

        # self.driver.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='Please wait...'])[1]/following::div[4]").click()

        # self.driver.find_element_by_name("userName").click()
        # self.driver.find_element_by_name("userName").clear()
        # self.driver.find_element_by_name("userName").send_keys(username)
        self.driver.find_element_by_xpath("//*[@id='m_login']/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input").click()
        self.driver.find_element_by_xpath("//*[@id='m_login']/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input").clear()
        self.driver.find_element_by_xpath("//*[@id='m_login']/div[1]/div[2]/div[1]/div/div[1]/form/div[1]/input").send_keys(username)

        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)

        time.sleep(2)

        self.driver.find_element_by_xpath('//*[@id="m_login_signin_submit"]').click()
        time.sleep(2)

    def logout(self):
        self.driver.find_element_by_xpath("//*[@id='m_header_topbar']/div/ul/li/a/span[1]").click()
        self.driver.find_element_by_xpath("//*[@id='m_header_topbar']/div/ul/li/div/div/div[2]/div/ul/li[4]/a").click()
        time.sleep(2)
        self.driver.close()


    def change_password(self, oldPassword, newPassword, conPassword):
        # self.driver.find_element_by_xpath("//*[@id'm_ver_menu']/ul/li[4]/a/span/span").click()
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div[2]/div/div[1]/div/ul/li[4]/a").click()
        # self.driver.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[2]/div/div[2]/div/div[1]/div/ul/li[4]/a").click()
        # self.driver.find_element_by_link_text("Security").click()

        # self.driver.get("https://orioncloud.io/dashboard/#/profile")
        # self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Task History'])[1]/following::span[2]").click()
        self.driver.find_element_by_xpath("/html/body/div[4]/i").click()
        time.sleep(4)
        self.driver.find_element_by_link_text("Security").click()

        self.driver.find_element_by_id("oldPassword").click()
        self.driver.find_element_by_id("oldPassword").clear()
        self.driver.find_element_by_id("oldPassword").send_keys(oldPassword)
        time.sleep(4)

        self.driver.find_element_by_id("newPassword").click()
        self.driver.find_element_by_id("newPassword").clear()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=newPassword | ]]
        time.sleep(2)
        self.driver.find_element_by_id("newPassword").send_keys(newPassword)
        time.sleep(4)

        self.driver.find_element_by_id("conPassword").click()
        self.driver.find_element_by_id("conPassword").clear()
        self.driver.find_element_by_id("conPassword").send_keys(conPassword)
        time.sleep(4)

        self.driver.find_element_by_xpath("//*[@id='m_user_profile_tab_4']/form/div[2]/div/div/div[2]/button[1]").click()
        # self.driver.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='Confirm Password*'])[1]/following::button[1]").click()
        # self.driver.find_element_by_xpath(
        #     "(.//*[normalize-space(text()) and normalize-space(.)='Task History'])[1]/following::span[2]").click()


if __name__ == "__main__":
    login_base()
