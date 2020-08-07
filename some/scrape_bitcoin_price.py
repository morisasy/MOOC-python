import bs4
from bs4 import BeautifulSoup as soup
#from bs4 import BeautifulSoup
import shutil
import tempfile
import requests

url = "https://www.goolge.com/search?q="
query = "bitcoin + price + in + usd"

def scrape():
    r = requests.get(url + query)
    s = soup(r.text, 'html.perser')
    ##s = soup(page.content, 'html.parser')
    c = s.find('div', class_= "BNeawe iBp4i AP7Wnd")
    return c.text

price = scrape()
print(f'Bitcoin price is {price}')
##page = requests.post(url)
##print(page.status_code)

##print(page.content)
