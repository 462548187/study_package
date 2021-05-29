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
print(fake_CN.numerify(text='Inter core i%-%%##K vs AMD Ruzena % %%##X'))  # Inter core i1-1113K vs AMD Ruzena 6 6157X

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

# ean(length, prefixes) 条形码，length条形码总长--只能是8或13位（默认），prefixes需传递一个元组，如果定义了将随机去元组中某一个字符串
# 并加上在生成的条码前
print(fake_CN.ean(length=13, prefixes=('2020', '2018')))  # 2018020495216

# 生成颜色 名称
print(fake_CN.color_name())  # WhiteSmoke

# 生成颜色 RGB
print(fake_CN.rgb_css_color())  # rgb(122,67,162)

# 生成颜色 代码
print(fake_CN.hex_color())  # #2a0c42

# 公司名称
print(fake_CN.company())  # 方正科技信息有限公司

# 信用卡卡号
print(fake_CN.credit_card_number())  # 213190350181790

# 货币符合
print(fake_CN.currency_symbol())  # ƒ

# 获取时间：默认格式 %Y-%m-%d #2000-09-02
print(fake_CN.date())  # 2007-05-20

# 时间格式
print(fake_CN.date(pattern='%Y-%m-%d %H:%M:%S'))  # 1981-08-20 20:15:48

# 文件名
print(fake_CN.file_name())  # 实现.odp

# 生成office类型的文件（后缀名 将都是office里面的其中一个）
print(fake_CN.file_name(category='office'))  # 这是.xls

# 电子邮箱
print(fake_CN.free_email())  # vyi@hotmail.com

# 图片链接
print(fake_CN.image_url())  # https://placeimg.com/650/96/any

# IPV4地址
print(fake_CN.ipv4_public())  # 217.147.136.196

# MAC地址
print(fake_CN.mac_address())  # 8d:73:34:cb:6f:ca

# 职业
print(fake_CN.job())  # 汽车机构工程师

# 生成一个随机字符串 字符串最大长度默认 200， 最小长度5
print(fake_CN.text())
print(fake_CN.text(max_nb_chars=5))  # 城市政府.

# 生成随机长度的二进制串，默认长度1048576
print(fake_CN.binary(10))  # b'u\x10\x90\x92S\xca\x03\xecg1'

# 女性的名字
print(fake_CN.name_female())  # 张倩

# 男性的名字
print(fake_CN.name_male())  # 马涛

# 手机号码
print(fake_CN.phone_number())  # 13769390972

# 生成个人资料
print(fake_CN.profile())

# 身份证号
print(fake_CN.ssn())  # 410883194804219622

# 用户代理
print(fake_CN.user_agent())  # Mozilla/5.0 (compatible; MSIE 5.0; Windows 95; Trident/5.0)
