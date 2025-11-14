# coding=utf-8
import tkinter

import random_choice


def one_button_window(title: str,  size: str,  lab1: str,  lab2: str,
                      button_1_text: str, button1_command,
) -> None:
    '''
    只有两个按钮的gui界面，不能更新界面，用于实现错误提醒
    接受参数：
        title: str  --gui标题
        size:  str  --gui尺寸，ru 200x300
        lab1:  str  --第一个文本
        lab2:  str  --第二个文本
        button_1_text: str  --第一个按钮的文本
        button_1_command    --第一个按钮的行为(接受一个函数, 应使用lambda传入)
    '''
    window = tkinter.Tk()
    window.geometry(size)

    window.title(title)
    tkinter.Label(window, text=lab1).pack()
    tkinter.Label(window, text=lab2).pack()
    tkinter.Button(window, text=button_1_text, command=button1_command).pack()

    window.update()
    window.mainloop()

def print_SRCGUI():
    print(r'''
        _______  ______      _____                  ______ .___     .__   ____
       /  ____ \|   __  \  /  _____\              /  _____ \   |    |  | \    /
      /  /____ \|  |  \  \/  /     \|  ______    /  /  ___ \|  |    |  |  |  |
      \______  \|   _   ./  /         |______|  /  /  \_   \|  |    |  |  |  |
      /\____/  /|  | \  \\  \____. /            \  \____/  /|  \____|  |  |  |
     /________/ |__|  \__\\.______/              \.______ /  \________._\/____\
---------------------------------------SRC-GUI----------------------------------------
''')

def check_names_list(l: list|str = random_choice.stu_names) -> None:
    '''检查stu_names是否为"FileNotFoundError" or "NullStudentNemesList" '''
    if l == random_choice.frd.FileNotFoundError:
        random_choice.frd.file_additional(file='../src-history/src-log.txt',
                            content=f'! SRC_Error FileNotFoundError\n')  # 向日志文件记录错误原因
        one_button_window(
            title='SRC-GUI-Error', size='400x300',
            lab1='Error: FileNotFoundError',
            lab2='文件 SRC/src-config/student_names.txt 不存在',
            button_1_text='打开SRC文档',
            button1_command=lambda: random_choice.open_document('../docs/SRC问题排查.html')
        )
        random_choice.exit()
    if l == random_choice.frd.NullStudentNemesList:
        random_choice.frd.file_additional(file='../src-history/src-log.txt',
                            content=f'! SRC_Error NullStudentNemesList\n')  # 向日志文件记录错误原因
        one_button_window(
            title='SRC-GUI-Error', size='500x300',
            lab1='Error: NullStudentNemesList',
            lab2='学生姓名列表为空，您未在 SRC/src-config/student_names.txt 中提供学生名',
            button_1_text='打开SRC文档',
            button1_command=lambda: random_choice.open_document('../docs/SRC基本配置和使用.html')
        )
        random_choice.exit()

def 不放回随机抽取(student = random_choice.student):
    def button_command():
        lab2.config(text=f'\n{student.choice_and_remove()}')
        lab1.config(text=f'剩余学生数量:  {len(random_choice.student.names)}')
        root.update()  # 更新窗口
    root = tkinter.Tk()
    root.geometry('400x200')
    root.title('SRC-GUI')

    tkinter.Label(root, text='SRC.py-GUI').pack()  # 显示文本
    tkinter.Label(root, text='不放回随机抽取').pack()

    lab1 = tkinter.Label(root, text=f'剩余学生数量:  {len(random_choice.student.names)}')
    lab1.pack(anchor='w')

    tkinter.Button(root, text='抽取', command=button_command, activebackground='yellow').pack()  # 显示按钮

    lab2 = tkinter.Label(root, text=f'点击"抽取"抽取学生姓名')
    lab2.pack()

    root.mainloop()

def main_gui() -> None:
    '''SRC-GUI 的主界面'''

    def button_command1():
        random_choice.open_document(url='../docs/SRC基本配置和使用.html')
    def button_command2():
        random_choice.command_line()
    def button_command3():
        random_choice.open_document(url='github.com/yunjiao20/SRC', file=False)
    def button_command4():
        不放回随机抽取()

    root = tkinter.Tk()
    root.geometry('400x300')
    root.title('SRC-GUI')

    tkinter.Label(root, text='SRC-GUI').pack()
    tkinter.Label(root, text='SRC-GUI，SRC的图形化版本，提供了SRC的简单功能').pack()
    tkinter.Label(root, text=' ').pack()
    # button 1
    tkinter.Label(root, text='SRC文档，帮助您的配置与使用').pack()
    tkinter.Button(root, text='SRC Docs', command=button_command1).pack()  # 显示按钮
    # button 2
    tkinter.Label(root, text='打开SRC的命令行界面').pack()
    tkinter.Button(root, text='command line', command=button_command2).pack()
    # button 3
    tkinter.Label(root, text='SRC的GitHub项目地址，你将可以从此获取更新\nGitHub并不总是链接的上，您可稍后再试').pack()
    tkinter.Button(root, text='project address', command=button_command3).pack()
    # button 4
    tkinter.Label(root, text='随机不放回抽取学生姓名，更新了记忆功能').pack()
    tkinter.Button(root, text='开始抽取', command=button_command4).pack()

    root.update()  # 更新窗口
    print('[gui.py]from func<gui()> 窗口被更新')
    root.mainloop()

def main() -> None:
    print_SRCGUI()
    check_names_list()
    main_gui()

if __name__ == '__main__':
    main()