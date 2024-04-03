import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

matplotlib.use('TkAgg')
# 假设您的表格数据存储在名为"patents.csv"的CSV文件中
# 请根据您的实际情况修改文件名和路径
df = pd.read_csv("../Data/model_inputs.CSV")
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'brown', 'gray', 'pink', 'olive', 'teal', 'lime', 'indigo']
# 分组并计算均值
grouped = df.groupby('IPC')['Patent Value'].mean().reset_index()
grouped = grouped.sort_values(by='Patent Value', ascending=False)
print(grouped)
# 设置图表
plt.figure(figsize=(20, 10))
bars=plt.barh(grouped['IPC'], grouped['Patent Value']/10000, color=colors, edgecolor='black')

# 设置横纵坐标标签
plt.xlabel('Average Patent Value(Ten thousand dollars)',fontsize=24)
plt.ylabel('IPC',fontsize=24)
plt.xticks(fontsize=24)
plt.yticks([])
# 显示图表
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.title('Average Patent Value by IPC',fontsize=24)

# 添加图例项
for bar, label in zip(bars, grouped['IPC']):
    bar.set_label(label)

# 显示图例
plt.legend(loc='upper right',bbox_to_anchor=(1.0, 1.0),fontsize=24)
plt.tight_layout()
plt.savefig('../picture/IPC_mean_analysis.png')
plt.show()