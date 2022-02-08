""" The module for HTML parsing related functions. """
import urllib.request

import bs4

from . import exceptions


def html_from_url(url: str) -> bs4.BeautifulSoup:
    """Downloads an HTML page from a url and converts it to a BeautifulSoup object.

    :param url: The URL to download HTML from, in a string.
    :return: BeautifulSoup object extracted from the url.
    """
    request = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla"}))
    html_doc = request.read()
    html_soup = bs4.BeautifulSoup(html_doc, features="html.parser")
    return html_soup


def extract_links(
    page: bs4.BeautifulSoup, filter_relative: bool, extensions: list = None, domains: list = None
) -> set:
    """Extracts all the links with a file extension listed in the extensions param from a BeautifulSoup object and
    returns a list of them. Raises an exception if there are no audio links in the object. If extensions is not
    specified, returns all links on the page.

    :param page: a BeautifulSoup object to extract audio links from.
    :param filter_relative: a bool value to decide whether to remove relative URLs.
    :param extensions: OPTIONAL: a list of file extensions to filter for. If not specified, returns all links.
    :param domains: OPTIONAL: a list of domains to require. If not supplied, returns all links.
    :return: a set of links to audio files ending in .flac or .mp3
    """
    all_links = set()
    # Get all links on page.
    for link in page.findAll("link"):
        href = link.get("href")
        if href:
            all_links.add(href)
    for link in page.findAll("a"):
        href = link.get("href")
        if href:
            all_links.add(href)

    correct_extensions_links = set()
    if extensions is not None:
        # Add matching links to the correct_links list
        for link in all_links:
            # if 'link' ends with any extension in extensions
            if any(link.endswith(extension) for extension in extensions):
                correct_extensions_links.add(link)
    else:
        # Add all links to the correct_extensions_links list if extensions is an empty list
        correct_extensions_links = all_links

    correct_domains_links = set()
    if domains is not None:
        # Add matching links to the correct_links list
        for link in correct_extensions_links:
            # if 'link' starts with https://domain or http://domain, add it to correct domains links
            if any(link.startswith(f"http://{domain}") for domain in domains):
                correct_domains_links.add(link)
            if any(link.startswith(f"https://{domain}") for domain in domains):
                correct_domains_links.add(link)
    else:
        # Add all links to the correct_domains_links list if extensions is an empty list
        correct_domains_links = correct_extensions_links

    correct_links = set()
    if filter_relative is True:
        for link in correct_domains_links:
            # filter out relative links
            if any(link.startswith(start) for start in ["http://", "https://"]):
                correct_links.add(link)
    else:
        correct_links = correct_domains_links

    if not correct_links:
        raise exceptions.NoLinksFoundInPage(
            "The page provided does not contain any links that match the criteria."
        )
    else:
        return correct_links
