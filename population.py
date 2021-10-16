from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import time
import csv
import pandas as pd


def get_records(countries):
    records = []

    for i in range(0, 236):

        result = countries[i].find_all("td")
        record = []
        for r in result:
            record = list(record)
            record.append(r.text)
            record = tuple(record)

        records.append(record)
    return records

def main():
    url = "https://www.worldometers.info/world-population/population-by-country/"

    req = requests.get(url)
    soup = bs(req.text, "html.parser")

    countries = soup.find_all("tr")

    records = get_records(countries)

    # dataframe and save to .xlsx file
    cols = [
        "Rank",
        "Country",
        "Population (2020)",
        "Yearly Change",
        "Net Change",
        "Density (P/SqKm)",
        "Land Area (SqKm)",
        "Migrants (net)",
        "Fert Rate",
        "Med Age",
        "Urban Papulation %",
        "World Share"
    ]
    df = pd.DataFrame(records, columns=cols)
    df.to_excel("population.xlsx", index=False)

if __name__ == "__main__":
    main()
