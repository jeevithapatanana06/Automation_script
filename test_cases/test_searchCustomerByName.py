import time
import pytest

from page_objects.AddcustomerPage import AddCustomer
from page_objects.SearchCusomerPage import SearchCustomer
from page_objects.login_page import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        addcust = AddCustomer(self.driver)
        addcust.clickOnCustomersMenu()
        addcust.clickOnCustomersMenuItem()
        time.sleep(2)

        self.logger.info("************* searching customer by Name **********")
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")
        self.searchcust.setLastName("Terces")
        self.searchcust.clickSearch()
        time.sleep(5)
        status= self.searchcust.searchCustomerByName("Victoria Terces")
        self.driver.close()
        assert True==status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")


