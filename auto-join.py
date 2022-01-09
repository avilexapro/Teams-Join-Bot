import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'C:\Program Files (x86)\Chrome Drivers\97.0.4692.71\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://kyc.edmatix.com/login')
driver.maximize_window()

driver.find_element(By.ID, 'orgcode').send_keys('MLZEES')
driver.find_element(By.ID, 'mat-input-1').send_keys('9866482000')
driver.find_element(By.ID, 'mat-input-2').send_keys('9866482000', Keys.ENTER)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a')))
finally:
    driver.find_element(By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a').click()

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button')))
finally:
    driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button').click()

time.sleep(3)

driver.quit()
