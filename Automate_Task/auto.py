from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import json

def login(driver, un, pw):
    driver.find_element(By.ID, "loginLink").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()[contains(.,'Western Student Login')]]").click()
    time.sleep(1)

    username = driver.find_element(By.ID, "userId")
    password = driver.find_element(By.ID, "password")

    username.send_keys(un)
    password.send_keys(pw)

    driver.find_element(By.NAME, "submit").click()

def booking(driver, date, time):
    cards = driver.find_elements(By.CLASS_NAME, "thumbnail")
    for card in cards:
        if date in card.find_element(By.CLASS_NAME, "pull-left").text:
            print("Hi\n\n")
            if time in card.find_element(By.TAG_NAME, "small").text:
                print("Hi2\n\n")
                try:
                    print("Hi3\n\n")
                    item = card.find_element(By.XPATH, "//button[text()=Register]")
                    return True
                except:
                    break
    return False

def auto(cat):
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    

    driver.get("https://shop.westernmustangs.ca/Program/GetProducts?classification=d818e98b-a3ed-4636-a8be-43e4645fc87d")

    login(driver, input, input)

    driver.find_element(By.XPATH, f"//h4[text()='{cat}']").click()
    
    time.sleep(1)

    if booking(driver, "Sunday, November 21, 2021", "10:30 AM"):
        print("done")
    else: 
        print("this timeslot is either full or does not exist, please enter a new time")


    time.sleep(5)

    driver.quit()


if __name__=="__main__":
    auto("Drop In Badminton")
