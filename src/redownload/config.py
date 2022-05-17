import os
import platform

import yaml


# Set the IS_UNIX constant to true or false based on the platform
if platform.system() == "linux" or platform.system() == "darwin":
    IS_UNIX = True
else:
    IS_UNIX = False
    import winreg

# Set the LOCATION constant
if not IS_UNIX:
    LOCATION = os.path.join(os.getenv("APPDATA"), "redownload", "config.yml")
elif IS_UNIX:
    LOCATION = os.path.join(os.getenv("HOME"), ".config", "redownload", "config.yml")


def create_default() -> None:
    """Create a config file at the correct location with the default values

    :return: None
    """
    # Figure out where the default output dir should be
    if not IS_UNIX:
        # Get the location of the Downloads folder from the registry
        # Yes this is long, windows is stupid. There's nothing I can do about it. Blame Microsoft.
        # https://stackoverflow.com/a/48706260/13800487
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            downloads_location = winreg.QueryValueEx(key, downloads_guid)[0]
        # Actually set the output dir
        output_dir = os.path.join(downloads_location, "redownloads")
    elif IS_UNIX:
        output_dir = os.path.join(os.getenv("HOME"), "Downloads", "redownloads")

    default_config = {"output_dir": output_dir, "track_formats": [".flac", ".mp3"]}

    with open(LOCATION, "w") as stream:
        yaml.safe_dump(default_config, stream)


def load() -> dict:
    """Load the config file from LOCATION and return it as a dict.

    :return: Config dict
    """
    if not os.path.exists(LOCATION):
        create_default()
    with open(LOCATION, "r") as stream:
        loaded_config = yaml.safe_load(stream)
    return loaded_config


config = load()
