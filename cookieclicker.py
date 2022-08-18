from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# my_money = driver.find_element(By.XPATH, '//*[@id="money"]')

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')

# Get item IDs:
items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

# Timeout:
timeout = time.time() + 2
five_min = time.time() + 60*5

# Vjezbanje:
# all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
# for price in range(0, len(all_prices)):
#     print(all_prices[price].text)
# item_prices = []
# for price in all_prices:
#     element_text = price.text
#     if element_text != "":
#         cost = int(element_text.split("-")[1].strip().replace(",",""))
#         item_prices.append(cost)
# cookie_upgrades = {}
# for n in range(len(item_prices)):
#     cookie_upgrades[item_prices[n]] = item_ids[n]
# print(cookie_upgrades)

# my_money = driver.find_element(By.XPATH, '//*[@id="money"]').text
# if "," in my_money:
#     my_money = my_money.replace(",","")
# cookie_count = int(my_money)
# print(cookie_count)


while True:
    cookie.click()
    # Trigger every 5 seconds to check if u have enough money:
    if time.time() > timeout:
        # Get all upgrade <b> tags:
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",",""))
                item_prices.append(cost)
        cookie_upgrades = {}

        # Creating dictionary of items and prices:
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count:
        my_money = driver.find_element(By.XPATH, '//*[@id="money"]').text
        if "," in my_money:
            my_money = my_money.replace(",","")
        cookie_count = int(my_money)

        # Find affordable upgrades:
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        timeout = time.time()+5

    if time.time() >five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break





