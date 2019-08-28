#Import Required Packages:
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
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
