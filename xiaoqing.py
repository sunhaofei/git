#!/usr/bin/env python3
## -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:06:40 2020

@author: sunhaofei
"""

import pandas as pd

from matplotlib import pyplot as plt

filename = '/Users/sunhaofei/Downloads/data_hxh.xlsx'

df = pd.read_excel(filename)

## 设置天气情况的判别条件, 云量低于5成算晴天（1），云量大于5算阴天（0）；有雨有雪算雨天（2）

df["conditions"] = [0 if cloud > 5 else 1 for cloud in df["clouds"].apply(float)]
row_list = []
for index, row in df.iterrows():
    if row["rains"] == 1:
        row["conditions"] = 2
    row_list.append(row)
df = pd.DataFrame(row_list)

# data = df.head(20)#默认读取前5行的数据
# print("获取到所有的值:\n{0}".format(data))  # 格式化输出

# 把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
period =pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], freq="D")
df["datetime"] = period
# print(df.head(10))

# 把datetime 设置为索引
df.set_index("datetime", inplace=True)

# # 准备数据
_x = df.index
_t = df["T"]
_y = 30

# # #画图
fig = plt.figure(figsize=(200, 7), dpi=100)
color = {0:"yellow", 1: "red", 2: "blue"}
plt.bar(range(len(_x)), _t, color=[color[0] if i == 0 else(color[1] if i == 1 else color[2]) for i in df["conditions"]])
# plt.plot(range(len(_x)), _t, color="black",lw=5)
plt.show()
plt.savefig('/Users/sunhaofei/Downloads/gift.jpg')
