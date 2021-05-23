source venv/bin/activate
pyinstaller src/main.py -F \
--name "GuiScripter" \
--icon='rob_icon.icns' \
--add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' \
--add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' \
--add-data "src/static/*:static" \
--add-data "src/static/*.png:static" \
--onedir --noconsole \
--clean