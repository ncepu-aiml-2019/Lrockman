#!/usr/bin/env python
# coding: utf-8

# In[8]:


for i in range(2,101):
    fg = 0
    for l in range(2,i):
        if i % l == 0:
            fg = 1
            break
    if fg == 0:
        print (i)


# In[ ]:




