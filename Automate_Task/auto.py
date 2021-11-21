from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json

def login(driver):
    driver.find_element(By.ID, "loginLink").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()[contains(.,'Western Student Login')]]").click()
    time.sleep(1)

    username = driver.find_element(By.ID, "userId")
    password = driver.find_element(By.ID, "password")

    username.send_keys(input())
    password.send_keys(input())

    driver.find_element(By.NAME, "submit").click()
    
def auto():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    

    driver.get("https://shop.westernmustangs.ca/Program/GetProducts?classification=d818e98b-a3ed-4636-a8be-43e4645fc87d")

    login(driver)

    try:
        elem = WebDriverWait(driver, 10).unit(
            EC.element_to_be_clickable((By.XPATH, "div[@onclick=window.location='/Program/GetProgramDetails?courseId=4cbf8cd1-3fca-4e35-b331-a8dbb9b5a86f&semesterId=81dac0e7-2456-44c9-bfe4-6ed494cc6824']")).click()
        )
    except:
<<<<<<< HEAD
        time.sleep(5)
        
=======
        time.sleep(30)
>>>>>>> eb5bcb9c591bb3b0c7f0b88ac68e4ed46d129de8
        driver.quit()


if __name__=="__main__":
    auto()
