import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties

matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文黑体字体
df=pd.read_excel("../Data/datapro2.xlsx")
zldf=df["专利价值"].value_counts().reset_index()
zldf.columns=["专利价值","专利数量"]
plt.scatter(zldf["专利价值"]/1000,zldf["专利数量"])
plt.xlabel("专利价值")
plt.ylabel("专利数量")
plt.title("不同专利价值下的专利数量分布散点图")
plt.savefig('../picture/不同专利价值下的专利数量分布散点图.png')

# # 排序，以便按照专利价值升序绘制
# value_counts = zldf.sort_values(by='专利价值')
#
# # 绘制折线图
# plt.plot(zldf['专利价值'], zldf['专利数量'], marker='o', linestyle='-')
# plt.xlabel('专利价值')
# plt.ylabel('专利数量')
# plt.title('../picture/不同专利价值下的专利数量分布折线图.png')
plt.show()