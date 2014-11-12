#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import HTMLTestRunner

class TestScenario1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        mainPage = self.driver.get("http://devmate.com")


    def test1(self):
        signUpPage = "http://devmate.com/signup"
        signUpButton = self.driver.find_element_by_css_selector(".btn.btn-construct.btn-sign-up-now")
        signUpButton.click()
        self.assertEquals(signUpPage, self.driver.current_url)

        checkBox = self.driver.find_element_by_name("selling_outside_app_store")
        checkBox.click()
        self.assertTrue(checkBox.is_selected())

        wait = WebDriverWait(self.driver, 5)
        solutionForm = wait.until(EC.element_to_be_clickable((By.XPATH, ".//*[@id='form-signup']/input[5]")))
        self.assertTrue(solutionForm)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestScenario1))
        dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
        buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
             stream=buf,
             title='Test the Report',
             description='Result of tests'
             )
        runner.run(suite)