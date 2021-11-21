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

    driver.find_element(By.XPATH, "//h4[text()='*Fitness Centre Entrance Reservation']").click()
    
    time.sleep(30)

    driver.quit()


if __name__=="__main__":
    auto()
