from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")  # Run in headless mode
options.add_argument("--disable-gpu")  # Disable GPU acceleration

driver = webdriver.Chrome(options=options)
driver.get("https://www.example.com")

print(driver.title)  # Print the title of the page
driver.save_screenshot("screenshot.png")  # Save a screenshot of the page

driver.quit()  # Close the browser