#coding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import HTMLTestRunner
from locators import MainPageLocators, UrlLinks

class TestScenario1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(UrlLinks.startPage)

    def test1(self):
        signUp = self.driver.find_element(*MainPageLocators.SIGNUP_BUTTON)
        signUp.click()
        self.assertEquals(UrlLinks.signUpPage, self.driver.current_url)

        checkBox = self.driver.find_element(*MainPageLocators.CHECKBOX)
        checkBox.click()
        self.assertTrue(checkBox.is_selected())

        wait = WebDriverWait(self.driver, 5)
        solutionForm = wait.until(EC.element_to_be_clickable(MainPageLocators.SOLUTIONFORM))
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