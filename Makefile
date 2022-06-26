version:
	poetry run python build_system/update_version.py

cli:
	make version
	poetry run pyinstaller --onefile ./src/redownload_cli.py --name redownload-cli

gui:
	make version
	poetry run pyinstaller --onefile ./src/redownload_gui.py --name redownload-gui
