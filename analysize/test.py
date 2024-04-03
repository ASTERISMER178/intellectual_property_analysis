import matplotlib.pyplot as plt
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
# 示例数据（假设df为你的dataframe）
data = {'True_Value': [10, 20, 15, 30, 25],
        'Predicted_Value': [12, 18, 16, 28, 22]}
df = pd.DataFrame(data)

# 计算预测值与真实值的绝对差
df['Absolute_Difference'] = abs(df['Predicted_Value'] - df['True_Value'])

# 绘制点图
plt.scatter(df['True_Value'], df['Absolute_Difference'], color='blue', marker='o')

# 添加标题和标签
plt.title('Scatter Plot of Prediction Errors')
plt.xlabel('True Value')
plt.ylabel('Absolute Difference')

# 显示图表
plt.show()
