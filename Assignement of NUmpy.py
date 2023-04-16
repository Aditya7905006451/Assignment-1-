#!/usr/bin/env python
# coding: utf-8

# . Create a null vector of size 10 but the fifth value which is 1.

# In[1]:


import numpy as np


# In[2]:


a= np.zeros(10,dtype='int32')


# In[3]:


a


# In[4]:


a[4]=1


# In[5]:


a


#  Create a vector with values ranging from 10 to 49.

# In[11]:


a=np.random.randint(10,49,size=(10))
print(a)


#  Create a 3x3 matrix with values ranging from 0 to 8

# In[12]:



a = np.random.randint(0,8,size=(3,3))
print(a)
     


# Find indices of non-zero elements from [1,2,0,0,4,0]

# In[19]:


a= np.array([1,2,0,0,4,0])


# In[25]:


for i in range(6):
    if a[i]!=0 :
        print(a[i])
        


# Create a 10x10 array with random values and find the minimum and maximum values.

# In[26]:


a= np.random.rand(10,10)


# In[27]:


a


# In[30]:


print(np.min(a))


# In[31]:


print(np.max(a))


#  Create a random vector of size 30 and find the mean value.

# In[32]:



a= np.random.randint(0,100,size=(30))
print(a)
     


# In[33]:


np.mean(a)


# In[ ]:




