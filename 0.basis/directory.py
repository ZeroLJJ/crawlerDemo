#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2019/5/15 9:56
# @Author  : Zero
# @File    : directory
# @Descr   : 

import os

print('***获取当前目录***')
# 以下两种，在当前脚本文件是被引用时，有可能会不同
print(os.getcwd())  # 当前的工作目录（主脚本文件所在的目录）
print(os.path.abspath(os.path.dirname(__file__)))  # 当前文件的目录

print('***获取上级目录***')
print(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
print(os.path.abspath(os.path.dirname(os.getcwd())))
print(os.path.abspath(os.path.join(os.getcwd(), "..")))

print('***获取上上级目录***')
print(os.path.abspath(os.path.join(os.getcwd(), "../..")))