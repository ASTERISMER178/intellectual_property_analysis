import pandas as pd
import numpy as np
df = pd.read_excel('../Data/result12_dtc.xlsx')
# 创建一个示例DataFrame


# 按照真实类型分组
groups = df.groupby('真实值')

# 计算每个组的预测准确率
accuracies = {}

for name, group in groups:
    correct_predictions = (group['真实值'] == group['预测值']).sum()
    total_predictions = len(group)
    accuracy = correct_predictions / total_predictions
    accuracies[name] = accuracy

# 打印每个类型的预测准确率
for key, value in accuracies.items():
    print(f'类型 {key} 的预测准确率: {value:.2f}')