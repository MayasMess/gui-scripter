.\venv\Scripts\activate
pyinstaller src\main.py -F --name "GuiScripter" --icon='rob_icon.ico' --add-data "src\static\*;static" --add-data "src\static\*.png;static" --onedir --noconsole --clean