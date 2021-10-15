from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import csv
import time
import pandas as pd

def get_url(search):
    """Generate a url from search area"""
    template = "https://www.amazon.com/s?k={}&ref=nb_sb_noss_1"
    search = search.replace(" ", "+")

    url = template.format(search)
    url += "&page={}"
    return url

def extract_record(item):
    # description and url
    item_tag = item.h2.a
    desc = item_tag.text.strip()
    url = "https://www.amazon.com" + item_tag.get("href")

    try:
        # price
        price = item.find("span", "a-price")
        item_price = price.find("span", "a-offscreen").text
    except AttributeError:
        return

    try:
        # rating and review count
        rating = item.i.text
        review_count = item.find("span", {"class" : "a-size-base"}).text
    except AttributeError:
        rating = ""
        review_count = ""

    result = (desc, item_price, rating, review_count, url)
    return result

def main(search):
    url = "https://www.amazon.com/"
    url = get_url(search)
    # print(url)

    records = []
    for page in range(1, 11):
        driver = webdriver.Chrome()
        driver.get(url.format(page))

        soup = bs(driver.page_source, "html.parser")
        results = soup.find_all("div", {"data-component-type" : "s-search-result"})
        # print(len(results)

        for result in results:
            record = extract_record(result)
            if record:
                records.append(record)

        driver.close()

        # save to file
        with open("myrecords.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['Description', "Price", "Rating", "Review Count", "URL"])
            writer.writerows(records)

main("lg mobiles")
