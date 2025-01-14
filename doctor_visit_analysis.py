# -*- coding: utf-8 -*-
"""Doctor visit analysis.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1htKJuimdQAkU5r2l7N6JHgOtRHoteFhb

### **Loading The Dataset**
"""

import pandas as pd
ds=pd.read_excel('/content/Doctor_visits_analysis.xlsx')
df=ds

"""### **Exploring the Dataset**"""

ds.head()   #used to retrieve first 5 columns in the dataset

ds.tail()     #used to retrieve last 5 columns in the dataset

ds.describe()   #describe method is used to find statistics of the dataset

ds.dtypes   #dtypes method is used to find the datatypes of all the columns.

ds.info()    #info method is used to find the count of null values in each column along with the column name and its respective datatype.

ds["illness"].value_counts()

ds['gender'].value_counts()    #value_counts() method is used to find the number of unique values in a column along with their count

ds.isnull().sum()      #this method is used to find the number of null values in the column.

"""### Data Cleaning"""

ds['age']=ds['age']*100
ds

df = df.drop(ds[(ds.visits==0)].index)       #this df variable contains only the rows where the number of visits is not '0'.
df

"""### Data Visualization Using Matplotlib"""

import matplotlib.pyplot as plt
fd=ds[ds['visits']>=1]
visit_counts=fd['gender'].value_counts()
plt.bar(visit_counts.index, visit_counts.values)
plt.xlabel('Gender')
plt.ylabel('Number of Visits')
plt.title('Number of Visits based on Gender')
plt.show()

c1=ds['private'].value_counts()
plt.bar(c1.index,c1.values)
plt.xlabel('Yes or No')
plt.ylabel('Number of people ')
plt.title('Count of people for private insurance')
plt.show()

c2=ds['freepoor'].value_counts()
plt.bar(c2.index,c2.values)
plt.xlabel('Yes or No')
plt.ylabel('Number of people ')
plt.title('Count of people for government insurance of poor people')
plt.show()

df.groupby(['gender','reduced']).mean()

import seaborn as sns
plt.figure(figsize=(10,10))
sns.heatmap(ds.corr(),cbar=True,annot=True,cmap='Reds')

plt.figure(figsize=(8,8))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')

label=['yes','no']
Y=df[df['freepoor']=='yes']
N=df[df['freepoor']=='no']
x= [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x, labels=label,autopct='%1.1f%%')
plt.title("% of people getting govt health insurance due to low income")
plt.show()

label=['yes','no']
Y=df[df['private']=='yes']
N=df[df['private']=='no']++++++
x= [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people having private health insurance ")
plt.show()

label=['yes','no']
Y=df[df['freerepat']=='yes']
N=df[df['freerepat']=='no']
x= [Y.shape[0],N.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label)
plt.title("% of people getting govt health insurance due to old age,disability or verteran status")
plt.show()

db=ds.groupby('gender')['reduced'].sum().to_frame().reset_index()
plt.barh(db['gender'],db['reduced'],color=['pink','purple'])
plt.title("Reduced activity vs gender")
plt.xlabel('gender')
plt.ylabel('reduced activity')
plt.show()

