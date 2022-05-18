# Downloading and Using the CLI
Currently, Redownload is only available with a CLI (command line interface).
Instructions for downloading it and using it are as follows:
- Go to the [Releases](https://github.com/Morpheus636/redownload/releases) page in this repository.
- Select the most recent stable release (or alpha/beta, but you may have problems with them).
- Download the file starting with `redownload-cli` for your operating system.
## <img alt="Linux" src="https://cdn-icons-png.flaticon.com/512/6124/6124995.png" width="25" /> Linux
- Open a terminal
- `cd` into the directory containing the `redownload-cli-linux` file
- Run `chmod +x ./redownload-cli-linux`
- You can now run the file with `./redownload-cli-linux <archive.org OR relisten.net link>`. This will download all the .mp3's and .flac's
to `./redownloads/`
- If you need more options, you can run `./redownload-cli-linux --help` and it will print the help to the console.

## <img alt="MacOS" src="https://cdn-icons-png.flaticon.com/512/179/179309.png" width="25" /> MacOS
- Open a terminal
- `cd` into the directory containing the `redownload-cli-mac` file.
- Run `chmod +x ./redownload-cli-mac`
- You can now run the file with `./redownload-cli-mac <archive.org OR relisten.net link>`. This will download all the .mp3's and .flac's
to `./redownloads/`
- If you need more options, you can run `./redownload-cli-linux --help` and it will print the help to the console.

### <img alt="Error Icon" src="https://cdn-icons-png.flaticon.com/512/1304/1304037.png" width="20" /> If you get "Apple can’t check app for malicious software" error,
By default, MacOS prevents apps from running if your system can't check if the software is malicious or not.
**This github repository is not malicious**, so it's safe to say we can override this and run the software anyway.

- Immediately after you get the popup, go to **System Preferences** > **Security and Privacy**
- Near the bottom of the page, next to where it says "redownload-cli-mac was blocked from use because it is not from an identified developer", click the button that says - "**Open Anyway**"
- **Run the app again**. (`./redownload-cli-mac ...`)
- A confirmation popup will appear. **Click "Open" in the new popup**.

## <img alt="Windows" src="https://cdn-icons-png.flaticon.com/512/888/888882.png" width="25" /> Windows
- Open cmd.exe
- `cd` into the directory containing the `redownload-cli-windows.exe` file.
- Run the file with `redownload-cli-windows <archive.org OR relisten.net link`. This will download all the .mp3's and .flac's
to a subdirectory of your working directory called `redownloads`
- If you need more options, you can run `./redownload-cli-windows --help` and it will print the help to the console.

## <img alt="Help!" src="https://emojis.slackmojis.com/emojis/images/1643514968/9949/blob_help.png?1643514968" width="25" /> Help!
If you need help or clarification, join me on [Discord](https://discord.morpheus636.com) or, you can open a [GitHub Issue](https://github.com/Morpheus636/redownload/issues).

Uicons by <a href="https://www.flaticon.com/uicons">Flaticon</a>
