

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = "/snap/firefox/current/usr/lib/firefox/firefox"  # adjust to what you found


driver = webdriver.Firefox(options = options)
driver.get("https://www.google.com")
print("Page title:", driver.title)
driver.quit()