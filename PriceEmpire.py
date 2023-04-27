from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
driver = webdriver.Chrome()
driver.get("https://pricempire.com/live")
time.sleep(50)

İtemBox=[]
Cards = driver.find_elements(By.CLASS_NAME ,"select")

for kart in Cards:
    İtem_Name = kart.find_elements(By.TAG_NAME ,"item-name")[0].text
    item_Price = kart.find_elements(By.TAG_NAME ,"item-price")[0].text
  
    İtemBox.append(İtem_Name)
    İtemBox.append(item_Price)

    for x in range(len(İtemBox)):
        print(İtemBox[x])

time.sleep(30)
driver.quit()
