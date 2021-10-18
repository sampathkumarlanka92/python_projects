from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import os
import csv
import time
import pandas as pd

def folder(images):
    try:
        foldername = "myimages"
        os.mkdir(foldername)
    except:
        print("Folder Exists!!")


    img_download(images, foldername)

def img_download(images, foldername):
    count = 0
    i = 1
    image_urls = []
    for image in images:
        try:
            img_url = image["src"]
            if ".svg" not in img_url and img_url not in image_urls:
                image_urls.append(img_url)
            else:
                img_url = ""
        except KeyError:
            try:
                img_url = image["data-src"]
                if ".svg" not in img_url and img_url not in image_urls:
                    image_urls.append(img_url)
                else:
                    img_url = ""
            except:
                pass

        try:
            result = requests.get(img_url).content
            try:
                result = str(result, "utf-8")
            except UnicodeDecodeError:
                with open(f"{foldername}/part_{i}.jpg", "wb+") as f:
                    f.write(result)
                count += 1
                i += 1
        except:
            pass
    # print(image_urls)
    # print(len(image_urls))

    if count == len(image_urls):
        print("All Images Downloaded!")
    else:
        print(f"{count} out of {len(images)} Downloaded")


def main(url):
    response = requests.get(url)

    soup = bs(response.text, "html.parser")

    images = soup.find_all("img")
    # print("total images: ", len(images))
    # print(images)

    folder(images)

url = "https://in.hotels.com/"
main(url)
