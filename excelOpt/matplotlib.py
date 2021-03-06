# 导入第三方模块
import matplotlib.pyplot as plt

# plt.rcParams['font.sans-serif'] = ['SimHei']
# # 构造数据
# edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
# labels = ['中专', '大专', '本科', '硕士', '其他']
# explode = [0, 0.1, 0, 0, 0]
# # 绘制饼图
# plt.pie(x=edu,  # 绘图数据
#         labels=labels,  # 添加教育水平标签
#         autopct='%.1f%%',  # 设置百分比的格式，这里保留一位小数
#         explode=explode
#         )
# # plt.axes(aspect='equal')
# # 显示图形
# plt.show()

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]

# 设置分离的距离，0表示不分离
explode = (0, 0.1, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)

# Equal aspect ratio 保证画出的图是正圆形
plt.axis('equal')

plt.show()