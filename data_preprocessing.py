"""
    数据预处理，最后生成./Data/DataProcessed.xlsx
"""

import re

import pandas as pd

data_file = './Data/2021年专利质押转让_clean.xls'

# read data
data_pd = pd.read_excel(data_file)


data_format_columns = ['Seq', 'Subseq', 'PatentName', 'PatentNumber', 'PatentType', 'EstimateValue', 'BaseDate', 'ReportDate', 'Loan']
data_format_pd = pd.DataFrame(columns=data_format_columns)

PatentType = ('实用新型', '发明', '外观设计', '发明专利')

for i_row in range(len(data_pd)):

    patent_type = None
    lines = re.split('\n', data_pd.iloc[i_row, 2].strip())
    subseq = 0

    for j_row in range(len(lines)):
        if len(lines[j_row].strip()) == 0:
            # 空行
            continue
        line = lines[j_row].strip()
        fields = re.split(r'\s+', line)

        subseq += 1
        i_field = 1 if fields[0].isdigit() else 0

        newline = {}
        newline['Seq'] = int(data_pd.iloc[i_row, 0])
        newline['Subseq'] = subseq

        while i_field < len(fields):
            if fields[i_field].startswith('ZL') or fields[i_field].startswith('BS'):
                patent_number = fields[i_field]
                i_field += 1
                while i_field < len(fields):
                    if fields[i_field].isascii():
                        patent_number += fields[i_field]
                        i_field += 1
                    else:
                        break
                newline['PatentNumber'] = patent_number

            elif fields[i_field] in PatentType:
                newline['PatentType'] = fields[i_field]
                i_field += 1

            elif 'PatentName' not in newline:
                newline['PatentName'] = fields[i_field]
                i_field += 1
            else:
                print(f"Warning: {newline['Seq']}-{newline['Subseq']}: {fields[i_field]}")
                i_field += 1

        newline['EstimateValue'] = data_pd.iloc[i_row, 3]
        newline['BaseDate'] = data_pd.iloc[i_row, 4]
        newline['ReportDate'] = data_pd.iloc[i_row, 5]
        newline['Loan'] = data_pd.iloc[i_row, 6]

        if 'PatentNumber' not in newline:
            print(f"{newline['Seq']}-{newline['Subseq']} 无专利号")
        else:
            newline_arr = [newline.get(x, '') for x in data_format_columns]
            data_format_pd.loc[len(data_format_pd)] = newline_arr

data_format_pd['BaseDate'] = data_format_pd['BaseDate'].dt.strftime('%Y-%m-%d').apply(str)
data_format_pd['ReportDate'] = data_format_pd['ReportDate'].dt.strftime('%Y-%m-%d').apply(str)
data_format_pd.to_excel('./Data/DataProcessed.xlsx', index=False)
