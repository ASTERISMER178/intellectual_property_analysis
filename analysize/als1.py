import pandas as pd
import numpy as np
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
# 假设专利产出国家的列名为"Country"
# 请根据您的实际情况修改列名
# country_count = data['公开国别'].value_counts()


# 计算中国专利的数量
# def china_count(country_counts):
#         china_patent1 = country_counts.get('中国', 0)
#         china_patent2 = country_counts.get('中国台湾', 0)
#         china_patent3 = country_counts.get('中国香港', 0)
#         china_patents = china_patent2+china_patent1+china_patent3
#         return china_patents

# 创建DataFrame
df = pd.DataFrame(data)
# 计算每个产业链位置的总数量
# 计算每个产业链位置的中国专利数量占比
# china_patent_counts_by_position = df[df['公开国别'] == '中国'].groupby('产业链位置').size()
# total_patent_counts_by_position = df.groupby('产业链位置').size()
# china_patent_percentage_by_position = (china_patent_counts_by_position / total_patent_counts_by_position) * 100
#
# # 计算总产业链位置的中国专利数量占比
# total_china_patent_count = china_patent_counts_by_position.sum()
# total_patent_count = df[df['公开国别'] == '中国'].shape[0]
# total_china_patent_percentage = (total_china_patent_count / total_patent_count) * 100
#
# # 绘制直方图
# positions = ['总占比'] + china_patent_percentage_by_position.index.tolist()
# percentages = [total_china_patent_percentage] + china_patent_percentage_by_position.tolist()
#
# plt.figure(figsize=(10, 6))
# plt.bar(positions, percentages, color='blue')
# plt.xlabel('产业链位置')
# plt.ylabel('中国专利数量百分比占比')
# plt.title('中国全球专利数量总分布')
# plt.ylim(0, 100)
# plt.savefig('../picture/中国全球专利数量总分布.png')  # 文件名可以根据需要修改
# plt.show()
# 计算每个产业链位置的总数量
# total_counts = df['产业链位置'].value_counts()
# print(total_counts)
# # 计算每个产业链位置中国专利数量的占比
# china_counts = df[df['公开国别'] == '中国']['产业链位置'].value_counts()
# print(china_counts)
# china_percentage = china_counts / total_counts * 100
# print(china_percentage)
# # 计算总产业链位置中国专利数量的占比
# total_china_counts = china_counts.sum()
# total_china_percentage = total_china_counts / df.shape[0] * 100
# print(type(total_china_percentage))
#
# # 创建新的DataFrame存储数据
# result_df = pd.DataFrame({'产业链位置': ['总占比', '产业链中游', '产业链上游', '产业链下游'],
#                           '中国专利数量百分比占比': [total_china_percentage] + china_percentage.tolist()})
# result_df=result_df.iloc[[0,2,1,3], :]
# print(result_df)
# # 绘制直方图
# plt.bar(result_df['产业链位置'], result_df['中国专利数量百分比占比'])
# plt.xlabel('产业链位置')
# plt.ylabel('中国专利数量百分比占比(%)')
# plt.title('中国全球专利数量百分比占比')
# plt.legend(["百分比"])#, prop=font
# plt.savefig('../picture/中国全球专利数量总分布.png')  # 文件名可以根据需要修改
# plt.show()
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
# # plt.show()  # 显示图表
# data1 = data[data["产业链位置"] != "产业链上游"]
# data2 = data[data["产业链位置"] != "产业链中游"]
# data3 = data[data["产业链位置"] != "产业链下游"]
# data1['公开国别'] = data1['公开国别'].apply(lambda x: x if x in countries_of_interest else '其他')
#
# # 计算每个国家的专利数量
# patent_counts_by_country = data1['公开国别'].value_counts()
#
# # 绘制饼状图
# plt.pie(patent_counts_by_country, labels=patent_counts_by_country.index, autopct='%1.1f%%', startangle=140)
#
# # 添加标题
# plt.title('产业链上游各国专利数量占比')
# plt.savefig('../picture/产业链上游各国专利数量占比总分布.png')  # 文件名可以根据需要修改
# plt.show()
# country_count1 = data1['公开国别'].value_counts()
#
# # 计算其他国家专利的数量
# china_patent1=china_count(country_count1)
# other_patent1 = data1.shape[0] - china_patent1
#
# # 准备绘制饼状图的数据
# sizes = [china_patent1, other_patent1]
# plt.figure()
# # 绘制饼状图
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
#
# plt.axis('equal')  # 使饼图为正圆形
# plt.title('Upstream of the industry chain')
# plt.savefig('../picture/专利数量产业链上游分布.png')
#
# country_count2 = data2['公开国别'].value_counts()
#
# # 计算其他国家专利的数量
# china_patent2=china_count(country_count2)
# other_patent2 = data2.shape[0] - china_patent2
#
# # 准备绘制饼状图的数据
# sizes = [china_patent2, other_patent2]
# plt.figure()
# # 绘制饼状图
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
#
# plt.axis('equal')  # 使饼图为正圆形
# plt.title('mid-industry chain')
# plt.savefig('../picture/专利数量产业链中游分布.png')
# country_count3 = data3['公开国别'].value_counts()
#
# # 计算其他国家专利的数量
# china_patent3=china_count(country_count3)
# other_patent3 = data3.shape[0] - china_patent3
#
# # 准备绘制饼状图的数据
# sizes = [china_patent3, other_patent3]
# plt.figure()
# # 绘制饼状图
# plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#         autopct='%1.1f%%', shadow=True, startangle=140)
#
# plt.axis('equal')  # 使饼图为正圆形
# plt.title('Downstream of the industry chain')
# plt.savefig('../picture/专利数量产业链下游分布.png')