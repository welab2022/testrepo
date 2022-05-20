from selenium import webdriver
from selenium.webdriver.chrome.service import Service


USERNAME = 'hung'
PASSWORD = '12345'

s = Service("C:/Users/conbo/ChromeDriver/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get('http://127.0.0.1:5500/Test/login.html')

user_input = driver.find_element_by_id('user-name')
user_input.send_keys(USERNAME)

password_input = driver.find_element_by_id('password')
password_input.send_keys(PASSWORD)

login_button = driver.find_element_by_id('login-button')
login_button.click()
driver.close()
