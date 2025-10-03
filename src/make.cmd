pyinstaller -F -n SRC SRC\random_choice.py
move SRC\dist\SRC.exe SRC\

pyinstaller -F -n SRC-GUI SRC-GUI\gui.py
move SRC\dist\SRC-GUI.exe SRC-GUI\