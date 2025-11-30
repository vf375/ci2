#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import pandas as pd


# In[ ]:


import matplotlib.pyplot as plt


# In[ ]:


graph_data = pd.read_csv("graph.csv", index_col=0, sep=";", decimal=",")


# In[2]:


graph_data.plot()

# In[3]:

plt.savefig("graph.png")






