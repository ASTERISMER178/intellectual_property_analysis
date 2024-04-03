import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

matplotlib.use('TkAgg')
# 假设您的表格数据存储在名为"patents.csv"的CSV文件中
# 请根据您的实际情况修改文件名和路径
df = pd.read_csv("../Data/rawdata.CSV")
# 使用groupby分组并生成一个字典，其中键为分组的属性值，值为对应的DataFrame
for col in df.columns:
    # 判断是否只有一个字符且为 '-'
    mask = (df[col].astype(str).str.len() == 1) & (df[col] == '-')
    df.loc[mask, col] = None
df = df.dropna(subset=['Patent Value'])
for index,row in df.iterrows():
    value = row['Patent Value']  # 获取当前行中 "column_name" 属性的值
    # 在这里对属性值进行操作，例如加倍
    new_value=value[1:]
    number = new_value.replace(',', '')
    # 将操作后的值赋回到当前行的属性
    df.at[index, 'Patent Value'] = number
df['Patent Value'] = df['Patent Value'].astype(np.int64)
df['Publication Country'] = df['Publication Country'].replace('中国台湾', 'China')
df['Publication Country'] = df['Publication Country'].replace('中国香港', 'China')
df['Publication Country'] = df['Publication Country'].replace('中国澳门', 'China')
selected_countries = ['China', 'Japan', 'Korea', 'United States', 'Germany']

df = df[df['Publication Country'].isin(selected_countries)]

# 定义五种颜色
colors = ['blue', 'green', 'red', 'purple', 'orange']
# 分组并计算均值
grouped = df.groupby('Publication Country')['Patent Value'].mean().reset_index()
grouped = grouped.sort_values(by='Patent Value', ascending=False)
print(grouped)
# 设置图表
plt.figure(figsize=(10, 6))
bars=plt.barh(grouped['Publication Country'], grouped['Patent Value']/10000, color=colors, edgecolor='black')

# 设置横纵坐标标签
plt.xlabel('Average Patent Value(Ten thousand dollars)',fontsize=24)
plt.ylabel('Publication Country',fontsize=24)
# plt.xlabel('Year',fontsize=24)
plt.xticks(fontsize=24)
plt.yticks([])
# 显示图表
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.title('Average Patent Value by Country',fontsize=24)
# 添加图例项
for bar, label in zip(bars, grouped['Publication Country']):
    bar.set_label(label)

# 显示图例
plt.legend(loc='upper right',bbox_to_anchor=(1.0, 1.0),fontsize=24)
plt.tight_layout()
plt.savefig('../picture/Country_mean_analysis.png')
plt.show()