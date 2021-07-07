import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/Users/devinanderson/Documents/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element_by_id("money")
COOKIE_MONEY = int(money.text)


def clicker():
    while COOKIE_MONEY < 1000000:
        cookie_click = driver.find_element_by_id("cookie")
        cookie_click.click()
        if COOKIE_MONEY > 14000:
            purchase_option = driver.find_element_by_id("buyShipment")
            purchase_option.click()
    print(COOKIE_MONEY)


clicker()
clicker()
clicker()