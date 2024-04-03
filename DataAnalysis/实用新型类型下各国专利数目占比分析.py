import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


matplotlib.use('TkAgg')
font = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文黑体字体


# 假设您的表格数据存储在名为"patents.csv"的CSV文件中
# 请根据您的实际情况修改文件名和路径
data = pd.read_csv("../Data/Elevator_Patents_List.CSV")
data['公开国别'] = data['公开国别'].replace('中国台湾', '中国')
data['公开国别'] = data['公开国别'].replace('中国香港', '中国')
data['公开国别'] = data['公开国别'].replace('中国澳门', '中国')

# 创建DataFrame
df = pd.DataFrame(data)

df = df[df["专利类型"] == "实用新型"]

# 将国家不在列表中的国家归类为其他
countries_of_interest = ['中国', '日本', '韩国', '美国', '德国']
df['公开国别'] = df['公开国别'].apply(lambda x: x if x in countries_of_interest else '其他')

# 计算每个国家的专利数量
patent_counts_by_country = df['公开国别'].value_counts()
print(patent_counts_by_country)

# 绘制饼状图
plt.pie(patent_counts_by_country, labels=patent_counts_by_country.index, autopct='%1.1f%%', startangle=140)

# 添加标题
plt.title('实用新型类型各国专利数量占比')
plt.savefig('../picture/实用新型类型各国专利数量总分布.png')  # 文件名可以根据需要修改
plt.show()