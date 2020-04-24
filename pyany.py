import selenium
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
import getpass

input_username = input("Username/Email: ")
input_password = getpass.getpass(prompt='Password: ') 

#username = 'leine.tee1@gmail.com'
#password = 'Penguin12!!'
username = input_username
password = input_password

#Headless chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("/Users/vagif/Downloads/chromedriver",options=chrome_options)
driver.get('https://www.pythonanywhere.com/login/?next=/')

try:
    name = driver.find_element_by_xpath("//input[@name='auth-username']").send_keys(username)
    password = driver.find_element_by_xpath("//input[@name='auth-password']").send_keys(password)
    btn = driver.find_element_by_id("id_next").click()
    web = driver.find_element_by_id('id_web_app_link').click()
    driver.execute_script("document.getElementsByTagName('input')[5].click()")
except:
    print('Username/password incorrect.')


print('Complete')
