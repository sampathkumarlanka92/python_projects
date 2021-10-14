import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime
import csv

def get_url(position, location):
    """Generating URL from given position and location"""
    template = "https://in.indeed.com/jobs?q={}&l={}"
    url = template.format(position, location)
    return url

def get_record(job):
    """Extract job data"""
    url = "https://in.indeed.com"
    # job title
    jobtitle = job.select("h2 > span")
    job_title = jobtitle[0].get("title")

    # job url
    joburl = job.get("href")
    job_url = url + joburl

    # company name
    compname = job.find("span", {"class" : "companyName"})
    company_name = compname.text

    # company location
    loc = job.find("div", {"class" : "companyLocation"})
    location = loc.text

    # job salary
    try:
        sal = job.find("span", {"class" : "salary-snippet"})
        job_sal = sal.text
    except AttributeError:
        job_sal = ""

    # job summary
    summary = job.find("div", {"class" : "job-snippet"})
    job_summary = summary.li.text

    # job posted on
    dt = job.find("span", {"class" : "date"})
    postdate = dt.text
    curdate = datetime.today().strftime("%d-%m-%Y")

    record = (job_title, company_name, location, postdate, curdate, job_summary, job_sal, job_url)

    return record

def main(position, location, pages):
    """Run Program"""
    records = []
    url = get_url(position, location)

    count = 1
    while count <= pages:
        response = requests.get(url)
        soup = bs(response.text, "html.parser")
        jobs = soup.find_all("a", "sponTapItem")

        for job in jobs:
            record = get_record(job)
            records.append(record)

        try:
            nxt = soup.find("a", {"aria-label" : "Next"})
            nexturl = nxt.get("href")
            url = "https://in.indeed.com" + nexturl
        except AttributeError:
            break

        with open("myresults.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(['JobTitle', "Company", "Location", "PostDate", "Current Date", "Summary", "Salary", "JobURL"])
            writer.writerows(records)

        count += 1

main("python", "Hyderabad Telangana", 2)
