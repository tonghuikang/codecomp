#!/usr/bin/env python
# coding: utf-8

# In[101]:


# %reset -sf


# In[102]:


# import matplotlib.pyplot as plt


# In[103]:


import sys
import numpy as np
import pandas as pd
import lightgbm as lgb


# In[104]:


# with open("g0", "r") as f:
#     lines = f.readlines()

lines = sys.stdin.readlines()


# In[105]:


n,m = [int(x) for x in lines[0].split()]
train_data = []
for line in lines[1:n+1]:
    lst = [list(map(int,x.split(":"))) for x in line.split()]
    train_data.append([[x[0] for x in lst], [x[1] for x in lst]])
targets = []
for line in lines[n+1:n+1+n]:
    targets.append(int(line))
test_data = []
for line in lines[n+1+n:n+1+n+m]:
    lst = [list(map(int,x.split(":"))) for x in line.split()]
    test_data.append([[x[0] for x in lst], [x[1] for x in lst]])


# In[106]:


def process_data(dataset):
    processed = []
    for loc,time in dataset:
        time = [0] + [b-a for a,b in zip(time, time[1:])]*200
        time = time[:200]
        loc = loc*200
        loc = loc[:200]
        processed.append(time + loc)
    return processed


# In[107]:


train_data_p = process_data(train_data)
len(train_data_p[0])


# In[108]:


train_data_p = process_data(train_data)
test_data_p = process_data(test_data)
target_train = np.array(targets)
df_train = pd.DataFrame(train_data_p)
df_test = pd.DataFrame(test_data_p)


# In[109]:


eval_set = np.array([True if i < len(df_train)*0.2 else False for i in range(len(df_train))])
lgb_train = lgb.Dataset(df_train[~eval_set], target_train[~eval_set])
lgb_eval = lgb.Dataset(df_train[eval_set], target_train[eval_set], reference=lgb_train)
lgb_all = lgb.Dataset(df_train, target_train)


# In[110]:


params = {
#     'boosting_type': 'gbdt',
    'objective': 'binary',
    'verbose': -1,
#     'metric': {'auc'},
#     'num_leaves': 15,
#     'learning_rate': 0.05,
#     'feature_fraction': 0.9,
#     'bagging_fraction': 0.8,
#     'bagging_freq': 5,
#     'verbose': 1,
}


gbm = lgb.train(params,
                lgb_train,
#                 num_boost_round=1000,
                valid_sets=lgb_eval,
                verbose_eval=False,
                early_stopping_rounds=5)


# In[111]:


# gbm = lgb.train(params,
#                 lgb_all,
# #                 num_boost_round=1000,
# #                 valid_sets=lgb_eval,
#                 verbose_eval=10,
# #                 early_stopping_rounds=5
#                )


# In[112]:


pred_test = gbm.predict(df_test, num_iteration=gbm.best_iteration)


# In[113]:


# plt.hist(pred_test)


# In[114]:


res = [int(x > 0.5) for x in pred_test]
print("\n".join(str(x) for x in res))


# In[ ]:


# !jupyter nbconvert --to script *.ipynb


# In[ ]:





# In[ ]:




