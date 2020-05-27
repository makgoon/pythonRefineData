#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


selloutData = pd.read_csv("E:/kopocloud/dataset/kopo_channel_seasonality_new.csv")


# In[4]:


selloutData.head(2)


# In[5]:


selloutData["YEAR"] = pd.to_numeric(selloutData["YEARWEEK"].astype(str).str[:4])
selloutData["WEEK"] = pd.to_numeric(selloutData["YEARWEEK"].astype(str).str[4:])

selloutData.dtypes


# In[87]:


###52주 한정 데이터 생성

oeweekorgin = selloutData[(selloutData.WEEK <= 52)]


# In[8]:


firstanswer= selloutData.loc[(selloutData.REGIONID == "A01")&
                            (selloutData.YEAR == 2015)]


# In[9]:


firstanswer


# In[34]:


groupkey = ["PRODUCT"]


# In[60]:


firstgroupdata = firstanswer.groupby(by=groupkey)["QTY"].agg(["mean"])


# In[61]:


firstgroupdata.rename(columns = {'mean':'AVG_QTY'},
                     inplace = True)


# In[62]:


sortKey = ["AVG_QTY"]


# In[63]:


firstgroupdata = firstgroupdata.reset_index()


# In[67]:


sortedData = firstgroupdata.sort_values(sortKey)


# In[68]:


sortedData


# In[43]:


secondanswer = selloutData.loc[(selloutData.REGIONID == "A01")&
                               (selloutData.YEAR == 2015)]


# In[44]:


secondanswer


# In[45]:


secondanswer.loc[:,["PRODUCT"]].drop_duplicates().reset_index()


# In[95]:


thridanswer = selloutData.loc[(selloutData.YEAR == 2015)]


# In[102]:


thridanswer


# In[96]:


thridanswerweek = thridanswer.loc[(thridanswer.WEEK < 14)]


# In[103]:


thridanswerweek


# In[109]:


groupKey = ["REGIONID"]


# In[110]:


thridanswerweekavgr = thridanswerweek.groupby(by=groupKey)["QTY"].agg(["mean"]) 


# In[111]:


thridanswerweekavgr


# In[112]:


thridanswerweekavg = thridanswerweekavgr.reset_index()


# In[113]:


thridanswerweekavg.rename(columns = {'mean':'AVG_QTY'},
                     inplace = True)


# In[114]:


thridanswerweekavg


# In[117]:


sortKey = ["AVG_QTY"]


# In[118]:


thridanswerweekavg.sort_values(sortKey, ascending = [True])


# In[124]:


import warnings


# In[125]:


warnings.filterwarnings(action="ignore")


# In[131]:


def quercheck(inColumn):
    if inColumn <14:
        outValue = "1Q"
    elif inColumn <27:
        outValue = "2Q"
    elif inColumn < 40:
        outValue = "3Q"
    elif inColumn >= 40:
        outValue = "4Q"
    return outValue


# In[132]:


oeweekorgin["Qt"] = oeweekorgin.WEEK.apply(quercheck)


# In[139]:


groupKey = ["Qt"]


# In[140]:


oeweekorgin = oeweekorgin.groupby(by=groupKey)["QTY"].agg(["mean"]) 


# In[141]:


fourthanswer = oeweekorgin.rename(columns = {'mean':'AVG_QTY'})


# In[142]:


fourthanswer

