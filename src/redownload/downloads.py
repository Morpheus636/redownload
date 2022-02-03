import os

import requests

from . import exceptions


def download_from_set(urls: set, out_dir: str) -> None:
    """Takes a set of urls as an arg and downloads them all to out_dir.

    :param urls: a set of URLs.
    :param out_dir: a string containing a path pointing to the directory to save the downloaded files to
    :return: None
    """
    # If the output dir is a file, raise an exception.
    if os.path.isfile(out_dir):
        raise exceptions.InvalidOutputDir(
            "The output path specified is a file and cannot be overwritten."
        )
    # If the output dir doesn't exist, create it.
    if not os.path.exists(out_dir):
        os.mkdir(out_dir)
    # Download all the URLs in the set to the output dir.
    for url in urls:
        filename = url[url.rfind("/") + 1 : len(url)]
        with requests.get(url, stream=True) as response:
            with open(os.path.join(out_dir, filename), "wb") as f:
                for chunk in response.iter_content(2 ** 20):
                    f.write(chunk)
