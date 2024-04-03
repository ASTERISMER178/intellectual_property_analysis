import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import pandas as pd
import re
matplotlib.use('TkAgg')
# 假设您的表格数据存储在名为"patents.csv"的CSV文件中
# 请根据您的实际情况修改文件名和路径
df = pd.read_csv("../Data/Elevator_Patents_List.CSV")
# 使用groupby分组并生成一个字典，其中键为分组的属性值，值为对应的DataFrame
for col in df.columns:
    # 判断是否只有一个字符且为 '-'
    mask = (df[col].astype(str).str.len() == 1) & (df[col] == '-')
    df.loc[mask, col] = None
df = df.dropna(subset=['专利价值'])
for index,row in df.iterrows():
    value = row['专利价值']  # 获取当前行中 "column_name" 属性的值
    # 在这里对属性值进行操作，例如加倍
    new_value=value[1:]
    number = new_value.replace(',', '')
    # 将操作后的值赋回到当前行的属性
    df.at[index, '专利价值'] = number
df['专利价值'] = df['专利价值'].astype(np.int64)
df = df[df['公开国别'].isin(['中国', '中国台湾','中国香港'])]
df = df.dropna(subset=['申请人省市代码'])

# 假设您有一个名为 df 的 DataFrame
china_provinces = []  # 包含中国各个省份的列表
df = df[df['申请人省市代码'].isin(china_provinces)]

font = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")
# 计算每一专利类型的专利价值的均值和方差
stats = df.groupby('申请人省市代码')['专利价值'].agg(['mean', 'std'])

# 绘制柱状图
plt.figure(figsize=(200, 200))
stats.plot(kind='bar', y=['mean', 'std'], alpha=0.7)

plt.xlabel('申请人省市代码', fontproperties=font)
plt.ylabel('专利价值的均值和方差',fontproperties=font)
plt.title('不同申请人省市代码的专利价值均值和方差', fontproperties=font)
plt.legend(["均值", "标准差"], prop=font)
plt.xticks(rotation=90, fontproperties=font)

plt.savefig('../picture/不同申请人省市代码的专利价值分布.png')
plt.show()