import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
# 假设您的DataFrame中第一列是"年份"，第二列是"专利申请数量"
# 请根据您的实际列名进行调整
df=pd.read_excel("../Data/patent_num_global.xlsx")
plt.figure(figsize=(10, 6))  # 设置图形大小
plt.plot(df['year'], df['Number of patent applications']/10000, marker='o', linestyle='-')
plt.title('Number of Patent Applications Per Year Worldwide',fontsize=24)
plt.xlabel('Year',fontsize=24)
plt.ylabel('Amount (Ten thousand dollars)',fontsize=24)
plt.xticks(fontsize=24)
plt.yticks(fontsize=24)
plt.grid(True)  # 添加网格线
plt.tight_layout()
plt.savefig('../picture/num_year_analysis.png')
plt.show()
#Number of Patent Applications(tens of thousands of US dollars)