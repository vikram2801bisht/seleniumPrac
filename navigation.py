import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NavigationTesting(unittest.TestCase):

    options = Options()
    options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

    def setUp(self):
        self.driver = webdriver.Firefox(options = self.options)

    def test_google_search(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.implicitly_wait(10)
        # page_title = WebDriverWait(driver, 10).until(EC.title_contains("Google"))

        self.assertIn("Google", driver.title)
        time.sleep(6)
        element = driver.find_element(By.NAME, "q")
        time.sleep(6)
        element.clear()
        element.send_keys("Playwright")
        element.send_keys(Keys.RETURN)
        self.assertIn("playwright", driver.page_source.lower())

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()