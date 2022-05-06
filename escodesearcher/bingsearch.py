import requests
from urllib.request import urlopen, Request
from urllib.parse import quote
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("No module named 'bs4' found")
    exit(0)


class BingSearch():
    def __init__(self):
        super().__init__

    def search(self, query, num=1):
        keyword = quote(query)
        results = urlopen(Request("https://www.bing.com/search?q=" + keyword,
                                  data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10    _11_5) AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'})).read()
        soup = BeautifulSoup(results, "html.parser")
        urls = []
        for link in soup.find_all('a', href=True):
            if(('http://' in link['href'] or 'https://' in link['href']) and not ('bing.com' in link['href'] or 'microsoft.com' in link['href'])):
                url = link['href']
                urls.append(url)
        return urls[:num]
