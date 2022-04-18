from escodesearcher.assets.site_functions import site_functions
from escodesearcher.assets.site_functions import Functions
import requests
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("No module named 'bs4' found")
    exit(0)

class FetchCode:
    def __init__(self):
        super().__init__
    def fetch_code(self, url):
        
        url_array = url.split('/')
        site_origin = ""
        if(url_array[0] == "https:" or url_array[0] == "http:"):
            site_origin = url_array[2]
        else:
            site_origin = url_array[0]
        if(site_origin not in site_functions):
            return False
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        handler = Functions()
        code_blocks = getattr(handler, site_functions[site_origin])(soup)
        return code_blocks
