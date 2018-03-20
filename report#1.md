# 数据挖掘新生培训第一阶段报告

## 环境介绍

Windows 10 64位 家庭版

## Python 2.7 的安装

在 python.org [下载](https://www.python.org/downloads/release/python-2714/)py 2.7，在安装过程中选择 Add to PATH 以添加至环境变量。

打开 CMD，输入 `python` 弹出 python 交互界面，安装成功

```
C:\Users\Siriu>python
Python 2.7.12 (v2.7.12:d33e0cf91556, Jun 27 2016, 15:24:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## 安装必要的包

安装 numpy scipy pandas sklearn 包
```
python -m pip install --upgrade pip
pip install --user numpy scipy pandas sklearn
```

安装 MinGW-64 ，并且安装 Xgboost

在交互界面逐一 import 之，没有出现报错，安装成功

## 配置 VScode 下的 python

参见 VS code [官方文档](https://code.visualstudio.com/docs/languages/python)

下载 Python 插件，配置 usersetting 中 py 的路径，即可实现 linting/debugging

## 熟悉 numpy 和 pandas 等库的使用

> 详见 `creating-series.py` & `dataframe.py`

尝试了 series 和 dataframe 对象的构建和运算，和 dataframe 的取行与取列的操作。

> 详见 `test-xgboost.py`

尝试了一下 xgboost 官方文档中的程序，又看了看别人的博客，发现并不懂什么是什么，暂时略过。

## 习题解答思路

### ID 数量统计

使用 pandas 的 `read_csv(file)` 方法将csv文件读入dataframe。

取dataframe的特定列，调用unique方法，取得列的set；调用 `len(set)` 取得set的大小，即 unique_ID 的数量。

路口id，收费站id，车辆id均是同理。

### 分类统计并给出统计数据



