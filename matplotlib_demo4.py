#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 21:12:37
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt
"""pyplot中的文本显示函数"""
# plt.xlabel()  对x轴增加文本标签
# plt.ylabel()  对y轴增加文本标签
# plt.title()   对图形整体增加文本标签
# plt.text()    在任意位置增加文本
# plt.annotate() 在图形中增加带箭头的注解


a = np.arange(0.0, 5.0, 0.02)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15, color='green')
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=15)
# plt.text(2, 1, r'$\mu=100$', fontsize=15)  # $显示的是latex格式的文本$
plt.annotate(r'$\mu=100$', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.1, width=2))
plt.axis([-1, 6, -2, 2])
plt.grid(True)
plt.show()
