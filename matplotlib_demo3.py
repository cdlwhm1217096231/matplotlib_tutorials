#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 20:50:50
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

"""pyplot的中文显示"""
# 方法一------------改变的是绘制的全局字体
# pyplot并不默认支持中文显示，需要rcParams修改字体实现
matplotlib.rcParams['font.family'] = 'SimHei'
plt.plot([3, 1, 4, 5, 2])
plt.ylabel('纵轴(值)')
plt.savefig('test', dpi=600)
plt.show()
# rcParams的属性:'font.family'用于显示字体的名字，'font.style'字体风格，正常normal或斜体italic，'font.size'字体大小整数字号或者large，x-small
# 中文字体说明:SimHei中文黑体,Kaiti中文楷体，Lisu中文隶书，FangSong中文仿宋，YouYuan中文幼圆，STSong华文宋体
matplotlib.rcParams['font.family'] = 'STSong'
matplotlib.rcParams['font.size'] = 15

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴:时间')
plt.ylabel('纵轴：振幅')
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()

# 方法二-----建议第二种方法，不改变全局字体
# 在有中文输出的地方，加入一个属性: fontproperties

a = np.arange(0.0, 5.0, 0.02)

plt.xlabel('横轴：时间', fontproperties='SimHei', fontsize=15)
plt.ylabel('纵轴：振幅', fontproperties='SimHei', fontsize=15)
plt.plot(a, np.cos(2 * np.pi * a), 'r--')
plt.show()
