from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/devinanderson/Documents/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")
f_name = driver.find_element_by_name("fName")
f_name.send_keys("Devin")
l_name = driver.find_element_by_name("lName")
l_name.send_keys("Anderson")
email = driver.find_element_by_name("email")
email.send_keys("nostro37@gmail.com")

send = driver.find_elements_by_css_selector(".form-signin button")[0]
send.click()