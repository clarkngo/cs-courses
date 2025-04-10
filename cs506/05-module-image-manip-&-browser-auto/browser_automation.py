from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')  # run in headless mode
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)
driver.get('https://example.com')

print(driver.title)
driver.save_screenshot("screenshot.png")

driver.quit()

