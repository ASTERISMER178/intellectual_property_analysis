import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import matplotlib
matplotlib.use('TkAgg')
# 假设您的表格数据存储在名为"patents.csv"的CSV文件中
# 请根据您的实际情况修改文件名和路径
# df = pd.read_csv("../Data/Elevator_Patents_List.CSV")
df = pd.read_csv("../Data/model_inputs.CSV")

# 使用groupby分组并生成一个字典，其中键为分组的属性值，值为对应的DataFrame
# for col in df.columns:
#     # 判断是否只有一个字符且为 '-'
#     mask = (df[col].astype(str).str.len() == 1) & (df[col] == '-')
#     df.loc[mask, col] = np.nan
# df = df.dropna(subset=['专利价值'])
# for index,row in df.iterrows():
#     value = row['专利价值']  # 获取当前行中 "column_name" 属性的值
#     # 在这里对属性值进行操作，例如加倍
#     new_value=value[1:]
#     number = new_value.replace(',', '')
#     # 将操作后的值赋回到当前行的属性
#     df.at[index, '专利价值'] = number
# df['专利价值'] = df['专利价值'].astype(np.int64)
# df = df[df['公开国别'].isin(['中国'])]
# , '中国台湾','中国香港''中国澳门'
avg_values = df.groupby('Primary Technical Branch')['Patent Value'].mean()

# 对均值进行排序
sorted_avg_values = avg_values.sort_values()

# 绘制直方图
plt.bar(sorted_avg_values.index, sorted_avg_values.values / 10000)  # 均值除以10000，单位变成“万”
# tick_positions = [0, 0.5, 1.0, 1.5,2]
# tick_labels = ['0.00', '0.50', '1.00', '1.50','2.00']
# plt.yticks(tick_positions, tick_labels)
# 添加标题和标签
plt.xlabel('专利类型')
plt.ylabel('专利价值均值（万）')  # 修改纵坐标标签
plt.title('不同一级技术分支下的专利价值均值')

# 自动调整标签显示
# plt.xticks(rotation=45, ha='right')
# plt.yticks(range(int(min(sorted_avg_values.values) / 10000), int(max(sorted_avg_values.values) / 10000) + 1, 1))
# 自动调整标签显示
plt.legend(["均值"])#, prop=font
# plt.xticks(rotation=0, ha='right')
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.25)
plt.xticks(rotation=30)
plt.savefig('../picture/不同一级技术分支的专利价值均值分布.png')
plt.show()