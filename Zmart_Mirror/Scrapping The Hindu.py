from bs4 import BeautifulSoup as bs
import requests


source = requests.get("https://www.thehindu.com/news/").text
soup = bs(source,'lxml')

today = []
for strings in soup.stripped_strings:
    if len(strings) > 50 and "Watch" not in strings:
        today.append(strings)
del today[0]        

for i in today:
    print(i,sep = "\n")
   