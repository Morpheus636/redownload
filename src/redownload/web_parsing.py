""" The module for HTML parsing related functions. """
import urllib.request

import bs4


def download_from_url(url: str) -> bs4.BeautifulSoup:
    """Downloads an HTML page from a url and converts it to a BeautifulSoup object.

    :param url: The URL to download HTML from, in a string.
    :return: BeautifulSoup object extracted from the url.
    """
    request = urllib.request.urlopen(url)
    html = request.read()
    soup = bs4.BeautifulSoup(html, features="html.parser")
    return soup
