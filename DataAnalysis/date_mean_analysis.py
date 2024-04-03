import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

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
df = df.dropna(subset=['Publication Date'])
for index,row in df.iterrows():
    value = row['Patent Value']  # 获取当前行中 "column_name" 属性的值
    # 在这里对属性值进行操作，例如加倍
    new_value=value[1:]
    number = new_value.replace(',', '')
    # 将操作后的值赋回到当前行的属性
    df.at[index, 'Patent Value'] = number
df['Patent Value'] = df['Patent Value'].astype(np.int64)
df = df[df['Publication Country'].isin(['China', '中国台湾','中国香港''中国澳门'])]

df['Publication Date'] = df['Publication Date'].str[:4]
# df["Publication Date"] = pd.to_numeric(df["Publication Date"])
# 计算每年的专利价值均值
grouped = df.groupby('Publication Date')['Patent Value'].mean().reset_index()

# 设置图表风格
# plt.style.use('seaborn')

# 绘制直方图
plt.bar(grouped['Publication Date'], grouped['Patent Value'] / 10000, color='blue', label='Average Patent Value')

# # 绘制折线图
plt.plot(grouped['Publication Date'], grouped['Patent Value'] / 10000, marker='o', color='black', label='Average Patent Value curve')

# # 创建插值函数
# x = np.arange(grouped['Publication Date'].min(), grouped['Publication Date'].max() + 1)
# f = interp1d(grouped['Publication Date'], grouped['Patent Value'] / 10000, kind='cubic')
#
# # 绘制平滑的曲线图
# x_smooth = np.linspace(x.min(), x.max(), 100)
# plt.plot(x_smooth, f(x_smooth), marker='', color='red', label='Mean value curve')

# 使用字符串标签绘制平滑曲线
# plt.plot(grouped['Publication Date'], grouped['Patent Value'] / 10000, marker='o', linestyle='-', label='Mean value curve')


# 添加纵坐标虚线
plt.grid(True, axis='y', linestyle='--', alpha=0.6,color='black')

# 设置坐标轴标签
plt.xlabel('Publication Date',fontsize=12)
plt.ylabel('Average Patent Value(Ten thousand dollars)',fontsize=12)
plt.xticks(rotation=45,fontsize=12)
# 添加图例
plt.legend()
plt.title('Average Patent Value by Publication Date',fontsize=12)
plt.tight_layout()
plt.savefig('../picture/date_mean_analysis.png')
# 显示图表
plt.show()
