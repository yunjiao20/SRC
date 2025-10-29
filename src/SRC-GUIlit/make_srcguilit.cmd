pyinstaller -F -n SRCGUIlit gui.py
move .\dist\SRCGUIlit.exe
rmdir /s /q .\build
rmdir /s /q .\dist