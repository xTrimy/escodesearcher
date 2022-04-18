# escodesearcher

A source code searcher

Currently searching in a limited set of sites:

* Geeks for Geeks
* C plus plus
* Tutorials Point
* Programiz

## Dependencies

* requests - `pip install requests`
* beautifulsoup4 - `pip install beautifulsoup4`
* google - `pip install google`
* html2text - `pip install html2text`

## Usage

Use `SearchCode`

`escodesearcher` can be used to fetch source code urls from the sites mentioned above or to fetch the source codes in these sites

To fetch and save the source codes:

```python

from escodesearcher import SearchCode
code_searcher = SearchCode()
keyword = "Merge sort C++"

for index,source_code in enumerate(code_searcher.search("Merge Sort C++")):
    with open('fetched_files/'+str(index)+'.txt', 'w', encoding='utf8') as f:
        f.write(source_code)
```

To fetch urls only:

```python
from escodesearcher import UrlsFetcher
searcher = UrlsFetcher()
urls = searcher.fetch_urls("Binary Search C++")
print(urls)
```

Result is a list of urls from specific sites

To fetch source codes from specific url from the supported sites:

```python
from escodesearcher import FetchCode

code_grapper = FetchCode()
print(code_grapper.fetch_code(
    "https://www.tutorialspoint.com/binary-search-in-cplusplus"))

```
