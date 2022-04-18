from __future__ import absolute_import

from escodesearcher.assets.site_functions import site_functions

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    exit(0)
import requests
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("No module named 'bs4' found")
    exit(0)

class UrlsFetcher():
    def __init__(self):
        super().__init__
        self.site_set = site_functions
    def fetch_urls(self,string):
        urls = []
        for i in site_functions:
            search_query = string + " site:"+i
            for j in search(search_query, tld="com", num=1, stop=1, pause=4):
                # don't change pause=4 to a number below 2 to avoid google blocking your IP
                urls.append(j)

        return urls
