import os
import platform
import typing

import yaml


# Set the IS_UNIX constant to true or false based on the platform
if platform.system() == "Linux" or platform.system() == "Darwin":
    IS_UNIX = True
else:
    IS_UNIX = False
    import winreg

# Set the LOCATION constant
if not IS_UNIX:
    CONFIG_DIR = os.path.join(os.getenv("APPDATA"), "redownload")
    LOCATION = os.path.join(CONFIG_DIR, "config.yml")
elif IS_UNIX:
    CONFIG_DIR = os.path.join(os.getenv("HOME"), ".config", "redownload")
    LOCATION = os.path.join(CONFIG_DIR, "config.yml")

# Define the empty config variable to be populated by load()
config = dict()


def dump(config_dict: dict, location=LOCATION) -> None:
    """Dumps config dict to location using YAML syntax.

    :param config_dict: The dictionary to dump.
    :param location: The location of the config file. Optional, defaults to LOCATION
    :return: None
    """
    os.makedirs(os.path.dirname(location), exist_ok=True)
    with open(location, "w+") as stream:
        yaml.safe_dump(config_dict, stream)


def create_default(location=LOCATION) -> None:
    """Create a config file at the correct location with the default values

    :param location: The location of the config file. Optional, defaults to LOCATION
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

    # Save the default config to the file
    dump(default_config, location=location)


def set_key(key: str, value: typing.Any, location=LOCATION, ignore_invalid: bool = False) -> None:
    """Sets specified key to equal specified in the config dict, and writes the changes
    to the config file

    :param key: The key to set.
    :param value: The value to set the key to.
    :param location: The location of the config file. Optional, defaults to LOCATION
    :param ignore_invalid: If true, the function will add a key to the config file if it doesn't already exist.
    Otherwise, will raise a KeyError. Optional, defaults to False.
    :return None:
    """
    global config
    if key not in config.keys() and ignore_invalid is False:
        raise KeyError("The config key specified does not exist.")
    else:
        config[key] = value
        dump(config, location=location)


def load(location=LOCATION) -> dict:
    """Load the config file from LOCATION and return it as a dict.

    :param location: The location of the config file. Optional, defaults to LOCATION
    :return: Config dict
    """
    global config
    if not os.path.exists(LOCATION):
        create_default()
    with open(location, "r") as stream:
        loaded_config = yaml.safe_load(stream)
    config = loaded_config
    return loaded_config


# Load config
load()
