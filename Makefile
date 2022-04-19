build:
	poetry run python build_system/update_version.py
	poetry run pyinstaller --onefile ./src/redownload_cli.py --name redownload-cli
