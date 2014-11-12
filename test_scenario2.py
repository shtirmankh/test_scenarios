#coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestScenario2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        mainPage = self.driver.get("http://devmate.com")


    def testFeatures(self):
        framePage = "http://devmate.com/features/frameworks"

        featuresButton = self.driver.find_element_by_css_selector(".container>nav>a")
        featuresButton.click()

        self.assertEquals(framePage, self.driver.current_url)

        wait = WebDriverWait(self.driver, 5)
        elemPic = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".container>nav>a")))
        #self.driver.get_screenshot_as_file("/Screenshot/screen1.png")
        self.driver.save_screenshot("screen1.png")

        link = "http://devmate.com/features/app-management"
        self.driver.get(link)
        self.assertEquals(link, self.driver.current_url)
        elemBlock = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".visual-slider-img.on>img")))
        self.assertTrue(elemBlock)
        self.driver.save_screenshot("screen2.png")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()