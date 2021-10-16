from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import pandas as pd

main_url = "https://stackoverflow.com/"

driver = webdriver.Chrome()
driver.get(main_url)
time.sleep(3)

soup = bs(driver.page_source, "html.parser")
urls = soup.find_all("a")

driver.close()

urls_all = []
for url in urls:
    l = url.get("href")
    try:
        if "https" in l:
            link = (l,)
            urls_all.append(link)
            # print(link)
    except TypeError:
        pass
# print(urls_all)

with open("mylinks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Links in Stackoverflow"])
    writer.writerows(urls_all)
