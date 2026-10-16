import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


class demoQA_Testing(unittest.TestCase):

    options = Options()
    options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"

    def setUp(self):
        self.driver = webdriver.Firefox(options= self.options)
        self.driver.maximize_window()

    def test_demo_page(self):
        driver = self.driver
        actions = ActionChains(driver)
        driver.get("https://demoqa.com/")
        time.sleep(5)

        #Searching for the Elements page
        elements_card = driver.find_element(By.XPATH, "//h5[text()='Elements']")
        assert elements_card.is_displayed()
        elements_card.click()
        time.sleep(5)

        #Enable the Elements tab
        elements_tab = driver.find_element(By.CLASS_NAME, "pr-1")
        text_box = driver.find_element(By.CLASS_NAME, "text")
        if (elements_tab.is_selected):
            print("The Elements tab is already selected")
            assert text_box.is_displayed()
        else:
            elements_tab.click()
            print("The Elements tab was not selected so clicking on it.")

        time.sleep(5)


        #looking into the text box
        text_box.click()
        text_center = driver.find_element(By.CLASS_NAME, "text-center")
        assert text_center.is_displayed()
        print("The text box is opened and displayed.")

        #Filling the form
        full_name = driver.find_element(By.ID, "userName")
        full_name.click()
        full_name.clear()
        full_name.send_keys("Martha Gray")
        time.sleep(2)
        email = driver.find_element(By.ID, "userEmail")
        email.clear()
        email.send_keys("martha.gray2309@gmail.com")
        time.sleep(2)
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys("This is the current address").perform()
        time.sleep(2)
        print("The CurrentAddress is filled")
        actions.send_keys(Keys.TAB).send_keys("This is the Permanenet Address").perform()
        time.sleep(2)
        submit_button = driver.find_element(By.ID, "submit")
        assert submit_button.is_displayed
        assert submit_button.is_enabled
        submit_button.click()
        time.sleep(5)

        #Fetching the output from the field
        output = driver.find_element(By.ID, "output")
        print("The output of the input is - ")
        time.sleep(2)
        print(output.text)
        time.sleep(3)

        #Navigating to Checkbox
        checkbox_tab = driver.find_element(By.XPATH, "//span[text() = 'Check Box']")
        checkbox_tab.click()
        time.sleep(3)
        assert "/checkbox" in driver.current_url
        text_center0 = driver.find_element(By.XPATH, "//h1[@class='text-center' and text()='Check Box']")
        assert text_center0.is_displayed()
        print("The Check Box page is openeed.")
        checkBox = driver.find_element(By.CLASS_NAME, "rc-tree-checkbox")
        checkBox.click()
        assert "rc-tree-checkbox rc-tree-checkbox-checked" in checkBox.get_attribute("class")

        #checking the result
        result = driver.find_element(By.ID, "result")
        time.sleep(2)
        assert result.is_displayed()
        print("The result is displayed after checking the checkbox.")

        #fetch the result data
        raw_data = result.text
        # print(raw_data)
        selected_text = raw_data.split("You have selected :")[1].split("\n")
        cleaned_items = []
        for items in selected_text:
            cleaned_items.append(items)

        print(f"Total selected items: {len(selected_text)}")
        print(f"These are the items - {cleaned_items}")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()