# _*_coding : UTF-8 _*_
# 开发人员 : 13767
# 开发时间 : 2021/1/10  22:18
# 文件名称 : py2.py
# 开发工具 : PyCharm

import datetime


def inputdate():
    indate = input('请输入开始日期（20190909）后按<enter>：')
    indate = indate.strip()
    if len(indate) == 0:
        return datetime.date.today()
    else:
        if len(indate) == 8:
            datester = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:8]
            return datetime.datetime.strptime(datester, '%Y-%m-%d')
        else:
            print('输入错误，将按照当前日期推算')
            return datetime.date.today()


print('*************推算几天后的日期***************')
sdate = inputdate()
innum = input('请输入间隔天数后按enter')
if int(innum) != 0:
    fdate = sdate + datetime.timedelta(days=int(innum))
    fdate = datetime.datetime.strftime(fdate, '%Y-%m-%d')
    print('你推算的日期是：' + str(fdate))
else:
    print('输入醋五，程序将推出！！')
