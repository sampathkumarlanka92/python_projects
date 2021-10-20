from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
import time
import csv

PATH = r"C:\Users\admin\PycharmProjects\python_projects\chromedriver.exe"
service = Service(PATH)

options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(service=service, options=options)

wait = W(driver, 5)

url = "https://www.facebook.com/"

driver.get(url)
time.sleep(2)

# Login
user = wait.until(EC.presence_of_element_located((By.ID, "email")))
pwd = wait.until(EC.presence_of_element_located((By.ID, "pass")))

user.send_keys("lerasa4855@wawue.com")
pwd.send_keys("lerasa48")
# pwd.send_keys(Keys.RETURN)
login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]")))
login.click()

time.sleep(20)

# Search Keywords
s = "python programming"
search = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[aria-label='Search Facebook']")))
search.send_keys(s)
search.send_keys(Keys.RETURN)

time.sleep(3)
# print(driver.current_url)
soup = bs(driver.page_source, "html.parser")
search_results = soup.find_all("span", {"class" : "nc684nl6"})
# print(len(search_results))
# print(search_results)


# Log Out
acct = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[aria-label=Account]")))
acct.click()

time.sleep(2)

l = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v ekzkrbhg oo9gr5id hzawbc8m']")))
logout = l[4]
logout.click()

time.sleep(5)

driver.close()

data = []
for result in search_results:
    title = result.text
    fburl = result.find("a")
    fb_url = fburl.get("href")
    r = (title, fb_url)
    data.append(r)

# print(data)

with open("fb_search.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL"])
    writer.writerows(data)
