# -*- coding: utf-8 -*-

#导入要用的程序包
import pandas as pd
import random
from sklearn.metrics import accuracy_score as acs
#导入程序
data = pd.read_excel("feidata.xlsx")
#数据清理
del data['序号']

school = list(set(data['学校']))
s = []
for i in range(len(data)):
    s.append(school.index(data['学校'].iloc[i]))
data['学校'] = s
#%%
for i in range(len(data)):
    for j in [-8,-7,-6,-5,-4,-3,-2,-1]:
        if data.iloc[i,j] in [1,2,3]:
           data.iloc[i,j] = 0
        elif data.iloc[i,j] in [4,5,6]:
           data.iloc[i,j] = 1   

#%%
#训练集规模，按全体样本的0.9作为训练集，剩下的是测试集
r = 0.9
train_index = random.sample(list(range(len(data))),int(r*len(data)))
test_index = []
for i in range(len(data)):
    if i not in train_index:
        test_index.append(i)

train_data = data[data.index.isin(train_index)]
test_data = data[data.index.isin(test_index)]

x_t = train_data.iloc[:,0:-8]
y_train_mean = train_data.iloc[:,-8:].mean(axis=1)
y_t_1 = train_data.iloc[:,-8]
y_t_2 = train_data.iloc[:,-7]
y_t_3 = train_data.iloc[:,-6]
y_t_4 = train_data.iloc[:,-5]
y_t_5 = train_data.iloc[:,-4]
y_t_6 = train_data.iloc[:,-3]
y_t_7 = train_data.iloc[:,-2]
y_t_8 = train_data.iloc[:,-1]

x = test_data.iloc[:,0:-8]
y_test_mean = test_data.iloc[:,-8:].mean(axis=1)
y_1 = test_data.iloc[:,-8]
y_2 = test_data.iloc[:,-7]
y_3 = test_data.iloc[:,-6]
y_4 = test_data.iloc[:,-5]
y_5 = test_data.iloc[:,-4]
y_6 = test_data.iloc[:,-3]
y_7 = test_data.iloc[:,-2]
y_8 = test_data.iloc[:,-1]

#建立变量储存预测准确率结果
result = []
result.append(['焦虑情绪','抑郁情绪','烦躁情绪','失眠情况',
               '工作压力','家庭压力','经济压力','人际压力','八个指标的均值'])
#开始模型学习和预测
#XGB模型
from xgboost import XGBClassifier
RFC = XGBClassifier()
RFC.fit(x_t, y_train_mean) #new
p_y_mean = RFC.predict(x) #new
RFC.fit(x_t, y_t_1)
p_y_1 = RFC.predict(x)
RFC.fit(x_t, y_t_2)
p_y_2 = RFC.predict(x)
RFC.fit(x_t, y_t_3)
p_y_3 = RFC.predict(x)
RFC.fit(x_t, y_t_4)
p_y_4 = RFC.predict(x)
RFC.fit(x_t, y_t_5)
p_y_5 = RFC.predict(x)
RFC.fit(x_t, y_t_6)
p_y_6 = RFC.predict(x)
RFC.fit(x_t, y_t_7)
p_y_7 = RFC.predict(x)
RFC.fit(x_t, y_t_8)
p_y_8 = RFC.predict(x)
result.append([acs(y_test_mean,p_y_mean),acs(y_1,p_y_1),acs(y_2,p_y_2),acs(y_3,p_y_3),acs(y_4,p_y_4),acs(y_5,p_y_5),acs(y_6,p_y_6),acs(y_7,p_y_7),acs(y_8,p_y_8)])
#随机森林模型
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier()
RFC.fit(x_t, y_train_mean) #new
p_y_mean = RFC.predict(x) #new
RFC.fit(x_t, y_t_1)
p_y_1 = RFC.predict(x)
RFC.fit(x_t, y_t_2)
p_y_2 = RFC.predict(x)
RFC.fit(x_t, y_t_3)
p_y_3 = RFC.predict(x)
RFC.fit(x_t, y_t_4)
p_y_4 = RFC.predict(x)
RFC.fit(x_t, y_t_5)
p_y_5 = RFC.predict(x)
RFC.fit(x_t, y_t_6)
p_y_6 = RFC.predict(x)
RFC.fit(x_t, y_t_7)
p_y_7 = RFC.predict(x)
RFC.fit(x_t, y_t_8)
p_y_8 = RFC.predict(x)
result.append([acs(y_test_mean,p_y_mean),acs(y_1,p_y_1),acs(y_2,p_y_2),acs(y_3,p_y_3),acs(y_4,p_y_4),acs(y_5,p_y_5),acs(y_6,p_y_6),acs(y_7,p_y_7),acs(y_8,p_y_8)])
#极限提升树模型
from sklearn.ensemble import ExtraTreesClassifier
RFC = ExtraTreesClassifier()
RFC.fit(x_t, y_train_mean) #new
p_y_mean = RFC.predict(x) #new
RFC.fit(x_t, y_t_1)
p_y_1 = RFC.predict(x)
RFC.fit(x_t, y_t_2)
p_y_2 = RFC.predict(x)
RFC.fit(x_t, y_t_3)
p_y_3 = RFC.predict(x)
RFC.fit(x_t, y_t_4)
p_y_4 = RFC.predict(x)
RFC.fit(x_t, y_t_5)
p_y_5 = RFC.predict(x)
RFC.fit(x_t, y_t_6)
p_y_6 = RFC.predict(x)
RFC.fit(x_t, y_t_7)
p_y_7 = RFC.predict(x)
RFC.fit(x_t, y_t_8)
p_y_8 = RFC.predict(x)
result.append([acs(y_test_mean,p_y_mean),acs(y_1,p_y_1),acs(y_2,p_y_2),acs(y_3,p_y_3),acs(y_4,p_y_4),acs(y_5,p_y_5),acs(y_6,p_y_6),acs(y_7,p_y_7),acs(y_8,p_y_8)])
#支持向量机模型
from sklearn.svm import SVC
RFC = SVC()
RFC.fit(x_t, y_train_mean) #new
p_y_mean = RFC.predict(x) #new
RFC.fit(x_t, y_t_1)
p_y_1 = RFC.predict(x)
RFC.fit(x_t, y_t_2)
p_y_2 = RFC.predict(x)
RFC.fit(x_t, y_t_3)
p_y_3 = RFC.predict(x)
RFC.fit(x_t, y_t_4)
p_y_4 = RFC.predict(x)
RFC.fit(x_t, y_t_5)
p_y_5 = RFC.predict(x)
RFC.fit(x_t, y_t_6)
p_y_6 = RFC.predict(x)
RFC.fit(x_t, y_t_7)
p_y_7 = RFC.predict(x)
RFC.fit(x_t, y_t_8)
p_y_8 = RFC.predict(x)
result.append([acs(y_test_mean,p_y_mean),acs(y_1,p_y_1),acs(y_2,p_y_2),acs(y_3,p_y_3),acs(y_4,p_y_4),acs(y_5,p_y_5),acs(y_6,p_y_6),acs(y_7,p_y_7),acs(y_8,p_y_8)])
#逻辑斯蒂模型
from sklearn.linear_model import LogisticRegression
RFC = LogisticRegression(solver ='liblinear')
RFC.fit(x_t, y_train_mean) #new
p_y_mean = RFC.predict(x) #new
RFC.fit(x_t, y_t_1)
p_y_1 = RFC.predict(x)
RFC.fit(x_t, y_t_2)
p_y_2 = RFC.predict(x)
RFC.fit(x_t, y_t_3)
p_y_3 = RFC.predict(x)
RFC.fit(x_t, y_t_4)
p_y_4 = RFC.predict(x)
RFC.fit(x_t, y_t_5)
p_y_5 = RFC.predict(x)
RFC.fit(x_t, y_t_6)
p_y_6 = RFC.predict(x)
RFC.fit(x_t, y_t_7)
p_y_7 = RFC.predict(x)
RFC.fit(x_t, y_t_8)
p_y_8 = RFC.predict(x)
result.append([acs(y_test_mean,p_y_mean),acs(y_1,p_y_1),acs(y_2,p_y_2),acs(y_3,p_y_3),acs(y_4,p_y_4),acs(y_5,p_y_5),acs(y_6,p_y_6),acs(y_7,p_y_7),acs(y_8,p_y_8)])
#%%
result = pd.DataFrame(result).T
result.columns = ['目标','XGB','RFC','ETC','SVC','LOG']
print(result)
#%%
##使用SHAP包计算变量重要性并且绘图
import shap
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
#%%
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#%%
RFC.fit(x_t, y_test_mean)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t)
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_1)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_2)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_3)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_4)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_5)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_6)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_7)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)

RFC.fit(x_t, y_t_8)
explainer = shap.Explainer(RFC,x_t)
shap_values = explainer(x_t) 
shap.plots.bar(shap_values,max_display=20)





