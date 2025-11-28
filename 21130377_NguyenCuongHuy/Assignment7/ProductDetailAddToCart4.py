# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ProductDetailAddToCart4(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_product_detail_add_to_cart4(self):
        driver = self.driver
        driver.get("https://demo.nopcommerce.com/")
        driver.find_element(By.XPATH,"//button[@type='button']").click()
        driver.find_element(By.ID,"product_attribute_1").click()
        Select(driver.find_element("product_attribute_1")).select_by_visible_text("2.2 GHz Intel Pentium Dual-Core E2200")
        driver.find_element(By.ID,"product_attribute_2").click()
        Select(driver.find_element(By.ID,"product_attribute_2")).select_by_visible_text("2 GB")
        driver.find_element(By.XPATH,"//dd[@id='product_attribute_input_3']/ul/li/label").click()
        driver.find_element(By.XPATH,"//dd[@id='product_attribute_input_4']/ul/li[2]/label").click()
        driver.find_element(By.XPATH,"//dd[@id='product_attribute_input_5']/ul/li[3]/label").click()
        driver.find_element(By.ID,"add-to-cart-button-1").click()
    
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
