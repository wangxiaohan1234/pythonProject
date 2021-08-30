import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook
import warnings
# 不发出警告
warnings.filterwarnings('ignore')
from bokeh.io import output_file
# 绘图输出
output_file("bars2.html")

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.transform import dodge
from bokeh.core.properties import value
# 导入dodge、value模块
# 导入相关模块

wb = load_workbook("/Users/snowang/Downloads/pythontest/123.xlsx")
ws = wb["Sheet1"]
# total_list = []
# for row in ws.rows:
#     row_list = []
#     for cell in row:
#         row_list.append(cell.value)
#     total_list.append(row_list)
# namedict = {}
# valuedict = {}
fruits = []
names = []
counts = []
for index in range(len(list(ws.rows))):
    if index == 0:
        continue
    else:
        row = list(ws.rows)[index]
        for index2 in range(len(row)):
            cell = row[index2]
            if index2 == 0:
                fruits.append(cell.value)
            elif index2 == 1:
                names.append(cell.value)
            elif index2 == 2:
                counts.append(cell.value)

df = pd.DataFrame({'2015':[2, 1, 4, 3, 2, 4],'2016':[5, 3, 3, 2, 4, 6], '2017':[3, 2, 4, 4, 5, 3]},
                 index = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries'])
# 创建数据

fruits = df.index.tolist()   # 横坐标
years = df.columns.tolist()    # 系列名

data = {'index':fruits}
for year in years:
    data[year] = df[year].tolist()
print(data)
# 生成数据，数据格式为dict

source = ColumnDataSource(data=data)
# 将数据转化为ColumnDataSource对象

p = figure(x_range=fruits, y_range=(0, 10), plot_height=350, title="Fruit Counts by Year",tools="")

p.vbar(x=dodge('index', -0.25, range=p.x_range), top='2015', width=0.2, source=source,color="#c9d9d3", legend=value("2015"))
p.vbar(x=dodge('index',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,color="#718dbf", legend=value("2016"))
p.vbar(x=dodge('index',  0.25, range=p.x_range), top='2017', width=0.2, source=source,color="#e84d60", legend=value("2017"))
# 绘制多系列柱状图
# dodge(field_name, value, range=None) → 转换成一个可分组的对象，value为元素的位置（配合width设置）
# value(val, transform=None) → 按照年份分为dict

p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
# 其他参数设置
show(p)