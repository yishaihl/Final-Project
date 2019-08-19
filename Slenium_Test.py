#Import Required Packages:
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#Project variable:
driver_location = "//Users//yishaihalpert//Desktop//ChromeDriver"
website_url = "http://192.168.99.100:5000"
#Enter the website:
driver = webdriver.Chrome(executable_path=driver_location)
driver.maximize_window()
driver.get(website_url)
driver.implicitly_wait(30)
#Print the site text:
site_text = driver.find_element_by_xpath('/html/body').text
print(site_text)