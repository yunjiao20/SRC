'''SRC的主函数，原SRCcmdl和SRCGUI的主函数被移动到此'''
import tkinter

import gui
import random_choice 
import file_handler

def main_gui() -> None:
    '''SRC-GUI 的主界面'''

    def button_command1():
        random_choice.open_document(url='../docs/SRC基本配置和使用.html')
    def button_command2():
        command_line()
    def button_command3():
        random_choice.open_document(url='github.com/yunjiao20/SRC', file=False)
    def button_command4():
        gui.不放回随机抽取()

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


def command_line():
    '''SRC command-line 的主函数, input-handle-output loop'''
    random_choice.run_pyfile_if_argv()
    random_choice.print_SRC()
    random_choice.check_names_list()
    random_choice.print_help_msg()
    while True:
        i = input('mode> ')
        match i:
            case 'q':
                print('\nSRC Quit\n')
                return
            case 'h':
                random_choice.print_help_msg()
            case '1':
                random_choice.随机抽取模式()
            case '2':
                random_choice.不放回随机抽取()
            case '3':
                random_choice.随机抽学号()
            case 'clear':
                random_choice.student.names = random_choice.stu_names
                random_choice.frd.clear_file(file='../src-history/last_choiced_names.txt')
            case 'docs':
                random_choice.open_document('../docs/SRC基本配置和使用.html')
            case 'paddr':
                random_choice.open_document(url='github.com/yunjiao20/SRC', file=False)
            case 'gui':
                main_gui()
            case 'guilit': 
                gui.不放回随机抽取()
            case 'recover':
                random_choice.frd.rocover()
            case 'eval':
                print(eval(input('eval> ')))
            case 'exec':
                exec(get_several_line_input())
            case 'run':
                exec(frd.open_and_read(input('file> ')))
            case _:
                print(f'!!!ERROR INPUT!!!  "{i}" not a legal command, pleas input "h" to watch help message')
                print(f'!!!错误输入!!!  "{i}"不是合法指令，请输入"h"以查看帮助信息')

def gui_start() -> None:
    gui.print_SRCGUI()
    gui.check_names_list()
    main_gui()

def get_mode() -> dir:
    '''从文件src/src-config/mode.txt中读取配置信息并返回一个字典'''
    ret_dir = {}
    for line in file_handler.open_and_readlines(file='../src-config/config.txt'):
        if line[0] == '#':
            pass  # 忽略第一个字符为'#'的行
        else:
            config_msg = line.replace('\n', '').split()
            if len(config_msg) == 2:  # 只有.split()后长度为2的行才认为是配置信息
                ret_dir[config_msg[0]] = config_msg[-1]  # 在字典中插入配置信息    
    return ret_dir

def main() -> None:

    print('读取配置文件 src/src-config/config.txt...')
    config_dir = get_mode()
    
    if 'Seed' in config_dir.keys():
        random.seed = int(config_dir['Seed'])
        print(f'\tSeed: {config_dir['Seed']}')
        print('\t!!!Warnning: 设置Seed会导致每次抽取从头抽取的姓名相同!!!')

    if 'StartMode' in config_dir.keys():
        print(f'\tStartMode: {config_dir['StartMode']}')
        match config_dir['StartMode']:
            case 'commandline':  command_line()
            case 'mainGUI':      gui_start()
            case 'choiceGUI':    gui.不放回随机抽取()
            case _ :  print('src/src-config/mode.txt没有有效的StartMode模式消息')
    else :
        print('没有StartMode信息，默认打开src command-line')
        command_line()

if __name__ == "__main__":
    main()
