import pytest
import time
import random
import string
from page_objects.AddcustomerPage import AddCustomer
from page_objects.login_page import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By


class Test_003_AddCustomer:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    logger=LogGen.loggen()


    def test_addcustomer(self,setup):
        self.logger.info("*********login starts************")
        self.driver=setup
        self.logger.info("*********URL is opening************")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        time.sleep(4)

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.logger.info("********* new customer is adding************")
        self.addcust.clickOnAddnew()
        self.email = self.random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        #self.addcust.setEmail("drumak@gmail.com")
        time.sleep(2)
        self.addcust.setPassword("test123")
        time.sleep(2)
        self.addcust.setFirstName("DRUMAK")
        time.sleep(2)
        self.addcust.setLastName("CHINNA")
        time.sleep(2)
        self.addcust.setGender("Male")
        time.sleep(2)
        self.addcust.setDob("05/5/1985")
        time.sleep(2)
        self.addcust.setCompanyName("@")
        time.sleep(2)
        self.addcust.setCustomerRoles("Vendors")
        time.sleep(2)
        self.addcust.setManagerOfVendor("Vendor 2")
        time.sleep(2)
        self.addcust.setAdminContent("This is for Automation_testing.........")
        time.sleep(2)
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element(By.TAG_NAME,"body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "12:27_test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

    '''def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))'''
    def random_generator(size = 8, chars = string.ascii_lowercase+string.digits):
           return ''.join(random.choice(chars)for x in range(size))



