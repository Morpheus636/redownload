build:
	poetry run python build_system/update_version.py
	poetry run pyinstaller --hidden-import certifi --onefile ./src/redownload_cli.py --name redownload-cli
