import os
import shutil
import sys

import pytest


sys.path.append(os.path.relpath(__file__) + "/../src")
import src.redownload


def test_download_from_set():
    output_dir = os.path.join(os.getcwd(), "tmp_test_downloads_pytest")
    # Single-URL Tests
    correct_filepath = os.path.join(output_dir, "civic_renewal_forms.zip")
    url = "https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip"
    url_set = {url}

    # Test that it works when the output dir specified does not exist with one url in the set.
    if os.path.isfile(output_dir):
        os.remove(output_dir)
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir, ignore_errors=True)
    src.redownload.downloads.download_from_set(url_set, output_dir)
    assert os.path.isfile(correct_filepath) is True
    shutil.rmtree(output_dir, ignore_errors=True)

    # Test that it works when the output dir specified does exist with one url in the set
    if os.path.isfile(output_dir):
        os.remove(output_dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    src.redownload.downloads.download_from_set(url_set, output_dir)
    assert os.path.isfile(correct_filepath) is True
    shutil.rmtree(output_dir, ignore_errors=True)

    # Test that it raises an exception when the output dir specified is a file with one url in the set.
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir, ignore_errors=True)
    if not os.path.isfile(output_dir):
        # Make a file where output_dir should be
        with open(output_dir, "w") as _:
            pass
    with pytest.raises(src.redownload.exceptions.InvalidOutputDir):
        src.redownload.downloads.download_from_set(url_set, output_dir)
    shutil.rmtree(output_dir, ignore_errors=True)

    # Test that it raises an exception if you download the same file twice.
    if os.path.isfile(output_dir):
        os.remove(output_dir)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    src.redownload.downloads.download_from_set(url_set, output_dir)
    with pytest.raises(FileExistsError):
        src.redownload.downloads.download_from_set(url_set, output_dir)
    shutil.rmtree(output_dir, ignore_errors=True)

    # Multi-URL Tests.
    correct_filepaths = [
        os.path.join(output_dir, "civic_renewal_forms.zip"),
        os.path.join(output_dir, "5MB.zip"),
    ]
    url_set = {
        "https://www.dundeecity.gov.uk/sites/default/files/publications/civic_renewal_forms.zip",
        "http://ipv4.download.thinkbroadband.com/5MB.zip",
    }
    # Test that it works with multiple files.
    if os.path.isfile(output_dir):
        os.remove(output_dir)
    if os.path.isdir(output_dir):
        shutil.rmtree(output_dir, ignore_errors=True)
    src.redownload.downloads.download_from_set(url_set, output_dir)
    for file in correct_filepaths:
        assert os.path.isfile(file) is True
    shutil.rmtree(output_dir, ignore_errors=True)
