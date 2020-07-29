import bs4

#from bs4 import BeautifulSoup as soup
from bs4 import BeautifulSoup
import shutil
import tempfile
import requests



with open("index.html") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>a web page</html>")
#req = urllib.request.Request('http://www.voidspace.org.uk')
req = requests.get('https://news.google.com/news/rss')
#req= requests.get('https://imgs.xkcd.com/comics/making_progress.png')
#with urllib.request.urlopen(req) as response:
#   xml_page = response.read()


#news_url  = "https://news.google.com/news/rss"
#Client = urlopen(news_url)
#xml_page = Client.read()
#Client.close()

soup_page = soup(x, "xml")
news_list = soup_page.findall('items')

# print news title, url and publish date

for news in news_list:
    print(news.tittle.text)
    print(news.link.text)
    print(nws.pubDate.text)
    print("_"*60)
