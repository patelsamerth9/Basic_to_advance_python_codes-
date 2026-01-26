from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
def start_browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.instagram.com/")
    print("Please Log in manually in the browser window within 60 seconds...")
    time.sleep(60)
    driver.get("https://www.instagram.com/reels/")
    time.sleep(5)
    try:
        body_elem = driver.find_element(By.TAG_NAME, 'body')
        while True:
            body_elem.send_keys(Keys.DOWN)
            sleep_time = random.randint(10, 25)
            print(f"Scrolling in {sleep_time} seconds...")
            time.sleep(sleep_time)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()
if __name__ == "__main__":
    start_browser()