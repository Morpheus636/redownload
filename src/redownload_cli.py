import argparse
import os

import redownload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="The URL to the track you wish to redownload.")
    parser.add_argument(
        "-o", "--output_dir", help="Specify the directory to save the downloaded audio files to."
    )
    args = parser.parse_args()

    url = args.url
    if args.output_dir is not None:
        output_dir = args.output_dir
    else:
        output_dir = os.path.join(os.getcwd(), "redownloads")
    redownload.redownload(url, [".flac", ".mp3"], output_dir)


if __name__ == "__main__":
    main()
