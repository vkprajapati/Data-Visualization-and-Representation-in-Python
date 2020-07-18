# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:03:52 2020

@author: ViShAl
"""
import pandas as pd

url='https://raw.githubusercontent.com/WalePhenomenon/climate_change/master/fuel_ferc1.csv'
fuel_data = pd.read_csv(url, error_bad_lines=False)
fuel_data.describe(include='all')

fuel_data.groupby('report_year')['report_year'].count()
fuel_data[['fuel_unit']] = fuel_data[['fuel_unit']].fillna(value='mcf')
fuel_data.isnull().sum()
fuel_data.groupby('report_year')['report_year'].count()
fuel_data.groupby('fuel_type_code_pudl').first()

fuel_df1 = fuel_data.iloc[0:19000].reset_index(drop=True)
fuel_df2 = fuel_data.iloc[19000:].reset_index(drop=True)
assert len(fuel_data) == (len(fuel_df1) + len(fuel_df2))
pd.merge(fuel_df1, fuel_df2, how="inner")
pd.merge(fuel_df1, fuel_df2, how="outer")
pd.merge(fuel_df1, fuel_df2, how="left")
fuel_data.duplicated().any()

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(7,4))
plt.xticks(rotation=90)
fuel_unit = pd.DataFrame({'unit':['BBL', 'GAL', 'GRAMSU', 'KGU', 'MCF', 'MMBTU', 'MWDTH', 'MWHTH', 'TON'],
            'count':[7998, 84, 464, 110, 11354, 180, 95, 100, 8958]})
sns.barplot(data=fuel_unit, x='unit', y='count')
plt.xlabel('Fuel Unit')
plt.show()
