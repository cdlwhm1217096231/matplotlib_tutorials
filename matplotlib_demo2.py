#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 20:18:26
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt

# plot函数介绍

"""
plt.plot(x, y, format_string, **kwargs)

x: x轴数据，列表或者元组（可选参数）
y: y轴数据，列表或者元组
format_string： 控制曲线的格式字符串,可选参数
**kwargs： 放入第二组或更多(x, y, format_string),绘制多条曲线时使用(x轴数据不能省略)
"""

a = np.arange(10)
plt.plot(a, a * 1.5, a, a * 2.5, a, a * 3.5, a, a * 4.5)
plt.show()
# format_string： 控制曲线的格式字符串,可选-----由颜色字符、风格字符、标记字符组成,可以组合使用
# 颜色字符: b, g, r, c, m, y, k, w, 0.8（灰度值字符串）,#008000(RGB某种颜色)
# 风格字符: -实线，--破折线，-.点划线，：虚线，"''无线条
'''
标记字符:
.点标记， ','像素标记, 'o'实心圆标记, 'v'倒三角标记， '^'上三角标记, '>'右三角标记， '<'左三角标记
'1'下花三角标记，'2'上花三角标记, '3'左花三角标记, '4'右花三角标记, 's'实心方形标记, 'p'实心五角标记，'*'星形标记
'h'竖六边形标记, 'H'横六边形标记， '+'十字标记， 'x'x标记， 'D'菱形标记, 'd'瘦菱形标记， '|'垂直线标记
'''
a = np.arange(10)
plt.plot(a, a * 1.5, 'go-', a, a * 2.5,'rx', a, a * 3.5,'*', a, a * 4.5,'b-.')
plt.show()
# **kwargs： 放入第二组或更多(x, y, format_string),绘制多条曲线时使用(x轴数据不能省略)
# color:控制颜色，color='green'
# linestyle:线条风格,linestyle='dashed'
# marker:标记风格, marker='o'
# markerfacecolor:标记颜色，markerfacecolor='blue'
# markersize:标记尺寸, markersize=20
