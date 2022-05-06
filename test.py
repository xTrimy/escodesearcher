from escodesearcher import UrlsFetcher
from escodesearcher import FetchCode
from escodesearcher import SearchCode

# searcher = UrlsFetcher()
# urls = searcher.fetch_urls("Binary Search C++")
# print(urls)

# code_grapper = FetchCode()
# print(code_grapper.fetch_code(
#     "https://www.tutorialspoint.com/binary-search-in-cplusplus"))

code_searcher = SearchCode()
keyword = "Merge sort C++"

for index, source_code in enumerate(code_searcher.search(keyword, search_engine="bing")):
    with open('fetched_files/'+str(index)+'.txt', 'w', encoding='utf8') as f:
        f.write("//"+source_code[0])
        f.write(source_code[1])
