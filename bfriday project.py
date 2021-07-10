# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 10:17:15 2021

@author: Alpana
"""

import pandas as pd

bfriday = pd.read_csv("bfriday data set.csv")

bfriday.head(10)

#dimensions of data set
bfriday.shape

#calculate number of null values for each category
bfriday.isnull().sum()

#Unique and Non Unique calculation
bfriday.Gender.unique()
bfriday.Gender.nunique()
bfriday.Age.unique()
bfriday.Occupation.unique() #It is a discrete data
bfriday.Stay_In_Current_City_Years.unique()
bfriday.Marital_Status.unique()
bfriday.City_Category.unique()

#category description
bfriday.Product_Category_1.unique()
bfriday.Product_Category_2.unique()
bfriday.Product_Category_3.unique()

bfriday.Product_Category_1.shape[0]

#proportion of null
bfriday.isnull().sum()/bfriday.shape[0]

#no. of unique values for all columns
for i in bfriday.columns:
    print (i, ':' , bfriday[i].nunique())

bfriday['User_ID'].nunique()

bfriday.drop("Product_Category_1",axis = 1, inplace = True)

bfriday.Product_Category_2.fillna("other",inplace = True)

#x - bfriday_x
#y - bfriday_y
X = bfriday.drop(["Purchase"], axis=1)

bfriday_y = bfriday["Purchase"]
bfriday_x = pd.get_dummies(bfriday)

#spiltting the data
from sklearn.model_selection import train_test_split
train_x,test_x, train_y, test_y = train_test_split(bfriday_x,bfriday_y, test_size = 0.2)




















