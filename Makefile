build:
	poetry run python ./build-system/update-version.py
	poetry run pyinstaller --onefile ./src/redownload_cli.py --name redownload-cli }}
