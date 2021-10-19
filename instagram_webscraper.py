from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time
import csv

PATH = r"C:\Users\admin\PycharmProjects\python_projects\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

wait = W(driver, 5)

url = "https://www.instagram.com/"

driver.get(url)

user = wait.until(EC.presence_of_element_located((By.NAME, "username")))
pwd = wait.until(EC.presence_of_element_located((By.NAME, "password")))
login = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='loginForm']/div/div[3]/button")))

user.send_keys("lerasa48")
pwd.send_keys("lerasa4848")
login.click()

time.sleep(10)

try:
    saveinfo =wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Save Your Login Info?']")))
    if saveinfo:
        not_now = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        not_now.click()

    notification = wait.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='Turn on Notifications']")))

    if notification:
        not_now = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Not Now']")))
        not_now.click()
except Exception as e:
    print(e)

explore = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[3]/a")))
explore.click()

insta_data = []

driver.refresh()
time.sleep(4)

for i in range(1,4):
    for j in range(1,4):

        image_field = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[@id='react-root']/section/main/div/div[1]/div/div[{i}]/div[{j}]/div/a")))
        image_field.click() #click on image

        name_field = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div[1]/div/header/div[2]/div[1]/div[1]/span/a"))) # go to account page
        name_field.click()

        try:
            user = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[1]/h2")))
            username = user.text
        except:
            driver.execute_script("window.history.go(-1)")
            driver.execute_script("window.history.go(-1)")
            continue

        p = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[1]/span/span")))
        posts = p.text
        f = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span")))
        followers = f.text

        try:
            fg = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span")))
            following = fg.text
        except:
            following = 0
        try:
            act = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[2]/div/span")))
            acc_type = act.text
        except:
            acc_type = 'None'
        # print(username, posts, followers, following, acc_type)
        insta_data.append((username, posts, followers, following, acc_type))

        driver.execute_script("window.history.go(-1)")
        driver.execute_script("window.history.go(-1)")

driver.close()
# print(insta_data)

df = pd.DataFrame(insta_data, columns=['Username','Posts','Followers','Following','Account Type'])
# print(df)

# print(len(df.Username.unique()))
df.drop_duplicates(subset='Username', inplace=True)
# print(df.drop_duplicates(subset='Username', inplace=True))
# print(len(df.Username.unique()))

df = df.reset_index()
df.index += 1
# print(df)

df.to_csv(r"insta_data.csv", index = False, header = True)
