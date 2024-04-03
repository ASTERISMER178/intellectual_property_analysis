"""
    数据分析
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_file = './Data/DataProcessed.xlsx'

result_dir_path = os.path.join('./Result')
if not os.path.isdir(result_dir_path):
    os.makedirs(result_dir_path)

# plt Chinese support
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# read data
data_pd = pd.read_excel(data_file)

# 总估值
trans_estimateValue = {}
for i_row in range(len(data_pd)):
    if not pd.isna(data_pd['EstimateValue'][i_row]):
        trans_estimateValue[data_pd.iloc[i_row, 0]] = float(data_pd['EstimateValue'][i_row])
trans_estimateValue_arr = [trans_estimateValue[key] for key in trans_estimateValue.keys()]
print(f'平均总估值：{np.mean(trans_estimateValue_arr):.1f}, 中位数总估值：{np.median(trans_estimateValue_arr):.1f}, '
      f'范围：[{np.min(trans_estimateValue_arr):.1f}, {np.max(trans_estimateValue_arr):.1f}]')
plt.figure(1)
plt.hist(np.log10(trans_estimateValue_arr), bins=100)
plt.xlabel('总估值（万元）', fontsize=14)
x_ticks = [0, 1, 2, 3, 4, 5]
plt.xticks(ticks=x_ticks, labels=np.power(10, x_ticks))
plt.ylabel('记录数', fontsize=14)
plt.grid(axis='y', linestyle='-.')
# plt.show()
plt.savefig(os.path.join(result_dir_path, '总估值分布数.png'))

# 贷款额
trans_loan = {}
for i_row in range(len(data_pd)):
    if not pd.isna(data_pd['Loan'][i_row]):
        trans_loan[data_pd.iloc[i_row, 0]] = float(data_pd['Loan'][i_row])
trans_loan_arr = [trans_loan[key] for key in trans_loan.keys()]
print(f'平均贷款额：{np.mean(trans_loan_arr):.1f}, 中位数贷款额：{np.median(trans_loan_arr):.1f}, '
      f'范围：[{np.min(trans_loan_arr):.1f}, {np.max(trans_loan_arr):.1f}]')

# 贷款额
plt.figure(2)
plt.hist(np.log10(trans_loan_arr), bins=100)
plt.xlabel('贷款（万元）', fontsize=14)
x_ticks = [0, 1, 2, 3, 4, 5]
plt.xticks(ticks=x_ticks, labels=np.power(10, x_ticks))
plt.ylabel('记录数', fontsize=14)
plt.grid(axis='y', linestyle='-.')
# plt.show()
plt.savefig(os.path.join(result_dir_path, '贷款分布数.png'))

# 贷款与估值关系
loan_vs_value = [0, 0, 0]
for k, v in trans_loan.items():
    if v < trans_estimateValue[k]:
        loan_vs_value[0] += 1
    elif v > trans_estimateValue[k]:
        loan_vs_value[2] += 1
    else:
        loan_vs_value[1] += 1
loan_vs_value_ratio = np.array(loan_vs_value) / np.sum(loan_vs_value)
plt.figure(3)
plt.pie(loan_vs_value_ratio, explode=(0.01, 0.01, 0.01),
        autopct='%.1f%%', labels=['贷款 < 估值', '贷款 = 估值', '贷款 > 估值'])
# plt.show()
plt.savefig(os.path.join(result_dir_path, '贷款估值比.png'))

# patent vs type
trans_num_records = {}
record_type_estimateValue = {}
record_year_estimateValue = {}
for i_row in range(len(data_pd)):
    if not pd.isna(data_pd['EstimateValue'][i_row]):
        trans_num_records[data_pd.iloc[i_row, 0]] = trans_num_records.get(data_pd.iloc[i_row, 0], 0) + 1
patent_types = set(data_pd['PatentType'])
patent_types = set([x for x in patent_types if x == x])
for i_row in range(len(data_pd)):
    if not pd.isna(data_pd['EstimateValue'][i_row]) and data_pd['PatentType'][i_row] in patent_types:
        if data_pd['PatentType'][i_row] not in record_type_estimateValue:
            record_type_estimateValue[data_pd['PatentType'][i_row]] = []
        record_type_estimateValue[data_pd['PatentType'][i_row]].append(data_pd['EstimateValue'][i_row] / trans_num_records[data_pd.iloc[i_row, 0]])

    if not pd.isna(data_pd['EstimateValue'][i_row]) and data_pd['PatentNumber'][i_row].startswith('ZL'):
        year = int(data_pd['PatentNumber'][i_row][2:6])
        if year not in record_year_estimateValue:
            record_year_estimateValue[year] = []
        record_year_estimateValue[year].append(data_pd['EstimateValue'][i_row] / trans_num_records[data_pd.iloc[i_row, 0]])

record_type_estimateValue['发明专利'] += record_type_estimateValue['发明']
del record_type_estimateValue['发明']
# 比例图
plt.figure(4)
plt.pie([len(record_type_estimateValue['发明专利']), len(record_type_estimateValue['实用新型']), len(record_type_estimateValue['外观设计'])], explode=(0.01, 0.01, 0.01),
        autopct='%.1f%%', labels=['发明专利', '实用新型', '外观设计'])
# plt.show()
plt.savefig(os.path.join(result_dir_path, '专利类型分布图.png'))

# 专利类型 vs 平均估值
plt.figure(5)
x_ticks = np.arange(len([1, 2, 3]))
x_label = ['发明专利', '实用新型', '外观设计']
plt.bar(x=x_ticks, height=[np.mean(record_type_estimateValue['发明专利']), np.mean(record_type_estimateValue['实用新型']), np.mean(record_type_estimateValue['外观设计'])],
        width=0.5, color=['#1f77b4', '#ff7f0e', '#2ca02c'])

plt.xticks(ticks=x_ticks, labels=x_label)
plt.xlabel('专利类型', fontsize=14)
plt.ylabel('平均估值金额(万元)', fontsize=14)
plt.grid(axis='y', linestyle='-.')
# plt.show()
plt.savefig(os.path.join(result_dir_path, '专利类型估值图.png'))

plt.figure(6)
year_keys = sorted(record_year_estimateValue.keys())
year_values = [np.average(record_year_estimateValue[k]) for k in year_keys]
plt.plot(year_keys, year_values, label='交易记录')
plt.xticks(ticks=np.arange(min(year_keys), max(year_keys)+1, 2))
plt.xlabel('年', fontsize=14)
plt.ylabel('平均估值金额(万元)', fontsize=14)
X_data = np.arange(min(year_keys), max(year_keys)+1)
fitted_coeff = np.polyfit(year_keys, year_values, deg=1)
print(f'拟合参数：{fitted_coeff}')
Y_fitted = np.polyval(fitted_coeff, X_data)
plt.plot(X_data, Y_fitted, label='曲线拟合')
plt.legend()
# plt.show()
plt.savefig(os.path.join(result_dir_path, '专利年估值图.png'))
print(f'平均估值vs年相关系数：{np.corrcoef(year_keys, year_values)[0][1]:.2f}')

print('Done!')
