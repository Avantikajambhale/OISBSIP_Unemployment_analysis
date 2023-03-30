#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/unemployment.csv")


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df.tail()


# In[6]:


df.info()


# In[7]:


df.describe()


# In[8]:


df.dropna()


# In[9]:


df.isnull().sum()


# In[10]:


df.columns = ["States","Date","Frequency","Estimated Unemployment Rate","Estimated Employed",
              "Estimated Labour Participation Rate","Region","longitude","latitude"]


# In[11]:


df.info()


# In[12]:


import seaborn as sns
plt.style.use('seaborn-whitegrid')
plt.figure(figsize = (12,10))
plt.title('Unemployment')
sns.heatmap(df.corr())


# In[13]:


pip install -U seaborn


# In[14]:


pip install --upgrade matplotlib


# In[15]:


import plotly.express as ps
unemployment = df[["States", "Region", "Estimated Unemployment Rate"]]
figure = ps.sunburst(unemployment, path=["Region", "States"], 
                     values="Estimated Unemployment Rate", 
                     width=700, height=700, color_continuous_scale="RdY1Gn", 
                     title="Unemployment Rate in India")
figure.show()


# In[ ]:




