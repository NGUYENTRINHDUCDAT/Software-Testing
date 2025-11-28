# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ProductDetailAddToCart7(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_product_detail_add_to_cart7(self):
        driver = self.driver
        driver.get("https://demo.nopcommerce.com/")
        driver.find_element(By.LINK_TEXT,"Apple MacBook Pro").click()
        driver.find_element(By.ID,"product_enteredQuantity_4").click()
        driver.find_element(By.ID,"product_enteredQuantity_4").clear()
        driver.find_element(By.ID,"product_enteredQuantity_4").send_keys("0")
        driver.find_element(By.XPATH,"//form[@id='product-details-form']/article/div/div[2]/div[8]/div").click()
        driver.find_element(By.ID,"product-details-form").submit()
        driver.find_element(By.ID,"add-to-cart-button-4").click()
        driver.find_element(By.ID,"product_enteredQuantity_4").click()
        driver.find_element(By.ID,"product_enteredQuantity_4").clear()
        driver.find_element(By.ID,"product_enteredQuantity_4").send_keys("-1")
        driver.find_element(By.XPATH,"//form[@id='product-details-form']/article/div/div[2]/div[8]/div").click()
        driver.find_element(By.ID,"product-details-form").submit()
        driver.find_element(By.ID,"add-to-cart-button-4").click()
    
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
