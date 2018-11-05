#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-08-19 21:30:12
# @Author  : cdl (1217096231@qq.com)
# @Link    : https://github.com/cdlwhm1217096231/python3_spider
# @Version : $Id$

import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.pyplt as plt

"""pyplot的子绘图区域"""
# plt.subplot2grid()  设定网络，选中网络，确定选中的行列区域数量,编号从0开始
# plt.subplot2grid((3, 3), (2, 1), colspan=2, rowspan=3)

# GridSpec类结合subplot相当于plt.subplot2grid()
gs = gridspec.GridSpec(3, 3)
ax1 = plt.subplot(gs[0:1])
ax2 = plt.subplot(gs[1:-1])
