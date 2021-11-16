class RedownloadException(Exception):
    pass


class WebParsingException(RedownloadException):
    pass


class NoLinksFoundInPage(WebParsingException):
    pass
