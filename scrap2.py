from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

web = 'https://www.vivino.com/explore?e=eJzLLbI11rNQy83MszVQy02ssDU1MFBLrrQNDVZLBhIuagW2hmrpabZliUWZqSWJOWr5RSm2avlJlbZq5SXRsUBJMGUEoYwhlIlasW1yIgASQhzB'
# path = '/usr/local/bin/chromedriver'
# driver = webdriver.Chrome()
s = Service('usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get(web)


items = driver.find_elements(By.CLASS_NAME, 'wineCard__wineCard--2dj2T')
# items = driver.find_elements(By.XPATH, "//div[contains(@class, 'wineCard__wineCard--2dj2T')]")
# print(items)
for item in items:
    name = item.find_element(By.CLASS_NAME,'wineInfoVintage__vintage--VvWlU').text
    # name = item.find_element(By.XPATH, "//div[contains(@class, 'wineInfoVintage__truncate--3QAtw')]").text
    # item.find_element(By.XPATH("//div[@class='notesData']/div[@class='notesDate']")).getText()
    print(name)

while True:
    continue
