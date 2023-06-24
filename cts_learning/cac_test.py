
# -*- coding: utf-8 -*-
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_app_dynamics_job(self):
        driver = self.driver
        driver.get("https://india.oup.com/orcs/9780199451647/")
        for i in range(30):
            try:
                if self.is_element_present(By.XPATH, "//button[@onclick=\"javascript:submitOnlineResource('S',9780199451647)\"]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Organic Chemistry", driver.find_element("xpath", "//div[@id='general_content']/div[2]/div/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("HomePage invocation is successful")
        driver.find_element("xpath", "//button[@onclick=\"javascript:submitOnlineResource('S',9780199451647)\"]").click()
        for i in range(30):
            try:
                if self.is_element_present(By.ID, "btnSignIn"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Sign in with your Oxford ID", driver.find_element("xpath", "//div[@id='general_content']/div[2]/div/h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("Sign in page is successful")
        #driver.find_element("xpath", "//div[@id='general_content']/div[2]/div[2]/div[2]/form/div[1]/div[2]")
        driver.find_element("uid").clear()
        driver.find_element("uid").send_keys("akanksha.sharma@cognizant.com")
        driver.find_element("pwd").clear()
        driver.find_element("pwd").send_keys("akankshaOUP123")
        driver.find_element("btnSignIn").click()
        for i in range(30):
            try:
                if self.is_element_present(By.XPATH, "//div[@id='general_content']/div[2]/div/h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print("Sign in for the user is successful")
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        driver.find_element_by_link_text("Keep Updated").click()
        for i in range(30):
            try:
                if self.is_element_present(By.XPATH, "//div[@id='general_content']/div[2]/div/h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        print("Keep updated page is successful")
        driver.find_element_by_link_text("Sign out").click()
        for i in range(30):
            try:
                if self.is_element_present(By.XPATH, "//div[@id='general_content']/div[2]/div/h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("You have now been signed out of your Oxford ID account.", driver.find_element("xpath", "//div[@id='general_content']/div[2]/div[2]/div/p").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        print("Signout is successful")
        driver.close()
    
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
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()