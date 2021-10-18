from googlesearch import search
from random import randint
import pandas as pd

keyword = "python"

pause_time = 2

urls = []
for url in search(keyword, tld="com", num=10, start=0, stop=10, pause=pause_time):
    pause_time = randint(1, 5)
    # print(url)
    urls.append(url)

df = pd.DataFrame(urls, columns = ["Google Results",])
df.to_excel("google_results.xlsx", index=False)
