import time
#import unittest
import pytest
from selenium import webdriver
from page_objects.login_page import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("*************** Test_001_Login *****************")
        self.logger.info("****Started Home page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        time.sleep(4)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.save_screenshot(".\\screenshots\\" + "test_homePage.png")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** Home page title test failed****")
            self.driver.close()
#            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):

        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        time.sleep(4)
        self.lp.setusername(self.username)
        time.sleep(3)
        self.lp.setPassword(self.password)
        time.sleep(3)
        self.lp.clickLogin()
        time.sleep(2)
        print(self.driver.title)
        self.lp.click_logout()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("****Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot(".\\screenshots\\" + "test_login.png")
            self.driver.close()
#            assert False
