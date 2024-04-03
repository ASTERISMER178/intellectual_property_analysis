import pandas as pd


pd.set_option('display.max_colwidth', None)
# 创建示例DataFrame
df=pd.read_csv("../Data/model_inputs.CSV")
df = df.rename(columns={"Primary Technical Branch":"一级技术分支","Patent Value":"专利价值"})

# 选择需要的列，并按照专利分支分组，并计算均值
mean_values = df[['专利价值', '一级技术分支']].groupby('一级技术分支').mean()

# 保存为txt文件
mean_values.to_csv('../picture/mean_values.txt', sep='\t',float_format='%.2f')