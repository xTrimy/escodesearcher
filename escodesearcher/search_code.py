from escodesearcher.urls_fetcher import UrlsFetcher
from escodesearcher.fetch_code import FetchCode


class SearchCode:
    def __init__(self):
        super().__init__
        self.UrlsFetcher = UrlsFetcher()
        self.CodeFetcher = FetchCode()

    def search(self, string, search_engine="google"):
        urls = self.UrlsFetcher.fetch_urls(string, search_engine=search_engine)
        source_codes = []
        for i in urls:
            codes = self.CodeFetcher.fetch_code(i)
            if(codes != False):
                for j in codes:
                    arr = [i,j]
                    source_codes.append(arr)
        return source_codes
