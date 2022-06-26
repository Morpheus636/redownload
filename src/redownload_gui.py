import PySimpleGUI as gui

import redownload


layout = [
    [gui.Text(f"Redowload GUI {redownload.version.build_version}")],
    [gui.Text("URL"), gui.InputText()],
    [gui.Submit(button_text="Redownload")],
    [gui.Text("Copyright Josh Levin (Morpheus636) 2022, Released under the GNU GPL V3")],
]

window = gui.Window(title=f"Redownload - {redownload.version.build_version}", layout=layout)

# Event Loop
while True:
    event, values = window.read()
    if event in (None, "Exit"):
        break
window.close()
