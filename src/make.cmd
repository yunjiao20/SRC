pyinstaller -F -n SRC SRC\random_choice.py
move SRC\dist\SRC.exe SRC\

pyinstaller -F -n SRC-GUI SRC-GUI\gui.py
move SRC\dist\SRC-GUI.exe SRC-GUI\

pyinstaller -F -n SRCGUIlit SRC-GUIlit\gui.py
move SRC-GUIlit\dist\SRCGUIlit.exe SRC-GUIlit\
