# beauty_soup.py
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from urllib.request import urlopen
import mechanicalsoup
import time
import requests
url = "https://react-amazon-bestsellers-books-dy.netlify.app/"
session =HTMLSession()

response=session.get(url)
response.html.render()

soup=BeautifulSoup(response.html.html,'html.parser')
books=soup.find_all('article',class_='book')
for book in books:
    print(book.find('h2').text)
    print(book.text)

# 1
# browser = mechanicalsoup.Browser()
# url = "https://www.ouedkniss.com/"
# login_page = browser.get(url)
# login_html = login_page.soup
# print(login_html)
# # 2
# form = login_html.select("form")[0]
# form.select("input")[0]["value"] = "zeus"
# form.select("input")[1]["value"] = "ThunderDude"

# # 3
# profiles_page = browser.submit(form, login_page.url)
# print(profiles_page.url)
# links = profiles_page.soup.select("a")
# for link in links:
#     address = link["href"]
#     text = link.text
#     print(f"{text}: {address}")

# base_url = "http://olympus.realpython.org"
# for link in links:
#     address = base_url + link["href"]
#     text = link.text
#     print(f"{text}: {address}")

# page = browser.get("http://olympus.realpython.org/dice")
# tag = page.soup.select("#result")[0]
# result = tag.text

# print(f"The result of your dice roll is: {result}")


# for i in range(4):
#     page = browser.get("http://olympus.realpython.org/dice")
#     tag = page.soup.select("#result")[0]
#     result = tag.text
#     print(f"The result of your dice roll is: {result}")

#     # Wait 10 seconds if this isn't the last request
#     if i < 3:
#         time.sleep(10)