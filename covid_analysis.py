#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[99]:


sns.set(rc={'figure.figsize':(11.8,8.7)})


# In[9]:


data = pd.read_csv("/Users/gup9905/Desktop/DataAnalytics/Covid_Analysis/archive/StatewiseTestingDetails.csv")


# In[12]:


data_india = pd.read_csv("/Users/gup9905/Desktop/DataAnalytics/Covid_Analysis/archive/covid_19_india.csv")


# In[31]:


data_vaccine = pd.read_csv("/Users/gup9905/Desktop/DataAnalytics/Covid_Analysis/archive/covid_vaccine_statewise.csv")


# In[32]:


data_italy =pd.read_csv("/Users/gup9905/Desktop/DataAnalytics/Covid_Analysis/archive/covid19_italy_region.csv")


# In[33]:


data_italy.head()


# In[34]:


data_italy_province =pd.read_csv("/Users/gup9905/Desktop/DataAnalytics/Covid_Analysis/archive/covid19_italy_province.csv")


# In[35]:


data_italy_province.head()


# In[15]:


data.head()


# In[24]:


data.tail()


# In[16]:


data_india.head()


# In[17]:


data_india.tail()


# In[18]:


data.columns


# In[19]:


data.describe()


# In[18]:


data_india.describe()


# In[19]:


data_vaccine.describe()


# In[36]:


data_italy.columns


# # relating the variables with scatterplots

# In[87]:


sns.pairplot(data_italy)


# In[91]:


data_italy.columns


# In[98]:


sns.relplot(x='TotalPositiveCases',y='HomeConfinement', data=data_italy)


# In[90]:


sns.relplot(x='TotalPositiveCases',y='Recovered', data=data_italy)


# In[93]:


sns.relplot(x='TotalPositiveCases', y='TotalHospitalizedPatients', hue='RegionName', data=data_italy)


# In[100]:


data_india.columns


# In[102]:


sns.relplot(x='Date', y='Cured', hue='State/UnionTerritory', data=data_india)


# In[ ]:


sns.relplot(x='Confirmed', y='Deaths', hue='State/UnionTerritory', data=data_india)


# In[103]:


sns.relplot(x='Date', y='Deaths', hue='State/UnionTerritory', data=data_india)


# In[67]:


data_italy.columns


# In[95]:


sns.relplot(x ='TotalPositiveCases', y ='HomeConfinement',hue='RegionName' , data = data_italy)


# In[96]:


sns.relplot(x ='TotalPositiveCases', y ='Deaths',hue='RegionName' , data = data_italy)


# In[49]:


sns.lineplot(x='TotalPositiveCases', y='Deaths', data=data_italy)


# In[55]:


sns.lineplot(x='TestsPerformed', y='TotalPositiveCases', data=data_italy)


# In[25]:


data.columns


# In[22]:


data_india.columns


# In[83]:


sns.relplot(x='Date',y='Deaths', hue = 'State/UnionTerritory', data=data_india)


# In[56]:


sns.relplot(x='TotalSamples', y='Positive', data=data)


# In[104]:


data_vaccine.columns


# In[111]:


sns.relplot(x='Male(Individuals Vaccinated)', y='Total Individuals Vaccinated', data=data_vaccine)


# In[112]:


sns.relplot(x='Female(Individuals Vaccinated)', y='Total Individuals Vaccinated', data=data_vaccine)


# In[119]:


sns.relplot(x='Total Doses Administered', y='Total Sputnik V Administered', data=data_vaccine)


# In[121]:


sns.relplot(x='Total Doses Administered', y='Total CoviShield Administered', data=data_vaccine)


# In[ ]:





# In[120]:


sns.relplot(x='Total Doses Administered', y='Total Covaxin Administered', data=data_vaccine)

