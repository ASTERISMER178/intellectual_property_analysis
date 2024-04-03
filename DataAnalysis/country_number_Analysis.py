import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


matplotlib.use('TkAgg')
# font = FontProperties(fname=r"C:\Windows\Fonts\msyh.ttc")
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文黑体字体


# 假设您的表格数据存储在名为"patents.csv"的CSV文件中
# 请根据您的实际情况修改文件名和路径
data = pd.read_csv("../Data/rawdata.CSV")
data['Publication Country'] = data['Publication Country'].replace('中国台湾', 'China')
data['Publication Country'] = data['Publication Country'].replace('中国香港', 'China')
data['Publication Country'] = data['Publication Country'].replace('中国澳门', 'China')

# 创建DataFrame
df = pd.DataFrame(data)


# 将国家不在列表中的国家归类为其他
countries_of_interest = ['China', 'Japan', 'Korea', 'United States', 'Germany']
df['Publication Country'] = df['Publication Country'].apply(lambda x: x if x in countries_of_interest else 'Other countries')

# 计算每个国家的专利数量
patent_counts_by_country = df['Publication Country'].value_counts()
print(patent_counts_by_country)
print(countries_of_interest)

# # 绘制饼状图
# plt.pie(patent_counts_by_country, labels=patent_counts_by_country.index, autopct='%1.1f%%', startangle=140)
# plt.axis('equal')

# 创建饼状图
pctdistance=0.85
explode = (0.05, 0.05, 0.05, 0.1,0.3,0.5)
fig, ax = plt.subplots()
ax.pie(patent_counts_by_country, labels=patent_counts_by_country.index, autopct='%1.1f%%', shadow=True, startangle=50,textprops=dict(size=24),explode=explode,labeldistance=1.1)
# plt.rc('font', size=24)
# 添加标题
ax.set_zorder(0)
title=plt.title('Percentage of Patents by Country',fontsize=24)
plt.tight_layout()
plt.savefig('../picture/country_number_Analysis.png')  # 文件名可以根据需要修改
plt.show()