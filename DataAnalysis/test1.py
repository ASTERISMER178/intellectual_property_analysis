import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# 假设你的DataFrame为df，包含两列：'专利类型' 和 '专利价值'
# 以下是一个简化的例子，你需要根据你的实际数据进行调整
data = {'专利类型': ['类型A', '类型B', '类型A', '类型B', '类型C'],
        '专利价值': [10, 15, 8, 12, 20]}
df = pd.DataFrame(data)

# 计算每个专利类型的专利价值均值
mean_values = df.groupby('专利类型')['专利价值'].mean().reset_index()

# 绘制横向直方图
bars = plt.barh(mean_values['专利类型'], mean_values['专利价值'], color=['blue', 'green', 'red', 'purple', 'orange'])
# 隐藏纵坐标标签
plt.yticks([])
# 添加标签
plt.xlabel('专利价值均值')
plt.title('不同专利类型的专利价值均值')

# 添加图例项
for bar, label in zip(bars, mean_values['专利类型']):
    bar.set_label(label)

# 显示图例
plt.legend(loc='upper right',bbox_to_anchor=(1.0, 1.0))
plt.tight_layout()
# 显示图形
plt.show()
