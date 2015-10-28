#-*- coding: utf-8 -*-
def diarylog():
    from sys import argv
    script, filename = argv
    txt = open(filename, 'a+')
    print '输出以前的日志信息：\n'
    print txt.read()
    print '是否记录本次的输入信息？\n'
    x = raw_input('y/n\n')
    if x == 'y':
        shuru = raw_input('请输入你的命令\n')
        txt.write(shuru)
        txt.write('\n')
        txt.close()
    else:
        print '你选择了退出，正在退出...\n'
diarylog()
