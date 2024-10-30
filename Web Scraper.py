# Python3 Web Scraper for Cybersecurity news
#---------------------------------------------

from bs4 import BeautifulSoup
import requests
import smtplib
from datetime import date

# ----------------------------------------------
# List of pages to pull requests from

# https://www.darkreading.com/
# https://hackread.com/
# https://www.bleepingcomputer.com/
# https://thehackernews.com/
# https://www.csoonline.com/
# https://krebsonsecurity.com/
# ----------------------------------------------




def main():
    today = date.today()
    month, year = today.strftime("%B %Y").split()
    month = month.lower()
    news_dict = dict()
    news_count = 5    # Number of articles linked
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}

    #dark_reading(news_dict, news_count, month, yearm)
    #hackread(news_dict, news_count)
    #bleeping_computer(news_dict, news_count, headers)
    the_hacker_news(news_dict, news_count, headers)
    print(news_dict)


# Filter and process requests from websites above individually


# ----------------------------------------------
# Dark Reading Requests
# Sitemap: https://www.darkreading.com/news-archive-index.xml

def dark_reading(news_dict, news_count, month, year):
    news_list = list()
    response = requests.get(f"https://www.darkreading.com/news/archive/{year}/{month}.xml")
    soup = BeautifulSoup(response.content, "html.parser")
    news = soup.find_all('loc')
    for index in range(news_count):
        news_list.append(news[-index].string)
    news_dict['dark_reading'] = news_list

# ----------------------------------------------
# Hackread Requests
# Sitemap: https://hackread.com/post-sitemap1.xml

def hackread(news_dict, news_count):
    news_list = list()
    response = requests.get("https://hackread.com/post-sitemap1.xml")
    soup = BeautifulSoup(response.content, "html.parser")
    news = soup.find_all('loc')
    for index in range(news_count):
        news_list.append(news[index].string) # Reversed indexing
    news_dict['hackread'] = news_list

# ----------------------------------------------
# Bleeping Computer Requests

def bleeping_computer(news_dict, news_count, headers):
    news_list = list()
    response = requests.get("https://www.bleepingcomputer.com/feed/", headers=headers) # headers used to avoid 403 error
    soup = BeautifulSoup(response.content, "html.parser")
    news = soup.find_all('guid')
    for index in range(news_count):
       news_list.append(news[-index].string)
    news_dict['bleeping_computer'] = news_list

# ----------------------------------------------
# The Hacker News Requests

def the_hacker_news(news_dict, news_count, headers):
    news_list = list()
    response = requests.get("https://thehackernews.com/", headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    for link in soup.find_all('a', href=True):
       print(link['href'])
    #news_dict['the_hacker_news'] = news_list

# ----------------------------------------------
# Computer Security Online (CSO) Requests
response = requests.get("https://www.csoonline.com/")
soup = BeautifulSoup(response.content, "html.parser")

# ----------------------------------------------
# Krebs on Security Requests
response = requests.get("https://krebsonsecurity.com/")
soup = BeautifulSoup(response.content, "html.parser")





if __name__ == "__main__":
    main()
    # ....



