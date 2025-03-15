from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select  # for interacting with dropdowns
from selenium.webdriver.support.ui import WebDriverWait  # for explicit waits
from selenium.webdriver.support import expected_conditions as EC
import time  # increase wait time for debugging

browser = webdriver.Chrome()
browser.get("https://accounts.google.com/signup")

# Find input id = "firstName" and fill "Thomas" as firstname
firstname = browser.find_element(By.ID, 'firstName')
firstname.send_keys('Thomas')
time.sleep(2)

# Find input id = "lastName" and fill "Anderson" as lastname
lastname = browser.find_element(By.ID, "lastName")
lastname.send_keys("Anderson")
time.sleep(2)

# Locate the next button and transition to the next form
browser.find_element(By.ID, "collectNameNext").click()
time.sleep(2)

# Enter the date of birth details
day = browser.find_element(By.NAME, "day")
day.send_keys('1')
time.sleep(2)

# Select options from the Month dropdown
month = Select(browser.find_element(By.ID, "month"))
month.select_by_visible_text('January')
time.sleep(2)
# Enter the year of birth
year = browser.find_element(By.NAME, "year")
year.send_keys("1990")
time.sleep(2)

# Enter the gender
gender = Select(browser.find_element(By.ID, "gender"))
gender.select_by_visible_text("Male")
time.sleep(2)

# Locate the next button and transition to the next form
browser.find_element(By.ID, "birthdaygenderNext").click()
time.sleep(2)

# Enter a username
username = browser.find_element(By.NAME, "Username")
username.send_keys("thomasanderson111990")
time.sleep(2)

# Locate the next button and transition to the next form
browser.find_element(By.ID, "next").click()

# Enter password and confirm password
# We are waiting for Google to verify the email and then show the input field
# So an explicit wait is needed here to wait for a certain condition to occur before proceeding
# In this case, it is the visibility of the password input field.

passwd = WebDriverWait(browser, 60).until(EC.visibility_of_element_located((By.NAME, "Passwd")))
passwd.send_keys("ThomAnd1190")

passwd = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.NAME, "PasswdAgain")))
passwd.send_keys("ThomAnd1190")
time.sleep(2)

browser.find_element(By.ID, "createpasswordNext").click()
time.sleep(3)
