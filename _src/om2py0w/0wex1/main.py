#-*- coding: utf-8 -*-
def diarylog():
    from sys import argv
    script, filename = argv
    txt = open(filename, 'a+')
    print '�����ǰ����־��Ϣ��\n'
    print txt.read()
    print '�Ƿ��¼���ε�������Ϣ��\n'
    x = raw_input('y/n\n')
    if x == 'y':
        shuru = raw_input('�������������\n')
        txt.write(shuru)
        txt.write('\n')
        txt.close()
    else:
        print '��ѡ�����˳��������˳�...\n'
diarylog()
