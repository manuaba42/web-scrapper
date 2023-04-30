from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from tabulate import tabulate
import time

web = 'https://www.vivino.com/explore?e=eJzLLbI11rNQy83MszVQy02ssDU0UEuutHV3UksGEgFqBbaGaulptmWJRZmpJYk5avlFKbZq-UmVtmrlJdGxQEkwZQQADKcWTg%3D%3D'
s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get(web)

driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(9) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > label:nth-child(4) > div:nth-child(1) > input:nth-child(1)").click()
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)'))).click()
WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shipToDropdown_itemLink__7h3Co[data-value='gb']"))).click()

time.sleep(5)
slider1 = driver.find_element(By.XPATH, "//div[@class='rc-slider-handle rc-slider-handle-1']")
slider2 = driver.find_element(By.XPATH, "//div[@class='rc-slider-handle rc-slider-handle-2']")
# ActionChains(driver).drag_and_drop_by_offset(slider1, 0, 0).perform()
ActionChains(driver).click_and_hold(slider1).pause(1).move_by_offset(-50,0).release().perform()
# ActionChains(driver).drag_and_drop_by_offset(slider2, 25, 0).perform()
ActionChains(driver).click_and_hold(slider2).pause(1).move_by_offset(-75,0).release().perform()

time.sleep(5)

reached_page_end = False
last_height = driver.execute_script("return document.body.scrollHeight")

while not reached_page_end:
    driver.execute_script("window.scrollBy(0, 10000);")

    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if last_height == new_height:
        reached_page_end = True
    else:
        last_height = new_height

items = driver.find_elements(By.CLASS_NAME, "wineCard__wineCard--2dj2T")
# print(items)
wines = [['Name', 'Region', 'Price',  'Rating']]
for item in items:
    wine = []

    name = (item.find_element(By.CLASS_NAME,'wineInfoVintage__vintage--VvWlU').text) 
    region = (item.find_element(By.CLASS_NAME,'wineInfoLocation__regionAndCountry--1nEJz').text)
    prices = item.find_element(By.CSS_SELECTOR, "div[class='addToCartButton__price--qJdh4'] div:nth-child(2)").text
    rating = (item.find_element(By.CLASS_NAME,'vivinoRating_averageValue__uDdPM').text)

    if float(rating) >= 3.7:
        wine = [name, region, prices, rating]

        wines.append(wine)

print(tabulate(wines))

while True:
    continue
