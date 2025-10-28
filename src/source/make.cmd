REM coding: utf-8

rmdir /s /q .\__pycache__

REM 使用pyinstaller编译 src\source\random_choice.py , 生成程序src\dist\SRC.exe
pyinstaller -F -n SRC random_choice.py
REM 移动SRC.exe至 src\SRC\SRC.exe, 并删除pyinstaller生成的文件
REM move的/Y如存在同名文件，自动覆盖而不询问
move /Y .\dist\SRC.exe ..\SRC\
rmdir /s /q .\build
rmdir /s /q .\dist
del SRC.spec

pyinstaller -F -n SRC-GUI gui.py
move /Y .\dist\SRC-GUI.exe ..\SRC-GUI\
rmdir /s /q .\build
rmdir /s /q .\dist
del SRC-GUI.spec