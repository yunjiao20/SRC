'''
file_reader.py
读取文件，处理内容
'''
from time import strftime, time    # 获取当前时间



class SRC_Error:
    def __init__(self, error) -> None:
        self.error = error
    def __len__(self) -> int:
        return 0    # error的长度返回零
    def __repr__(self) -> str:
        return self.error

# SRC标准错误
FileNotFoundError    = SRC_Error(error='FileNotFoundError')
NullStudentNemesList = SRC_Error(error='NullStudentNemesList')

def open_and_readlines(file: str) -> list[str] | SRC_Error:
    ''' 使用readlines()读取utf-8编码文件内容并返回，如没有此文件，
    返回FileNotFoundError'''
    try:
        with open(file, mode='r' ,encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        return FileNotFoundError
    else :
        return lines
    
def get_stunames(lines: list[str]) -> list[str] | SRC_Error:
    '''从所给列表的每个字符串元素中读取学生姓名，使用split()
    如果行的第一位为#，则忽略此行'''
    if lines == FileNotFoundError: # 没有此文件
        return lines  # 返回此错误信息
    
    stu_names_l = []
    for line in lines:
        if line[0] == '#':
            pass    # 忽略以#开头的行
        else :
            stu_names = line.split()
            if stu_names:    # stu_name 不为空列表
                stu_names_l += stu_names
            else :    # 空行和只有空格的行
                pass

    return stu_names_l if stu_names_l else NullStudentNemesList

def get_stunames_from_file(file: str, return_error: bool = True) -> list[str] | SRC_Error:
    '''调用open_and_readlines()和get_stunames()，打开文件获取学生姓名，简化调用流程
    如果return_error为False，当获取的姓名为NullStudentNemesList时，不返回SRC_Error，返回空列表。这是为了兼容上次抽取姓名文件'''
    names = get_stunames(open_and_readlines(file=file))
    return [] if (not return_error and names==NullStudentNemesList) else names
    # 当return_error为False时，如names==NullStudentNamesList，返回空列表而非错误
    # 考虑到直接 isinstance(names, SRC_Error) 会导致FileNotFoundError也被过滤，这将会在文件 src-history/last_choiced_names.txt
    # 缺失时程序保持静默，这将导致此函数在处理此文件时始终返回空列表，使记忆功能缺失。与其使用户使用受限制的功能，不如直接崩溃，提醒用户
    # 重新配置SRC

def open_and_read(file: str) -> str:
    '''打开文件并使用read()读取，返回一个字符串'''
    return open(file=file, mode='r', encoding='utf-8').read()

def file_additional(file: str, content: str) -> None:
    '''向文件中追加内容'''
    with open(file, mode='a', encoding='utf-8') as f:
        f.writelines(content)

def clear_file(file: str) -> None:
    '''清空文件'''
    with open(file, mode='w', encoding='utf-8'): pass

def ftime() -> str:
    '''返回当前时间的格式化字符串'''
    return strftime('%Y/%m/%d/%H:%M')

def time_stamp() -> int:
    '''返回当前时间戳，只保留整数部分'''
    return int(time())

def while_until_get_someting(first_msg: str,
                             input_msg: str,
                             until:     tuple[str],
                             help_msg:  str) -> str:
    '''一个while循环，重复input(input_msg)直到获取到指定的几个信息，
    否则输出help_msg。
    因为input()只能获取字符串，until元组的元素必须是字符串，否则无法识别，
    此函数返回一个在until中的字符串，为了减少命令行中的代码量'''
    print(first_msg)
    while True:
        i = input(input_msg)
        if i in until:
            return i
        else:
            print(help_msg)

def get_msg_from_log(get: str, dir_key: str) -> dir:
    '''
    从日志文件 src/source/src-history/src-log.txt 中读取历史信息，提取出字典并返回
    此函数有些复杂，为了给 2025/11/22 新增的 recover 功能提供信息支持

    get: str  获取的信息类型，对应返回字典的值，应为字符串 'name' 或 'copy'，标志返回
              某次打开时抽取的学生姓名或某次更新的学生姓名副本
    dir_key: str  对应返回字典的键，应为字符串 'time' 或 'timestamp'，标志着字典的键
              为格式化的时间或时间戳

    例如:
        get_msg_from_log(get='name', dir_key='time') == {
            '2025/11/21/20:03': ('小明', '小红', '小军',),
            '2025/11/21/21:43': ('小丽',),
            '2025/11/22/7:28':  ('小美', '小李',),
            } # key:当前时间的格式化字符串  value:此次运行抽取的学生姓名元组

        get_msg_from_log(get='name', dir_key='timestamp') == {
            1763812275: ('小明', '小红', '小军',),
            1763812478: ('小丽',),
            1763813440: ('小美', '小李',),
            } # key:当前时间戳的整型形式  value:此次运行抽取的学生姓名元组

        get_msg_from_log(get='copy', dir_key='time') == {
            '2025/11/21/20:03': ('小明', '小红', '小军','小丽', '小美', '小梅', '小丑',),
            '2025/11/22/7:28':  ('小美', '小君', '小李', '小钻风', '小明',),
            } # key:当前时间的格式化字符串  value:此次运行更新的学生姓名副本

       get_msg_from_log(get='copy', dir_key='time') == {
            1763812275: ('小明', '小红', '小军','小丽', '小美', '小梅', '小丑', ...),
            1763813440: ('小美', '小君', '小李', '小钻风', '小明', '唐纳德·J·特朗普', ...),
            } # key:当前时间戳的整型形式  value:此次运行更新的学生姓名副本

    提供时间戳是为了辨别时间的先后，方便 recover 通过起始和终止时间戳获取中间所有的信息
    '''
    with open('../src-history/src-log.txt', mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    key_addr: int = 4 if dir_key=='time' else 5  # 标志返回字典键的在启动信息的位置
                            # '$ SRC start at 2025/11/22/20:37 1763815067 >'.split()[key_addr]

    def get_name(lines = lines, key_addr = key_addr) -> dir:
        d = {'keys': dir_key,  'values': 'name'}  # 字典中的默认值保存字典键和值的类型，方便外部函数的判断
        k = ''; v = []
        for line in lines:
            if line[0] == '$':  # 此行是否为SRC启动信息，如'$ SRC start at 2025/11/22/20:37 1763815067 >'
                if k:  # 如果k不为空
                    d[k]=tuple(v) if k not in d.keys() else d[k]+tuple(v)  # 保存v
                    # 如果没有键k，d[k]=tuple(v)；如果存在键k，d[k]=d[k]+tuple(v)两姓名元组相加
                    # 这是因为以分钟为最小单位的格式化时间字符串如果关闭再迅速打开可能会存在相同的值，
                    # 只使用d[k]=tuple(v)可能会导致相同k的上一个值被覆盖
                    # 而以秒为最小单位的时间戳则无此问题，为了代码复用，也以此行处理
                k = line.split()[key_addr]
                v = []  # 更新k、v
            elif line[0] not in '$#!-<>[':  # 没有SRC log的特殊标识符，不是日志信息，则为学生姓名
                v.append(line)
        return d
    
    def get_copy(lines = lines, key_addr = key_addr) -> dir:
        d = {'keys': dir_key,  'values': 'copy'}  # 字典中的默认值保存字典键和值的类型，方便外部函数的判断
        k = ''
        for line in lines:
            if line[0] == '$':
                k = line.split()[key_addr]    # 更新k
            elif line[0] == '[':  # 将列表的方括号作为辨别保存的副本信息的值——这比以'-'辨别更可靠
                if k:
                    d[k] = tuple(eval(line))  # 读取列表并转为元组，此行可能会造成代码注入
                    k = ''    # 当k不是空字符时此if语句才执行，执行完后k被清空，直到下一次
                              # line[0]=='$'时k才再次被赋值，保证只有运行信息后的第一个以
                              # '['开头的信息才被处理
        return d
    
    return get_name() if get == 'name' else get_copy()


def rocover():
    '''依托日志文件，提供历史信息恢复功能，包括每次运行时抽取的信息信息或恢复某次更新的姓名副本'''
    print('src recover 用于恢复一些信息')
    mode = while_until_get_someting(first_msg='需要恢复的信息:\n\tname  --恢复历史抽取的学生姓名\n\tcopy  --恢复学生姓名配置',
        input_msg='rocover/mode> ',until=('name', 'copy'), help_msg='请依照上述提示信息选择恢复信息')
    key  = while_until_get_someting(first_msg='你需要通过什么来检索信息\n\ttime  --通过SRC打开的格式化时间信息来恢复信息(如 2025/11/22/9:14)\n\ttimestamp  --通过时间戳(如 1763813440)来恢复信息，允许使用起始和终止时间批量选择',
        input_msg='recover/key> ', until=('time', 'timestamp'), help_msg='请依照上述提示信息选择检索方式')
    
    print('handling...')
    d: dir = get_msg_from_log(get=mode, dir_key=key)
    for k in d.keys():  # 输出字典的信息
        print(f'{k} :  {d[k]}')

    if d['keys']=='time' and d['values']=='name':
        print('键入启动时间(如 2025/11/22/7:28)，此次抽取的学生姓名将会被插入历史抽取学生姓名文件 src/src-history/last_chioced_names.txt')
        if input('是否要帮你清空此文件(y/n)') in 'Yy':
            clear_file('../src-history/last_choiced_names.txt')
        while True:
            k = input('recover/time-name> ')
            if k == 'q':
                return
            elif k in d.keys():
                for v in d[k]:
                    file_additional(file='../src-history/last_choiced_names.txt', content=v)
                    print(v)
            else:
                print(f'键"{k}"不存在')

    elif d['keys']=='timestamp' and d['values']=='name':
        print('键入启动时间戳(如 1763813440)，此次抽取的学生姓名将会被插入历史抽取学生姓名文件 src/src-history/last_chioced_names.txt')
        print('如"1763801125 - 1763813440"将会将两个时间戳之间抽取的学生姓名全部追加')
        if input('是否要帮你清空此文件(y/n)') in 'Yy':
            clear_file('../src-history/last_choiced_names.txt')
        while True:
            k = input('recover/timestamp-name> ')
            if k == 'q':
                return
            elif k in d.keys():
                for v in d[k]:
                    file_additional(file='../src-history/last_choiced_names.txt', content=v)
                    print(v)
            elif k.split()[1] == '-':
                try:
                    k = k.split()
                    for key in d.keys():
                        print(key)
                        if key == 'keys' or key == 'values': # 排除特殊值
                            continue
                        elif int(k[0]) <= int(key) <= int(k[2]): # 如果此时间戳在起始和终止时间戳之间
                            for v in d[key]:              # 插入数据
                                file_additional(file='../src-history/last_choiced_names.txt', content=v)  # 不用 v+'\n'
                                print(v)                                        # 因为readlines读取的姓名带有 \n                               
                except:
                    print('格式错误')
            else:
                print(f'键"{k}"不存在')

    elif d['keys']=='time' and d['values']=='copy':
        print('键入启动时间(如 2025/11/22/7:28)，此次更新的学生姓名将会被插入学生姓名配置文件 src/src-config/student_names.txt')
        if input('是否要帮你清空配置文件(y/n)') in 'Yy':
            clear_file('../src-config/student_names.txt')
        while True:
            k = input('recover/time-copy> ')
            if k == 'q':
                return
            elif k in d.keys():
                for v in d[k]:
                    file_additional(file='../src-config/student_names.txt', content=v)
                    print(v)
            else:
                print(f'键"{k}"不存在')                

    elif d['keys']=='timestamp' and d['values']=='copy':
        print('键入启动时间(如 1763813440)，此次更新的学生姓名将会被插入学生姓名配置文件 src/src-config/student_names.txt')
        print('配置文件恢复不提供提供起始和终止时间戳批量选择功能')
        if input('是否要帮你清空配置文件(y/n)') in 'Yy':
            clear_file('../src-config/student_names.txt')
        while True:
            k = input('recover/timestamp-copy> ')
            if k == 'q':
                return
            elif k in d.keys():
                for v in d[k]:
                    file_additional(file='../src-config/student_names.txt', content=v)
                    print(v)
            else:
                print(f'键"{k}"不存在')