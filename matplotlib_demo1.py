#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 19:47:06
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt  # （引入模块的别名）

'''matplotlib.pyplot是绘制各类可视化图形的命令子库,相当于快捷方式'''


# 当plt.plot()中只有一个列表时，会被当成y轴，而x轴是列表的索引，自动生成
plt.plot([3, 1, 4, 5, 2])
plt.ylabel("grade")
plt.savefig('grade', dpi=600)  # 将绘制的曲线存储成PNG文件,dpi=600：每个英寸包含600个像素点，表示输出图片的质量
plt.show()


# plt.plot()当有两个以上参数时，分别代表x轴和y轴的点
plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])
plt.ylabel('grade')
plt.axis([-1, 10, 0, 6])  # 设定横纵坐标尺度的列表,代表x轴坐标起始于-1，终止于10；y轴坐标起始于0，终止于6
plt.show()


# pyplot的绘图区域 ---------使用plt.subplot(行数，列数，子图个数)
"""在全局绘图区域中创建一个分区体系，并定位到一个子绘图区域"""
# plt.subplot(3, 2, 4) 等价于plt.subplot(324)
# 将绘图区域划分成3行2列的6个子区域,当前的绘图区在第四个区域见（图subplot介绍.png）


def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


a = np.arange(0.0, 5.0, 0.02)
plt.subplot(211)
plt.plot(a, f(a))

plt.subplot(2, 1, 2)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()
