# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ProductDetailAddToCart2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_product_detail_add_to_cart2(self):
        driver = self.driver
        driver.get("https://demo.nopcommerce.com/")
        driver.find_element(By.LINK_TEXT,"Build your own computer").click()
        driver.find_element(By.ID,"product_attribute_1").click()
        driver.find_element(By.ID,"product_attribute_2").click()
        Select(driver.find_element(By.ID,"product_attribute_2")).select_by_visible_text("8GB [+$60.00]")
        driver.find_element(By.ID,"product_attribute_3_7").click()
        driver.find_element(By.ID,"product_attribute_4_9").click()
        driver.find_element(By.ID,"product_attribute_5_11").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
