from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()
browser.get('https://orteil.dashnet.org/cookieclicker/')


time.sleep(5)


toggle_box = browser.find_element(By.XPATH, '//*[@id="toggleBox"]')
toggle_box.click()

cookie = browser.find_element(By.ID, 'bigCookie')
cookie.click()


browser.quit()

