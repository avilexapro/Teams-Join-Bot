import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

PATH = 'C:\Program Files (x86)\Chrome Drivers\97.0.4692.71\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://kyc.edmatix.com/login')
driver.maximize_window()

# School Code
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'orgcode')))
finally:  # After checking the presence of the element then it sends Keys to the intractable element.
    driver.find_element(By.ID, 'orgcode').send_keys('MLZEES')

# Username
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mat-input-1')))
finally:   # After checking the presence of the element then it sends Keys to the intractable element.
    driver.find_element(By.ID, 'mat-input-1').send_keys('9866482000')

# Password
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'mat-input-2')))
finally:  # After checking the presence of the element then it sends Keys to the intractable element.
    driver.find_element(By.ID, 'mat-input-2').send_keys('9866482000', Keys.ENTER)

# Avinash profile avatar
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a')))
finally:  # After checking the presence of the element then it clicks to the intractable element.
    driver.find_element(By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a').click()

# My Schedule
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button')))
finally:  # After checking the presence of the element then it clicks to the intractable element.
    driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button').click()

# Set timer till 3 seconds
time.sleep(3)

# Quits the browser
driver.quit()
