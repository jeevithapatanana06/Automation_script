import string

import pytest
import time
from page_objects.customerRoles import custRoles
from page_objects.login_page import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_CustomerRoles:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    def test_addcustomer_roles(self,setup):
        self.logger.info("*********login starts************")
        self.driver=setup
        self.logger.info("*********URL is opening************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.c = custRoles(self.driver)
        self.c.clickOnCustomersMenu()
        self.c.clickCustroles()
        self.c.custRolesAddcust()
        self.c.setname("Bugati")
        self.c.select_freeshipping()
        self.c.select_taxExempt()
        self.c.enable_pswd()
        self.c.set_systmName("charles babbage")
        self.c.savebtn()
        self.logger.info("*******saving the new cust role***********")
        self.note = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.note)
        if "The new customer role has been added successfully." in self.note:
            assert True==True

            self.logger.info("****the cust role has saved successfully****")
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_custrole.png")
            self.logger.info("******test failed*******")
            assert True==False

            self.driver.close()
            self.logger.info("*******the test ended******")






