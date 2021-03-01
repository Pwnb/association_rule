#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Set work directory
import os
os.getcwd()
os.chdir("C:\\Users\\Bryan\\Desktop\\")
os.getcwd()

# Import packages
import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import numpy as np
from datetime import datetime

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns

from pymining import itemmining, assocrules

import ast


# In[ ]:


#data importing
df = pd.read_csv('aaa.csv')
df.head(100)


# In[20]:


#get the model input - freq  (a series: index is order number ) 
df = df.rename(columns = {'日历日(YYYY-MM-DD)':'日期','类别描述':'商品类别'})
df['日期'] = pd.to_datetime(df['日期'])
df = df[(df['日期']>='2020/08/28')&(df['日期']<='2020-09-29')]
df.head()

# groupby combine str
#freq = df.groupby('零售小票编号')['类别描述'].apply(lambda x: "[%s]" % ','.join(x))
freq = df.groupby('零售小票编号')['商品类别'].apply(lambda x: ','.join(x))
freq = freq.map(lambda x: x.strip(',').split(','))


# In[56]:


relim_input = itemmining.get_relim_input(freq)
report = itemmining.relim(relim_input, min_support=30)
report


# In[57]:


rules1 = assocrules.mine_assoc_rules(report, min_support=30, min_confidence=0.5)
rules1


# In[58]:


a = []
for line in rules1:
    ## (len(line[0])>1 or len(line[1])>1) could be added for filtering - k-itme set>2  ##
    if ('未知'not in line[0] and '未知'not in line[1]):
        a.append(line)


# In[59]:


result = pd.DataFrame(a, columns = ['first_set', 'second_set', 'support','confidence'])
result.head()


# In[60]:


sets = result['second_set']

a = [list(x) for x in sets]

a


# In[61]:


sets = [frozenset({'a', 'c,'}), frozenset({'h,', 'a,'})]

a = [list(x) for x in sets]

a


# In[62]:


result.sort_values(by = 'confidence', ascending = False).head(20)


# In[63]:


result.sort_values(by = 'support', ascending = False)


# In[ ]:





# In[ ]:




