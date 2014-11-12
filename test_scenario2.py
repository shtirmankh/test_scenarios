#coding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
import HTMLTestRunner
from locators import MainPageLocators, UrlLinks

class TestScenario2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(UrlLinks.startPage)

    def testFeatures(self):
        featuresButton = self.driver.find_element(*MainPageLocators.FEATURES_BUTTON)
        featuresButton.click()

        self.assertEquals(UrlLinks.framePage, self.driver.current_url)

        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(MainPageLocators.ELEM_PIC))
        self.driver.save_screenshot("screen1.png")

        self.driver.get(UrlLinks.link)
        self.assertEquals(UrlLinks.link, self.driver.current_url)
        wait.until(EC.visibility_of_element_located(MainPageLocators.ELEM_BLOCK))
        self.assertTrue(MainPageLocators.ELEM_BLOCK)
        self.driver.save_screenshot("screen2.png")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(TestScenario2))
        dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
        buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
             stream=buf,
             title='Test the Report',
             description='Result of tests'
             )
        runner.run(suite)