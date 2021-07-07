from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/devinanderson/Documents/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_articles = driver.find_element_by_css_selector("#articlecount a")
#number_of_articles.click()

all_portals = driver.find_element_by_link_text("All portals")

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)