# _*_coding : UTF-8 _*_
# 开发人员 : 13767
# 开发时间 : 2021/1/10  22:33
# 文件名称 : py3.py
# 开发工具 : PyCharm

# 1产生一个3D彩票
# import random
# def ball3d():
#     radBall = ''
#     number = '1234567890'
#     for i in range(3):
#         radBall = radBall+str(random.choice(number))
#     return str(radBall)
#
# print(ball3d())


# 2输出三个手工3D彩票号码和3个随机3D彩票号码
import random


def ball3d():
    radBall = ''
    number = '1234567890'
    for i in range(3):
        radBall = radBall + str(random.choice(number))
    return str(radBall)


def inputNew():
    inStr = input('请输入一个福彩3D彩票(三位数字)：')
    inStr = inStr.strip()
    return inStr


def inputBox():
    cxStr = inputNew()
    if len(cxStr) == 3 and cxStr.isdigit():
        return cxStr
    else:
        print('输入错误，请重新输入3位数字的3D彩票')


inBall = []
while len(inBall) < 3:
    inBall.append(inputBox())
inBall.append(ball3d())
inBall.append(ball3d())
inBall.append(ball3d())
print('您需要的3D彩票已生成')
print('\n'.join(inBall))
