#!/usr/bin/env python
# coding: utf-8

# In[1]:


# action 2 method 2
import pandas as pd
from pandas import Series, DataFrame
# 写入需要处理的数据
data = {'Chinese':[68,95,98,90,80],'Math':[65,76,86,88,90],'English':[30,98,88,77,90],'Total':[0,0,0,0,0]}
df1 = DataFrame(data,index=['ZhangFei','GuanYu','LiuBei','DianWei','XuChu'], columns=['Chinese','Math','English','Total'])

df1['Total']=df1.sum(axis=1)

#输出统计结果
print (df1.describe())

print ("============================================")
#输出按总成绩倒序排名
print ('总成绩排名如下：')
print (df1.sort_values('Total',ascending=False))


# In[ ]:




