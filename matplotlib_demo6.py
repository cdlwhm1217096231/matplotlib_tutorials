#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 21:44:55
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt

"""pyplot的基础坐标函数"""
# plt.plot()绘制一个坐标图
# plt.boxplot()绘制一个箱形图
# plt.bar()绘制一个条形图
# plt.barh绘制一个横向条形图
# plt.polar()绘制极坐标图
# plt.pie()绘制饼图
# plt.scatter()绘制散点图，x, y长度相同
# plt.step()绘制步阶图
# plt.hist()绘制直方图

# 饼图的绘制
labels = 'Frogs', 'Hogs', 'Dogs', 'Cats'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode=explode, labels=labels,
        autopct='%1.1f%%', shadow=False, startangle=90)
plt.axis('equal')
plt.show()
# 直方图的绘制
np.random.seed(0)
mu, sigma = 100, 20  # 均值和标准差
a = np.random.normal(mu, sigma, size=100)
plt.hist(a, 40, density=1, histtype='stepfilled', facecolor='b', alpha=0.75)
plt.title('Histogram')
plt.show()
