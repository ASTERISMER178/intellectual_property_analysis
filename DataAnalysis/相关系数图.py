import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# 步骤1：创建示例DataFrame

df=pd.read_csv("../Data/model_inputs.CSV")
# 步骤2：计算皮尔逊相关系数
correlation_matrix = df.corr()

# 步骤3：创建缩短标签
short_labels = ["PD","NC","NDP","NC3Y","NC5Y","NCGP","NCDP","NLC","PV"]

# 步骤4：绘制热力图
plt.figure(figsize=(8, 6))
sns.set(font_scale=1.2)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', cbar=True, xticklabels=short_labels, yticklabels=short_labels,fmt=".2f")
plt.title("Pearson Correlation Heatmap")

# 步骤5：添加标签对应关系
# for i, label in enumerate(short_labels):
#     plt.text(i + 0.5, len(short_labels) + 0.5, f"{label} - {correlation_matrix.columns[i]}", ha='center', va='center')
# for i, label in enumerate(short_labels):
#     plt.text(-1.2, i + 0.5, f"{label} - {correlation_matrix.columns[i]}", ha='left', va='center')
plt.tight_layout()
# plt.savefig('../picture/hotmap.png')
plt.show()