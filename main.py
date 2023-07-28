import pickle
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import parameters
driver = webdriver.Chrome()
companies_list=[]
users_list = []

#to load saved cookies if present for username
def load_cookie(driver,username):
    with open(username+'.pkl', 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)
    return driver
#saving cookies file for user
def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

#function to login to account
def login(driver):
    # waiting for the page to load
    time.sleep(5)
    #entering username
    username=driver.find_element(By.XPATH, '//input[@aria-label="Phone number, username, or email"]')
    username.send_keys(parameters.username)
    # entering  password
    password = driver.find_element(By.XPATH, '//input[@aria-label="Password"]')
    password.send_keys(parameters.password)
    time.sleep(4)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(6)
    path=parameters.username+'.pkl'
    save_cookie(driver,path)
    time.sleep(200)


def main(driver):
    driver.get("https://www.instagram.com/")
    try:
        load_cookie(driver,parameters.username)
    except:
        login(driver)
    driver.get("https://www.instagram.com/")
    time.sleep(6)
    main_div = driver.find_element(By.XPATH, '//div[@class="xvb8j5 x1vjfegm"]')

    butttons=main_div.find_elements(By.XPATH, '//div[@class="x1n2onr6"]')

    for button in butttons:
        value=button.find_element(By.TAG_NAME,'a').get_attribute('href')
        if value=='https://www.instagram.com/#':
            button.click()
            break
    time.sleep(6)
    driver.find_element(By.XPATH, '//input[@aria-label="Search input"]').send_keys(parameters.location)
    time.sleep(5)
    all_searches=driver.find_elements(By.XPATH, '//div[@role="none"]')
    for search in all_searches:
        search_results=search.find_element(By.TAG_NAME,'a').get_attribute('href')
        if 'https://www.instagram.com/explore/locations/' in search_results:
            search.click()
            break
    time.sleep(10)


main(driver)
# loggin()