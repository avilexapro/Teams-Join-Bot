import datetime  # Gets 'datetime' for getting time.
import pyautogui  # Gets 'pyautogui' for automating the click and keys.
from time import sleep  # Gets 'Sleep' and sets timer.
from selenium import webdriver  # Gets the webdriver.
from selenium.webdriver.common.by import By  # Set of supported locator strategies.
from selenium.webdriver.common.keys import Keys  # Gets the 'Keys' to send to the element.
from selenium.webdriver.support.ui import WebDriverWait  # Gets 'WebDriverWait' for better use then time.sleep().
from selenium.webdriver.support import expected_conditions as EC  # Canned 'Expected Conditions' which are generally.

choose = int(input('You want auto press 1 or manual press 2: '))  # Asks the user for automatic login or manual.
if choose == 1:
    print('There is no option like that.')

elif choose == 2:
    class_select = int(input('What class do you want: '))  # If choose manual then it will ask which class to join.

else:
    print('Invalid option!')
    exit()

driver = webdriver.Chrome('C:\Program Files (x86)\Chrome Drivers\97.0.4692.71\chromedriver.exe')  # Gets the variable from the env and for chrome driver.
time = (datetime.datetime.now().hour, datetime.datetime.now().minute)  # Gets hour and minute and sets it in a variable.

driver.get('https://kyc.edmatix.com/login')  # Gets the website.
driver.maximize_window()  # Maximizes the window of the browser

button_one = '//*[@id="table-scroll"]/table/tbody/tr[1]/td[4]/button'  # XPath of first class in edmatix schedule.
button_two = '//*[@id="table-scroll"]/table/tbody/tr[3]/td[4]/button'  # XPath of second class in edmatix schedule.
button_three = '//*[@id="table-scroll"]/table/tbody/tr[2]/td[4]/button'  # XPath of third class in edmatix schedule.
button_four = '//*[@id="table-scroll"]/table/tbody/tr[4]/td[4]/button'  # XPath of forth class in edmatix schedule.
button_five = '//*[@id="table-scroll"]/table/tbody/tr[5]/td[4]/button'  # XPath of fifth class in edmatix schedule.
button_six = '//*[@id="table-scroll"]/table/tbody/tr[6]/td[4]/button'  # XPath of sixth class in edmatix schedule.


# The functions if for joining the first class.
def first_button():
    try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_one)))
    finally:  # After checking the presence of the element then it clicks to the intractable element.
        driver.find_element(By.XPATH, button_one).click()


# The functions if for joining the second class.
def second_period():
    try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_two)))
    finally:  # After checking the presence of the element then it clicks to the intractable element.
        driver.find_element(By.XPATH, button_two).click()


# The functions if for joining the third class.
def third_period():
    try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_three)))
    finally:  # After checking the presence of the element then it clicks to the intractable element.
        driver.find_element(By.XPATH, button_three).click()


# The functions if for joining the forth class.
def forth_period():
    try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_four)))
    finally:  # After checking the presence of the element then it clicks to the intractable element.
        driver.find_element(By.XPATH, button_four).click()


# The functions if for joining the fifth class.
def fifth_period():
    try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_five)))
    finally:  # After checking the presence of the element then it clicks to the intractable element.
        driver.find_element(By.XPATH, button_five).click()


# The functions if for joining the sixth class.
def sixth_period():
    try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, button_six)))
    finally:  # After checking the presence of the element then it clicks to the intractable element.
        driver.find_element(By.XPATH, button_six).click()


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
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a')))
finally:  # After checking the presence of the element then it clicks to the intractable element.
    driver.find_element(By.XPATH, '//*[@id="app"]/header/nav/div/div[1]/ul/li[2]/a').click()

# My Schedule
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button')))
finally:  # After checking the presence of the element then it clicks to the intractable element.
    driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[10]/button').click()

if choose == 1:  # This is activated when user chased auto method to sign in.
    if time <= (8, 40) or time <= (8, 55):  # This checks the time and then join the call.
        first_button()

    elif time <= (9, 00) or time <= (9, 50):  # This checks the time and then join the call.
        second_period()

    elif time <= (10, 00) or time <= (10, 50):  # This checks the time and then join the call.
        third_period()

    elif time <= (11, 00) or time <= (11, 50):  # This checks the time and then join the call.
        forth_period()

    elif time <= (12, 00) or time <= (12, 50):  # This checks the time and then join the call.
        fifth_period()

    elif time <= (14, 00) or time <= (15, 00):  # This checks the time and then join the call.
        sixth_period()

    else:
        print('No class found at this moment')  # Prints 'There is no class today' if no class in the time is found.
        driver.quit()  # If not found it quits the browser.
        exit()  # Then exits the code.

if choose == 2:  # This is activated when user chased manual method to sign in.
    # noinspection PyUnboundLocalVariable
    if class_select == 1:  # This checks the time and then join the call.
        first_button()

    elif class_select == 2:  # This checks the time and then join the call.
        second_period()

    elif class_select == 3:  # This checks the time and then join the call.
        third_period()

    elif class_select == 4:  # This checks the time and then join the call.
        forth_period()

    elif class_select == 5:  # This checks the time and then join the call.
        fifth_period()

    elif class_select == 6:  # This checks the time and then join the call.
        sixth_period()

    else:
        print(f'No class found by this number {class_select}')  # That there is no class of this number given by the user.
        driver.quit()  # If not found it quits the browser.
        exit()  # Then exits the code.

# Allowing chrome to open teams
try:  # This waits and checks for 10 seconds for the presence for the element it is better than using Time.Sleep().
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/script[3]')))
finally:  # Waits for 2.5 seconds and then clicks the 'Open Microsoft Teams' button.
    sleep(2.5)
    pyautogui.leftClick(1036, 225)

# Sets timer till 1 seconds
sleep(1)

# Quits the browser
driver.quit()

# Turning off the mic
sleep(10)

if pyautogui.pixel(605, 590) == (158, 162, 255):  # Gets the RGB color code of X = 1059, Y = 452 and checks it with the given RGB value.
    pyautogui.leftClick(605, 590)  # if true it clicks the mic button otherwise it directly clicks the join button.

if pyautogui.pixel(1059, 452) == (158, 162, 255):  # Gets the RGB color code of X = 1059, Y = 452 and checks it with the given RGB value.
    pyautogui.leftClick(1061, 456)  # if true it clicks the mic button otherwise it directly clicks the join button.

if pyautogui.pixel(1317, 643) == (255, 245, 232):  # Gets the RGB color code of X = 1059, Y = 452 and checks it with the given RGB value.
    pyautogui.leftClick(1317, 643)  # if true it clicks the mic button otherwise it directly clicks the join button.

else:
    exit()

sleep(4)
if pyautogui.pixel(1565, 36) == (66, 66, 66):
    pyautogui.leftClick(1565, 36)

else:
    print('You joined the class.')
