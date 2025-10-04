REM coding: utf8

REM 清除 src/SRC/SRC.exe 和 src/SRC-GUI/SRC-GUI.exe
del .\SRC\SRC.exe
del .\SRC-GUI\SRC-GUI.exe

REM 使用pyinstaller编译 src\source\random_choice.py , 生成程序src\dist\SRC.exe
pyinstaller -F -n SRC source\random_choice.py
REM 移动SRC.exe至 src\SRC\SRC.exe, 并删除pyinstaller生成的文件
move .\dist\SRC.exe SRC\
rmdir /s /q .\build
rmdir /s /q .\dist
del SRC.spec

pyinstaller -F -n SRC-GUI source\gui.py
move .\dist\SRC-GUI.exe SRC-GUI\
rmdir /s /q .\build
rmdir /s /q .\dist
del SRC-GUI.spec