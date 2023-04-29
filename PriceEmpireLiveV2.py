from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
#options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
driver.get("https://pricempire.com/live")
time.sleep(50)

İtemBox=[]
Cards = driver.find_elements(By.CLASS_NAME ,"select")

for kart in Cards:

    Weapon_name = ""    
    Skin_Name = ""
    item_Price = ""
    Profit =""
    Roi=""
    Sell_Price=""

    weapon_names = kart.find_elements(By.CLASS_NAME ,"weapon-name")
    skin_names = kart.find_elements(By.CLASS_NAME ,"skin-name")
    item_prices = kart.find_elements(By.TAG_NAME ,"item-price")
    Profit = kart.find_elements(By.CSS_SELECTOR ,".red span:nth-of-type(2)")[0].text
    Roi = kart.find_elements(By.CSS_SELECTOR ,"div.percentage")[0].text
    Sell_Price = kart.find_elements(By.CSS_SELECTOR ,"price[_ngcontent-serverapp-c89] span:nth-of-type(2)")[0].text


    if weapon_names:
        Weapon_name = weapon_names[0].text
    if skin_names:
        Skin_Name = skin_names[0].text
    if item_prices:
        item_Price = item_prices[0].text

    İtemBox.append(Weapon_name)
    İtemBox.append(Skin_Name)
    İtemBox.append(item_Price)
    İtemBox.append(Profit)
    İtemBox.append(Roi)
    İtemBox.append(Sell_Price)

    for i in range(0, len(İtemBox), 6):
        print("Weapon Name: {} // Skin Name: {} // Anlık Satış Fiyatı: {} // Kaar: {} // Roi: {} // Satış Fiyatı: {}".format(İtemBox[i], İtemBox[i+1], İtemBox[i+2], İtemBox[i+3], İtemBox[i+4], İtemBox[i+5]))


time.sleep(90)
