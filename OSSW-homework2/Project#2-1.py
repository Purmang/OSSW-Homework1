# -*- coding: utf-8 -*-
"""Project #2-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZJH_kKdSTJ_FOkqwL24n1K4IXPvk5Nhy
"""

import pandas as pd
from pandas import Series, DataFrame
data=pd.read_csv('2019_kbo_for_kaggle_v2.csv')

pd.set_option('display.max_columns',None)

temp=2015
for year in range(2015,2019):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",temp,"년@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n")
    for item in ['H','avg','HR','OBP']:
      print(item+")")
      display(data[(data['year']==year)].sort_values(by=[item],ascending=False).head(10))
      print("\n")
    temp=temp+1

data[data['year']==2018][['batter_name','war','tp','year']].sort_values(by=['war'],ascending=False).drop_duplicates('tp')

df=pd.DataFrame(data.corrwith(data['salary']),columns=['salary'])

df2=df.loc[['R','H','HR','RBI','SB','war','avg','OBP','SLG']]

df2[df2['salary'].isin(df2.max())] #df2.isin(df2.max())