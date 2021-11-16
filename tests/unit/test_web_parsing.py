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


def test_extract_links():
    page = src.redownload.web_parsing.download_from_url(
        "https://archive.org/details/ptf2021-11-14.litzenberger.sbd.akg414.flac16"
    )
    # Test without passing an extensions param
    links = src.redownload.web_parsing.extract_links(page)
    assert links is not None
    assert "https://archive.org/about/faqs.php" in links
    assert "https://archive.org/images/glogo.jpg" in links
    assert (
        "https://archive.org/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        in links
    )
    # Test with an extensions param
    links = src.redownload.web_parsing.extract_links(page, [".mp3"])
    assert links is not None
    assert "https://archive.org/about/faqs.php" not in links
    assert "https://archive.org/images/glogo.jpg" not in links
    assert (
        "https://archive.org/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        in links
    )
