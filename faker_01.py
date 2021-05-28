# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Liu Yue
@Version        :  
------------------------------------
@File           :  faker_01.py
@Description    :  
@CreateTime     :  2021/5/28 10:10 下午
------------------------------------
@ModifyTime     :  
"""
# 导入伪造虚拟数据的Faker类
from faker import Faker

# 实例化一个Faker对象：使用locale关键字参数来指定返回的数据语言（可以是中国/其他国家语言），如果默认不指定，将默认使用en_US
faker_data = Faker()
print(faker_data.name())  # 生成1个英文名字

fake_CN = Faker(locale='zh_CN')

# 随机使用locale列表中某种语言返回数据
fake = Faker(locale=['en_US', 'zh_CN', 'zh_TW'])
print(fake.name())  # 生成1个简体、繁体、英文的姓名

# 生成5个简体姓名
for _ in range(5):  # 这句中是 不使用_这个变量
    print(fake_CN.name())

# 返回当前Faker对象返回的数据语言
print(fake_CN.locales)  # ['zh_CN']

# text 关键字参数中：将#号替换成0-9的数字，letters关键字中：将？号替换成中字符串的任意一个子字符
print(fake_CN.bothify(text='产品编号：??-#######', letters='JD'))  # 产品编号：DD-9594797

# text关键字参数中^ 都替换为一个随机的十六进制字符，upper=False使用小写的十六进制字符
print(fake_CN.hexify(text='MAC地址：^^:^^:^^:^^:^^', upper=True))  # MAC地址：B8:6F:93:50:D1

# text 中 # 将替换成0-9的数字， % 将替换成1-9的数字， !将替换成一个随机数字或空字符串， @ 将替换成一个随机的非零数字或一个空字符串
print(fake_CN.numerify(text='Inter core i%-%%##K vs AMD Ryzen % %%##X'))  # Inter core i1-1113K vs AMD Ryzen 6 6157X

# 随机生成a-z A-Z
print(fake_CN.random_letter())

# 地址

# address 将生成一个详细地址 及邮编
print(fake_CN.address())  # 安徽省汕尾市黄浦梁街B座 684002

# 生成1个城市名
print(fake_CN.city())  # 成都县

# 生成国家
print(fake_CN.country())  # 圣文森特岛

# 邮政编码
print(fake_CN.postcode())  # 301622

# 街道地址
print(fake_CN.street_address())  # 301622

# 号码牌
print(fake_CN.license_plate())  # CTK 776

# 银行卡号
print(fake_CN.bban())  # 18位
print(fake_CN.iban())  # 22位