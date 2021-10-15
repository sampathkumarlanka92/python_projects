from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import pandas as pd

def main_url(driver, s, l):
    # identify keywords element and send keys - keywords
    keyword = driver.find_element_by_id("qsb-keyword-sugg")
    keyword.send_keys(s)

    # identify location element and send keys - location
    location = driver.find_element_by_id("qsb-location-sugg")
    location.send_keys(l)
    location.send_keys(Keys.RETURN)

    # identify search button and press
    # search = driver.find_element_by_class("search-btn")
    # search.send_keys(Keys.RETURN)

    # sleep time
    time.sleep(10)

    # get cur url
    cur_url = driver.current_url
    cur_url += "-{}"
    return cur_url

def extract_record(job):

    jtitle = job.select("div > a")
    try:
        job_title = jtitle[0].text        # title
        comp_name = jtitle[1].text        # company name
        review_count = jtitle[2].text     # review count
        job_url = jtitle[0].get("href")   # job url
    except IndexError:
        job_title = jtitle[0].text        # title
        comp_name = jtitle[1].text        # company name
        review_count = "No Reviews"       # review count
        job_url = jtitle[0].get("href")   # job url

    ktitle = job.select("div > ul > li")
    exp = ktitle[0].text                   # experienc
    sal = ktitle[1].text                   # salary
    loc = ktitle[2].text                   # location


    # print(ktitle)
    record = (job_title, comp_name, exp, sal, loc, review_count, job_url)
    return record


def main():
    s = input("Enter keyword to search: ")
    l = input("Enter location to search: ")

    # s = "python"
    # l = "hyderabad"

    url = "https://www.naukri.com/"
    records = []

    driver = webdriver.Chrome()
    # url
    driver.get(url)

    url = main_url(driver, s, l)
    # print(url)
    # length=0
    for page in range(1, 3):
        driver.get(url.format(page))
        time.sleep(10)
        soup = bs(driver.page_source, "html.parser")
        jobs = soup.find_all("div", {"class" : "jobTupleHeader"})
        # length += len(jobs)
    # print(length)

        for job in jobs:
            # print(job)
            record = extract_record(job)
            if record:
                records.append(record)

        with open("mynaukrijobs.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['JobTitle', "Company", "Experience", "Salary", "Location", "Review Count", "Job URL"])
            writer.writerows(records)

    driver.close()
    # print(records)

main()
