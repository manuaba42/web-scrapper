from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from tabulate import tabulate

web = 'https://www.vivino.com/explore?e=eJzLLbI11rNQy83MszVQy02ssDU1MFBLrrQNDVZLBhIuagW2hmrpabZliUWZqSWJOWr5RSm2avlJlbZq5SXRsUBJMGUEoYwhlIlasW1yIgASQhzB'

s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get(web)


items = driver.find_elements(By.CLASS_NAME, 'wineCard__wineCard--2dj2T')

wines = [['Name', 'Region', 'Rating']]
for item in items:
    wine = []

    name = (item.find_element(By.CLASS_NAME,'wineInfoVintage__vintage--VvWlU').text)
    region = (item.find_element(By.CLASS_NAME,'wineInfoLocation__regionAndCountry--1nEJz').text)
    # prices = item.find_element(By.CLASS_NAME,'addToCartButton__price--qJdh4')
    # for price in prices:
    #     print(price)
    rating = (item.find_element(By.CLASS_NAME,'vivinoRating_averageValue__uDdPM').text)

    wine = [name, region, rating]

    wines.append(wine)

print(tabulate(wines))

# while True:
#     continue
