from time import sleep  # Gets 'Sleep' and sets timer.
from selenium import webdriver  # Gets the webdriver.
from selenium.webdriver.common.by import By  # Set of supported locator strategies.
from selenium.webdriver.common.keys import Keys  # Gets the 'Keys' to send to the element.
from selenium.webdriver.support.ui import WebDriverWait  # Gets 'WebDriverWait' for better use then time.sleep().
from selenium.webdriver.support import expected_conditions as EC  # Canned 'Expected Conditions' which are generally useful within webdriver.

PATH = 'C:\Program Files (x86)\Chrome Drivers\97.0.4692.71\chromedriver.exe'  # Gets the path to the chrome driver.
driver = webdriver.Chrome(PATH)  # Sets the variable and chrome as the browser.

driver.get('https://kyc.edmatix.com/login')  # Gets the website.
driver.maximize_window()  # maximizes the window of the browser

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

# Set timer till 3 seconds
sleep(5)

# Quits the browser
driver.quit()
