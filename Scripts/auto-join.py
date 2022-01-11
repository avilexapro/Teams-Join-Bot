import datetime
import pyautogui  # Gets 'pyautogui' for automating the click and keys.
from time import sleep  # Gets 'Sleep' and sets timer.
from selenium import webdriver  # Gets the webdriver.
from selenium.webdriver.common.by import By  # Set of supported locator strategies.
from selenium.webdriver.common.keys import Keys  # Gets the 'Keys' to send to the element.
from selenium.webdriver.support.ui import WebDriverWait  # Gets 'WebDriverWait' for better use then time.sleep().
from selenium.webdriver.support import expected_conditions as EC  # Canned 'Expected Conditions' which are generally.

PATH = 'C:\Program Files (x86)\Chrome Drivers\97.0.4692.71\chromedriver.exe'  # Gets the path to the chrome driver.
driver = webdriver.Chrome(PATH)  # Sets the variable and chrome as the browser.
hour = datetime.datetime.now().hour

driver.get('https://kyc.edmatix.com/login')  # Gets the website.
driver.maximize_window()  # maximizes the window of the browser


class buttons:
    button_one = '//*[@id="table-scroll"]/table/tbody/tr[2]/td[4]/button'
    button_two = '//*[@id="table-scroll"]/table/tbody/tr[4]/td[4]/button'
    button_three = '//*[@id="table-scroll"]/table/tbody/tr[3]/td[4]/button'
    button_four = '//*[@id="table-scroll"]/table/tbody/tr[5]/td[4]/button'
    button_five = '//*[@id="table-scroll"]/table/tbody/tr[6]/td[4]/button'


class periods:
    @staticmethod
    def first_button():
        try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, buttons.button_one)))
        finally:  # After checking the presence of the element then it clicks to the intractable element.
            driver.find_element(By.XPATH, buttons.button_one).click()

    @staticmethod
    def second_period():
        try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, buttons.button_two)))
        finally:  # After checking the presence of the element then it clicks to the intractable element.
            driver.find_element(By.XPATH, buttons.button_two).click()

    @staticmethod
    def third_period():
        try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, buttons.button_two)))
        finally:  # After checking the presence of the element then it clicks to the intractable element.
            driver.find_element(By.XPATH, buttons.button_two).click()

    @staticmethod
    def forth_period():
        try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, buttons.button_four)))
        finally:  # After checking the presence of the element then it clicks to the intractable element.
            driver.find_element(By.XPATH, buttons.button_four).click()

    @staticmethod
    def fifth_period():
        try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, buttons.button_five)))
        finally:  # After checking the presence of the element then it clicks to the intractable element.
            driver.find_element(By.XPATH, buttons.button_five).click()


# School Code
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'orgcode')))
finally:  # After checking the presence of the element then it sends Keys to the intractable element.
    driver.find_element(By.ID, 'orgcode').send_keys('MLZEES')

# Username
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mat-input-1')))
finally:  # After checking the presence of the element then it sends Keys to the intractable element.
    driver.find_element(By.ID, 'mat-input-1').send_keys('9866482000')

# Password
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mat-input-2')))
finally:  # After checking the presence of the element then it sends Keys to the intractable element.
    driver.find_element(By.ID, 'mat-input-2').send_keys('9866482000', Keys.ENTER)

# Avinash profile avatar
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a')))
finally:  # After checking the presence of the element then it clicks to the intractable element.
    driver.find_element(By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a').click()

# My Schedule
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button')))
finally:  # After checking the presence of the element then it clicks to the intractable element.
    driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button').click()

if hour == 18:
    periods.first_button()

elif hour == 19:
    periods.second_period()

elif hour == 20:
    periods.third_period()

elif hour == 21:
    periods.forth_period()

elif hour == 22:
    periods.fifth_period()

else:
    exit()

# Allowing chrome to open teams
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/script[3]')))
finally:  # Waits for 2.5 seconds and then clicks the 'Open Microsoft Teams' button.
    sleep(2.5)
    pyautogui.click(1036, 225)

# Sets timer till 3 seconds
sleep(1)

# Quits the browser
driver.quit()

# Turning off the mic
sleep(3)

posXY = pyautogui.position(1059, 452)
pos_color = (158, 162, 255)
test = pyautogui.pixel(posXY[0], posXY[1])

if test == pos_color:
    pyautogui.click(1061, 456)

else:
    pyautogui.click(1323, 645)

sleep(2)
pyautogui.click(1323, 645)

sleep(2)
exit()
