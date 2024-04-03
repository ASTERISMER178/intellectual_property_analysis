

import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from matplotlib import MatplotlibDeprecationWarning
from sklearn import preprocessing
from sklearn.model_selection import KFold
# from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib
max_depth = 12
matplotlib.use('TkAgg')  # 切换到Tkinter后端
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用中文黑体字体
# path to the data file
eem_df = pd.read_csv('../Data/model_inputs.CSV')
eem_df = eem_df.rename(columns={"Industry Chain Position":"ICP","Primary Technical Branch":"PTB","Patent Type":"PT","Publication Country":"PC","Publication Date":"PD","Number of Claims":"NC","Number of Document Pages":"NDP","IPC":"IPC","Applicant's Province and City Code":"APCC","Number of Citations within 3 Years":"NC3Y","Number of Citations within 5 Years":"NC5Y","Number of Citing Patents":"NCGP","Number of Cited Patents":"NCDP","Patent Validity":"PV","Number of Litigation Cases":"NLC","Patent Value":"Patent Value","Patent Value Classification":"PVC"
})
eem_df = eem_df[eem_df["PT"] != "Invention Patent"]

train_set_all = eem_df.drop(["PVC","标题","Patent Value","PC"], axis=1)
target_all = eem_df["PVC"]
le = preprocessing.LabelEncoder()
target_cf_all = le.fit_transform(target_all)

train_set_all['PT'] = le.fit_transform(train_set_all['PT'])
train_set_all['ICP'] = le.fit_transform(train_set_all['ICP'])
train_set_all['PTB'] = le.fit_transform(train_set_all['PTB'])
train_set_all['PD'] = le.fit_transform(train_set_all['PD'])
train_set_all['IPC'] = le.fit_transform(train_set_all['IPC'])
train_set_all["APCC"] = le.fit_transform(train_set_all["APCC"])
train_set_all['PV'] = le.fit_transform(train_set_all['PV'])


clf = tree.DecisionTreeClassifier(max_depth=max_depth)
clf.fit(train_set_all, target_cf_all)
pred = clf.predict(train_set_all)
accuracy = np.sum(pred == target_cf_all) / len(target_cf_all)

fig = plt.figure(figsize=(40, 20))
tree.plot_tree(clf, feature_names=train_set_all.columns.tolist(), class_names=['large', 'small'], filled=True)
image_save_path = f'../Result/decision_tree_{max_depth}.png'
print(f'Decision tree image saved to {image_save_path}')
# plt.tight_layout()
plt.savefig(image_save_path)

print(f'accuracy: {100*accuracy:.2f}%')


def node_id_to_depth(clf):

    node_id_layer = {}
    cur_layer = [0]
    nxt_layer = []
    cur_depth = 0
    while len(cur_layer) >= 1:
        for node_id in cur_layer:
            node_id_layer[node_id] = cur_depth
            if clf.tree_.children_left[node_id] != -1:
                nxt_layer.append(clf.tree_.children_left[node_id])
            if clf.tree_.children_right[node_id] != -1:
                nxt_layer.append(clf.tree_.children_right[node_id])
        cur_depth += 1
        cur_layer = nxt_layer
        nxt_layer = []

    return node_id_layer

node_id_layer = node_id_to_depth(clf)

for i_depth in range(max_depth, 0, -1):
    for node_id in range(clf.tree_.node_count):
        if node_id_layer[node_id] >= i_depth:
            clf.tree_.children_left[node_id] = -1
            clf.tree_.children_right[node_id] = -1

    y_test_predict = clf.predict(train_set_all)
    print(f'Accuracy Max layer: {i_depth}, Accuracy: {100 * np.sum(y_test_predict == target_cf_all) / len(target_cf_all):.2f}%')
plt.show()
print('Done!')
