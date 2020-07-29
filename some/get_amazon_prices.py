from bs4 import BeautifulSoup
import shutil
import tempfile
import requests
import smtplib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

url = "https://www.amazon.ae/Pro-Smartphone-Auroral-Wireless-Headphones/dp/B085YP3MY5"
page = requests.post(url)
print(page.status_code)

print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# title of the page
print(soup.title)


# get attributes:
print(soup.title.name)


# beginning navigation:
print(soup.tittle.parent.name)

#print headers
print(soup.head)

#
print(soup.a)

soup.find_all('a')

#get values :
print(soup.title.string)

# getting specifi values

print(soup.p)

# getting all
print(soup.find_all('p'))

print(soup.find_all('a'))


for paragraph in soup.find_all('p'):
  print(paragraph.string)
  print(str(paragraph.text))

 for url in soup.find_all('a'):
    print(url.get('href'))
    print()

# print(soup.get_text)
#find a particular item

a = soup.find(id = "productTitle")
b = a.get_text()
print(b.strip())


# find an item's price

price = soup.find(id = "priceblock_ourprice")
b = price.get_text()
print(b)
print()
print(b[3:])
