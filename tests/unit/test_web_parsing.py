import os
import sys

import bs4
import pytest


sys.path.append(os.path.relpath(__file__) + "/../src")
import src.redownload


def test_html_from_url():
    page = src.redownload.web_parsing.html_from_url(
        "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    )
    assert type(page) == bs4.BeautifulSoup
    assert "It's hard to imagine a world without A Light in the Attic" in page.text


def test_extract_links():
    # TODO - Test the domain argument.
    page = src.redownload.web_parsing.html_from_url(
        "https://archive.org/details/ptf2021-11-14.litzenberger.sbd.akg414.flac16"
    )
    # Test without passing an extensions param and with filter_relative False
    links = src.redownload.web_parsing.extract_links(page, False)
    # Check that links are returned.
    assert links is not None
    # Check that links with various extensions are returned
    assert "https://archive.org/about/faqs.php" in links
    assert "https://archive.org/images/glogo.jpg" in links
    assert (
        "https://archive.org/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        in links
    )
    # Check that relative links are returned
    assert (
        "/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        in links
    )

    # Test without passing an extensions param and with filter_relative True
    links = src.redownload.web_parsing.extract_links(page, True)
    # Check that links are returned
    assert links is not None
    # Check that links with various extensions are returned
    assert "https://archive.org/about/faqs.php" in links
    assert "https://archive.org/images/glogo.jpg" in links
    assert (
        "https://archive.org/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        in links
    )
    # Check that relative links are not returned.
    assert (
        "/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        not in links
    )

    # Test with an extensions param provided
    links = src.redownload.web_parsing.extract_links(page, False, [".mp3"])
    # Check that links are returned
    assert links is not None
    # Check that links not ending with .mp3 are not returned
    assert "https://archive.org/about/faqs.php" not in links
    assert "https://archive.org/images/glogo.jpg" not in links
    # Check that links ending in .mp3 are returned.
    assert (
        "https://archive.org/download/ptf2021-11-14.litzenberger.sbd.akg414.flac16/ptf2021-11-14t02_Theme_From_The_Bottom.mp3"
        in links
    )

    # Test with a domains param and filter_relative True
    links = src.redownload.web_parsing.extract_links(
        page, filter_relative=True, domains=["archive.org"]
    )
    assert "https://archive.org/about/faqs.php" in links
    assert (
        "https://www.facebook.com/sharer/sharer.php?u=https://archive.org/details/ptf2021-11-14.litzenberger.sbd.akg414.flac16"
        not in links
    )

    # Test with a domains param and filter_relative False
    links = src.redownload.web_parsing.extract_links(
        page, filter_relative=False, domains=["archive.org"]
    )
    assert "https://archive.org/about/faqs.php" in links
    assert (
        "https://www.facebook.com/sharer/sharer.php?u=https://archive.org/details/ptf2021-11-14.litzenberger.sbd.akg414.flac16"
        not in links
    )

    # Test that an exception will be raised if the provided BS document has no links.
    html_doc = ""
    page = bs4.BeautifulSoup(html_doc, features="html.parser")
    with pytest.raises(src.redownload.exceptions.NoLinksFoundInPage):
        links = src.redownload.web_parsing.extract_links(page, False)
