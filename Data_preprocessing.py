#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno

DATASET_PATH = "C:/Users/vs_00/Desktop/Internship/SAS/Covid/archive/owid-covid-data.csv"
d1 = pd.read_csv(DATASET_PATH)
d1['date'] = pd.to_datetime(d1['date'])

d1.describe()

d1.info()

d1.shape

# d1.plot()


# d1.corr()


# sns.heatmap(d1.corr())


# In[9]:


# plt.subplots(figsize=(20,15))
# sns.heatmap(d1.corr())
# plt.savefig('Correlation Heatmap')


newcases = d1[["new_cases", "reproduction_rate", "date", "hosp_patients", "weekly_hosp_admissions", "new_tests",
               "total_vaccinations", "people_vaccinated", "new_vaccinations", "population"]]

newcases.head()

# In[12]:


newcases.tail()

sns.heatmap(newcases.corr())

# dropping reproduction rate
del newcases["reproduction_rate"]

# In[15]:


newcases.describe()

# In[16]:


newcases.info()

# In[17]:


msno.matrix(newcases)

# In[18]:


msno.bar(newcases)
plt.savefig("missing values bar chart")

# In[19]:


## deleting certail columns due to high collinearity
newcases.drop(columns=["total_vaccinations", "people_vaccinated"], axis=1, inplace=True)

# In[20]:


newcases.info()

# In[21]:


plt.scatter(y=newcases['new_cases'], x=newcases['hosp_patients'])
plt.xlabel("hospitalized patients")
plt.ylabel("new cases")

# In[22]:


plt.scatter(y=newcases['new_cases'], x=newcases['new_vaccinations'])
plt.xlabel("new vaccinations")
plt.ylabel("new cases")

# In[23]:


plt.scatter(y=newcases['new_cases'], x=newcases['date'])
plt.xlabel("date")
plt.ylabel("new cases")

# In[24]:


sns.boxplot(newcases['new_cases'])

# In[25]:


newcases.boxplot(column="new_cases")

# In[26]:


d1.boxplot(column="new_cases_per_million")

# In[27]:


d2 = newcases.copy()

# In[28]:


d2.head()

# In[29]:


d2.fillna(method='bfill')

# In[30]:


plt.scatter(y=d2['new_cases'], x=d2['date'])
plt.xlabel("date")
plt.ylabel("new cases")

# In[31]:


newcases.interpolate(method='linear', inplace=True)

# In[32]:


newcases.info()

# In[33]:


d2 = d1[["new_deaths", "date", "new_cases", "icu_patients", "hosp_patients", "new_tests", "people_vaccinated",
         "population"]]

# In[ ]:


# In[34]:


sns.heatmap(d2.corr())

# In[35]:


plt.scatter(y=d2["hosp_patients"], x=d2["people_vaccinated"])
plt.ylabel("Hospitalized patients")
plt.xlabel("People Vaccinated")

# In[36]:


plt.scatter(y=d2["new_deaths"], x=d2["icu_patients"])
plt.ylabel("New Deaths")
plt.xlabel("ICU Patients")

# In[37]:


d2['new_deaths'].mean()

# In[38]:


d2['icu_patients'].mean()

# In[39]:


plt.scatter(y=d2["new_deaths"], x=d2["people_vaccinated"])
plt.ylabel("New Deaths")
plt.xlabel("People Vaccinated")

# In[40]:


plt.scatter(y=d2["people_vaccinated"], x=d2["date"])
plt.ylabel("People Vaccinated")
plt.xlabel("Date")

India = d1[d1["location"] == "India"]

plt.scatter(y=India["people_vaccinated"], x=India["date"])
plt.ylabel("People Vaccinated")
plt.xlabel("Date")

plt.scatter(y=India["new_cases"], x=India["date"])
plt.ylabel("New Cases")
plt.xlabel("Date")
