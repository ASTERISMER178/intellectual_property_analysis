import pandas as pd
import numpy as np
# 创建示例DataFrame
df=pd.read_csv("../Data/model_inputs.CSV")
df = df.rename(columns={"Publication Date":"公开(公告)日","Number of Claims":"权利要求数量","Number of Document Pages":"文献页数","Number of Citations within 3 Years":"3年内被引用次数","Number of Citations within 5 Years":"5年内被引用次数","Number of Citing Patents":"引用专利数量","Number of Cited Patents":"被引用专利数量","Number of Litigation Cases":"诉讼案件数","Patent Value":"专利价值"})
# 计算皮尔逊相关系数
correlation_matrix = df.corr(numeric_only=True)

# 保存为txt文件
# correlation_matrix.to_csv('../picture/correlation_matrix.txt', sep='\t')
correlation_matrix.to_csv('../picture/correlation_matrix.txt', sep='\t', float_format='%.2f', lineterminator='\n')