from . import downloads, exceptions, web_parsing


def redownload(archive_org_link, filetypes, output_dir):
    page = web_parsing.html_from_url(archive_org_link)
    links = web_parsing.extract_links(page, True, filetypes)
    downloads.download_from_set(links, output_dir)
