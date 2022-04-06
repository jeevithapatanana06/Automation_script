import string
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class custRoles:
    #add customer roles :
    lnkCustomers_menu_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    custroles_item_xpth = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[2]/a/p"
    custrole_addrole_xpath = "/html/body/div[3]/div[1]/div/div/a"
    name_field_xpath = "//*[@id='Name']"
    freeshipping_key_id = "FreeShipping"
    taxexempt_key_ID = "TaxExempt"
    enable_pswd_ID = "EnablePasswordLifetime"
    set_systm_field_xpth = "//*[@id='SystemName']"
    save_btn_xpth = "/html/body/div[3]/div[1]/form/div/div/button[1]"

    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomers_menu_xpath).click()

    def clickCustroles(self):
        self.driver.find_element(By.XPATH,self.custroles_item_xpth).click()

    def custRolesAddcust(self):
        self.driver.find_element(By.XPATH,self.custrole_addrole_xpath).click()

    def setname(self,name):
        self.driver.find_element(By.XPATH,self.name_field_xpath).clear()
        self.driver.find_element(By.XPATH,self.name_field_xpath).send_keys(name)

    def select_freeshipping(self):
        self.driver.find_element(By.ID,self.freeshipping_key_id).click()

    def select_taxExempt(self):
        self.driver.find_element(By.ID,self.taxexempt_key_ID).click()

    def enable_pswd(self):
        self.driver.find_element(By.XPATH,self.enable_pswd_ID).click()

    def set_systmName(self,sname):
        self.driver.find_element(By.XPATH,self.set_systm_field_xpth).clear()
        self.driver.find_element(By.XPATH,self.set_systm_field_xpth).send_keys(sname)

    def savebtn(self):
        self.driver.find_element(By.XPATH,self.save_btn_xpth).click()

    def clickCustroles(self):
        self.driver.find_element(By.XPATH,self.custroles_item_cls).click()








