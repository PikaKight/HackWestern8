from selenium import webdriver

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://shop.westernmustangs.ca/Program/GetProducts?classification=d818e98b-a3ed-4636-a8be-43e4645fc87d")

print(driver.title)
driver.quit()