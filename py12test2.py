# _*_coding : UTF-8 _*_
# 开发人员 : 13767
# 开发时间 : 2021/1/10  19:30
# 文件名称 : py12test2.py
# 开发工具 : PyCharm

from datetime import datetime


class Medicine():
    name = ''
    price = 0
    PD = ''
    Exp = ''

    def __init__(self, name, price, PD, Exp):
        self.name = name
        self.price = price
        self.PD = PD
        self.Exp = Exp

    def get_name(self):
        return self.name

    def get_GP(self):
        start = datetime.strptime(self.PD, '%Y-%m-%d')
        end = datetime.strptime(self.Exp, '%Y-%m-%d')
        return (end - start).days


if __name__ == '__main__':
    medicine = Medicine(name='格列宁', price=1860, PD='2018-5-1', Exp='2018-12-1')
    name = medicine.get_name()
    GP = medicine.get_GP()

    print('药品名称：{}'.format(name))
    print('药品保质期：{}天'.format(GP))

# from datetime import datetime
#
#
# class Medicine(object):
#     def __init__(self, name, price, PD, Exp):
#         self.name = name
#         self.price = price
#         self.PD = PD
#         self.Exp = Exp
#
#     def get_name(self):
#         return self.name
#
#     def get_GP(self):
#         start = datetime.strptime(self.PD, '%Y-%m-%d')
#         end = datetime.strptime(self.Exp, '%Y-%m-%d')
#         GP = end - start
#         return GP.days
#
#     def is_expire(self):
#         today = datetime.now()
#         oldday = datetime.strptime(self.Exp, '%Y-%m-%d')
#         if today > oldday:
#             return True
#         else:
#             return False
#
#
# if __name__ == '__main__':
#     medicineObj = Medicine('感冒胶囊', 100, '2019-1-1', '2019-3-1')
#     print('name:', medicineObj.get_name())
#     print('药品保质期为：', medicineObj.get_GP())
#     print('药品是否过期：', '药品过期' if medicineObj.is_expire() else '药品未过期')
