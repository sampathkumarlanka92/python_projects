from bs4 import BeautifulSoup as bs
from selenium import webdriver
import pandas as pd
import requests
import time

allquotes = []
for i in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{i}"

    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(url)

    time.sleep(3)

    soup = bs(driver.page_source, "html.parser")
    pagesource = soup.prettify()

    # with open("pagesource.txt", "w", encoding="utf-8") as f:
    #     f.write(pagesource)

    title = soup.title.text
    # print(title)

    quote_full = soup.find_all("div", class_="quote")
    # print(quote_full)
    for quotes in quote_full:
        quote = quotes.find("span", class_="text").text
        author = quotes.find("small", class_="author").text
        tags_full = quotes.find("div", class_="tags")
        tags_all = tags_full.find_all("a")
        # print(quote)
        # print(author)
        # print(tags_full)
        # print(tags_all)
        tags = []
        for tag in tags_all:
            tags.append(tag.text)
        # print(tags)

        single = [quote, author, tags]
        allquotes.append(single)

    driver.close()

df = pd.DataFrame(allquotes, columns=['quotes', 'author', 'tags'])
df.to_csv('quotes.csv', index=False, encoding="utf-8")
