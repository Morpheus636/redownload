import argparse
import os
import sys

import redownload


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
    elif args.url is not None:
        if args.output_dir is not None:
            output_dir = args.output_dir
        else:
            output_dir = os.path.join(os.getcwd(), "redownloads")
    else:
        url = input("Enter the Relisten or Archive.org URL to download the tracks from: ")
        output_dir = input(
            "Enter the path to save the tracks to (ENTER for default [./redownlaods]): "
        )
        if not output_dir:
            output_dir = os.path.join(os.getcwd(), "redownloads")
    redownload.redownload(url, [".flac", ".mp3"], output_dir)


if __name__ == "__main__":
    main()
