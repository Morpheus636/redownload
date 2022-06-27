import argparse
import os
import sys

import redownload


config = redownload.config.config


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "url", help="The URL to the track you wish to redownload.", default=None, nargs="?"
    )
    parser.add_argument(
        "-o", "--output_dir", help="Specify the directory to save the downloaded audio files to."
    )
    parser.add_argument(
        "-v", "--version", action="store_true", help="Print Redownload's version information."
    )
    args = parser.parse_args()

    url = args.url
    if args.version:
        print(f"Build Version: {redownload.version.build_version}")
        sys.exit()
    # Non-Interactive Mode
    elif args.url is not None:
        if args.output_dir is not None:
            output_dir = args.output_dir
        else:  # Use the default output dir
            output_dir = None
    # Interactive Mode
    else:
        url = input("Enter the Relisten or Archive.org URL to download the tracks from: ")
        output_dir = input(
            f"Enter the path to save the tracks to (ENTER for default [{config['output_dir']}]): "
        )
        if not output_dir:  # Use the default output dir
            output_dir = None
    if output_dir:
        redownload.redownload(url, output_dir=output_dir)
    else:
        redownload.redownload(url)


if __name__ == "__main__":
    main()
