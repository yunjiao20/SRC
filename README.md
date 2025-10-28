# SRC
Student Random Choice 学生姓名随机抽取程序<br>
这是一个适用于seewo的随机抽取学生姓名的程序，最新版使用Python3.14.0编写，pyinstaller编译<br>
<br>
提供的程序为：<br>
*src/SRC/SRC.exe <br>
src/SRC-GUI/SRC-GUI.exe <br>
src/SRC-GUIlit/SRCGUIlit.exe* <br>
源码放在 *src/source/* 处 <br>
<br>
SRC需要文件src/src-config/student_names.txt进行配置，如您需要使用SRC，您最好克隆下所有文件<br>
<br>
值得一提的是，这个程序是相对臃肿且简陋的，因为希望可以拓展一些seewo上没有或不好下载的功能，SRC提供了一些并不必要的
功能。如果您需要用于一些严肃的环境中，你有其它更好的选择

## SRC文档
SRC提供了比此更详细的静态HTML文档，位与 src/docs/ 下。这将为你的配置、使用、错误处理提供方便，
SRC内提供了方便的打开它们的方式。如果你遇上了SRC的标准错误**FileNotFoundError**和**NullStudentNamesList**，
SRC也将会为你打开它

## SRC配置
使用SRC前，你需要进行配置，否则SRC将会返回**NullStudentNamesList**错误。你需要在配置文件
src/src-config/student_names.txt中提供学生姓名。<br>
SRC使用空格和换行来分隔学生姓名，且并不对空格的数量作要求，这意味着你可以使用如

    小明 小军      小红
    小李

或

    小明
    小红
    小军

来给SRC提供学生姓名

## SRC使用
配置完成后，双击文件<br>
*src/SRC/SRC.exe* <br>
*src/SRC-GUI/SRC-GUI.exe* <br>
*src/SRC-GUIlit/SRCGUIlit.exe* <br>
运行。这里推荐你使用*src/SRC-GUI/SRC-GUI.exe*。他们的具体区别请查看SRC文档。你应该自行给它们创建快捷方式，而不该
随意地移动它们。*src/SRC/SRC.exe*作为命令行程序，请查阅文档以查看使用方法
<br>
<br>
<br>
yunjiao20 writed in 2025/10/3
