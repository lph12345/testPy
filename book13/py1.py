# _*_coding : UTF-8 _*_
# 开发人员 : 13767
# 开发时间 : 2021/1/10  21:37
# 文件名称 : py1.py
# 开发工具 : PyCharm

import prettytable as pt


def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.filed_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        row = ['第{}行'.format(i + 1), '有票', '有票', '有票', '有票', '有票']
        tb.add_row(row)
    print(tb)


def order_ticket(row_num):
    tb = pt.PrettyTable()
    tb.filed_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row) == i + 1:
            rows = ['第{}行'.format(i + 1), '有票', '有票', '有票', '有票', '有票']
            rows[int(column)] = '已售'
            tb.add_row(rows)
        else:
            rows = ['第{}行'.format(i + 1), '有票', '有票', '有票', '有票', '有票']
            tb.add_row(rows)
    print(tb)


if __name__ == '__main__':
    row_num = 13
    show_ticket(row_num)
    choose_num = input('请输入选择的座位，如13,5，表示第13排5号座位：')
    try:
        row, column = choose_num.split(',')
    except:
        print('输入格式错误，如选择第13排5号座位请输入：13,5')
    order_ticket(row_num)
