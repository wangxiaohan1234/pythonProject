from openpyxl import load_workbook
import warnings
# 不发出警告
warnings.filterwarnings('ignore')
from bokeh.io import output_file
# 绘图输出
output_file("bars.html")

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
# 导入图表绘制、图标展示模块
# 导入ColumnDataSource模块
# 1、单系列柱状图 - 分类设置标签
# ColumnDataSource

from bokeh.palettes import Spectral7
from bokeh.transform import factor_cmap
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
            elif index2 == 2:
                counts.append(cell.value)

# fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
# counts = [5, 3, 4, 2, 4, 6]
source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))
colors = ["salmon", "olive", "darkred", "goldenrod", "skyblue", "orange"]
# 创建一个包含标签的data，对象类型为ColumnDataSource

# x_range一开始就要设置成一个字符串的列表；要一一对应
p = figure(x_range=fruits, y_range=(0, 30), plot_height=350, title="Fruit Counts",tools="")
# 加载数据另一个方式
p.vbar(x='fruits', top='counts', source=source,
       width=0.7,  # 宽度
       alpha=0.8,  # 透明度
       color=factor_cmap('fruits', palette=Spectral7, factors=fruits),  # 设置颜色
       legend="fruits")
# 绘制柱状图，横轴直接显示标签
# factor_cmap(field_name, palette, factors, start=0, end=None, nan_color='gray')：颜色转换模块，生成一个颜色转换对象
# field_name：分类名称
# palette：调色盘
# factors：用于在调色盘中分颜色的参数
# 参考文档：http://bokeh.pydata.org/en/latest/docs/reference/transform.html

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
show(p)
