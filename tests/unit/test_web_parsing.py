import os
import sys

import bs4


sys.path.append(os.path.relpath(__file__) + "/../src")
import src.redownload


def test_download_from_url():
    page = src.redownload.web_parsing.download_from_url(
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )
    assert type(page) == bs4.BeautifulSoup
    assert "It's hard to imagine a world without A Light in the Attic" in page.text
