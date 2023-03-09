
import requests
from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get('https://www.linkedin.com/home')
driver.maximize_window()
name_username = driver.find_element(By.ID,"session_key")
name_password = driver.find_element(By.NAME,"session_password")
name_username.click()
name_username.send_keys('keerthimom5984@gmail.com')
name_password.click()
name_password.send_keys('keerthi123')
name_signin=driver.find_element(By.CLASS_NAME,'sign-in-form__submit-btn--full-width')
name_signin.click()
time.sleep(5)
url=driver.current_url
name_search=driver.find_element(By.CLASS_NAME,'search-global-typeahead__input')
time.sleep(5)
name_search.click()
name_search.send_keys('layoffs')
name_search.click()
# html=requests.get(url)
# doc = BeautifulSoup(html.content,"html.parser")
# print('hi')
# print(doc)


