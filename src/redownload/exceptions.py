class RedownloadException(Exception):
    """The base exception for redownload. All other redownload exceptions are subclasses."""

    pass


class WebParsingException(RedownloadException):
    """The base exception for the web_parsing module. All exceptions raised by the web_parsing module are
    subclasses.
    """

    pass


class DownloadsException(RedownloadException):
    """The base exception for the downloads module. All exceptions raised by the downloads module  are
    subclasses
    """

    pass


class NoLinksFoundInPage(WebParsingException):
    """Exception raised by web_parsing.extract_links when no links are found in the provided BeautifulSoup object."""

    pass


class InvalidOutputDir(DownloadsException):
    """The output directory specified in downloads.download_from_set is invalid and cannot be used."""

    pass
