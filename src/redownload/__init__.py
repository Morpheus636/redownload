import urllib.parse

from . import downloads, exceptions, version, web_parsing


def redownload(link, filetypes, output_dir):
    parsed_link = urllib.parse.urlparse(link)
    if parsed_link.hostname == "archive.org":
        final_page = web_parsing.html_from_url(link)
    elif parsed_link.hostname == "relisten.net":
        page = web_parsing.html_from_url(link)
        archive_org_links = web_parsing.extract_links(
            page, filter_relative=True, domains=["archive.org"]
        )

        if len(archive_org_links) > 1:
            # Ask the user which link is correct
            print("The following archive.org links were found in that relisten page:")
            # Number and print each link
            archive_org_links = list(archive_org_links)
            for link in archive_org_links:
                print(f"{archive_org_links.index(link)}:    {link}")
            correct_link_number = input(  # FIXME - This shouldn't ask for input on it's own.
                "Enter the number corresponding to the correct archive.org link: "
            )
            # Get the link with the number the user specified, or error out.
            try:
                correct_link = archive_org_links[int(correct_link_number)]
            except ValueError:
                raise exceptions.InvalidInput("You must provide a number.")
            except IndexError:
                raise exceptions.InvalidInput("The number you provided is not an option.")
            final_page = web_parsing.html_from_url(correct_link)

        else:  # Only one archive.org link existed on that page.
            final_page = web_parsing.html_from_url(archive_org_links.pop())

    else:
        pass
        # Error out if they didn't give a link to one of those 2 places.

    links = web_parsing.extract_links(final_page, filter_relative=True, extensions=filetypes)
    downloads.download_from_set(links, output_dir)
