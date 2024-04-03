import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
# 创建示例DataFrame，你应该使用你的数据
data=pd.read_csv("../Data/model_inputs.CSV")
matplotlib.use('TkAgg')
# 分组并计算均值
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan', 'magenta', 'yellow', 'brown', 'gray', 'pink', 'olive']

grouped = data.groupby('Primary Technical Branch')['Patent Value'].mean().reset_index()
grouped = grouped.sort_values(by='Patent Value', ascending=False)
print(grouped)
# 设置图表
plt.figure(figsize=(20, 10))
bars=plt.barh(grouped['Primary Technical Branch'], grouped['Patent Value']/10000, color=colors, edgecolor='black')

# 添加虚线
# for val in grouped.values:
#     plt.axvline(val, color='gray', linestyle='--', linewidth=0.8)

# 设置横纵坐标标签
plt.xlabel('Average Patent Value(Ten thousand dollars)',fontsize=24)
plt.ylabel('Primary Technical Branch',fontsize=24)
plt.xticks(fontsize=24)
plt.yticks([])
# 显示图表
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.title('Average Patent Value by Primary Technical Branch',fontsize=24)
for bar, label in zip(bars, grouped['Primary Technical Branch']):
    bar.set_label(label)

# 显示图例
plt.legend(loc='upper right',bbox_to_anchor=(1.0, 1.0),fontsize=24)
plt.tight_layout()
plt.savefig('../picture/PrimaryTechnicalBranch_mean_analysis.png')
plt.show()
