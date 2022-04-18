from escodesearcher.urls_fetcher import UrlsFetcher
from escodesearcher.fetch_code import FetchCode

class SearchCode:
    def __init__(self):
        super().__init__
        self.UrlsFetcher = UrlsFetcher()
        self.CodeFetcher = FetchCode()
    def search(self, string):
        urls = self.UrlsFetcher.fetch_urls(string)
        source_codes = []
        for i in urls:
            codes = self.CodeFetcher.fetch_code(i)
            if(codes != False):
                source_codes += codes
        return source_codes