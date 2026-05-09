from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
print("Starting browser...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
print("Opening YouTube...")
driver.get("https://www.youtube.com")
time.sleep(5)
try:
    print("Trying to open Shorts...")
    shorts_link = driver.find_element(By.XPATH, "//a[@title='Shorts']")
    shorts_link.click()
    print("Shorts opened")
    time.sleep(5)
    for i in range(10):
        print(f"Watching short {i+1}")
        time.sleep(10)
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ARROW_DOWN)
except Exception as e:
    print("ERROR OCCURRED:", e)
print("Closing browser")
driver.quit()