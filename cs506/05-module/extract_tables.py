from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")  # Run in headless mode 
options.add_argument("--no-sandbox")  # Bypass OS security
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(options=options)

driver.get("https://www.w3schools.com/html/html_tables.asp")

table = driver.find_element(By.ID, "customers")
rows =table.find_elements(By.TAG_NAME, "tr")

for row in rows:
    cols = row.find_elements(By.TAG_NAME, "th") + row.find_elements(By.TAG_NAME, "td")
    col_data = [col.text for col in cols]
    print(col_data)

driver.quit()  # Close the browser