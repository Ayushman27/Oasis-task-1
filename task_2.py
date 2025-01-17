# -*- coding: utf-8 -*-
"""task_2.ipynb


Original file is located at
    https://colab.research.google.com/drive/1WqDZgNzjpUX_viBsPnBtlmTr-sRH1JWx
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd

df = pd.read_csv('/content/drive/MyDrive/Unemployment_Rate_upto_11_2020.csv')

df.head()

df.tail()

df.shape

df.info()

df.describe()

x = df['Region']
x

y = df[' Estimated Unemployment Rate (%)']
y

df2 = df.iloc[:3]
df2

import plotly.express as px
import matplotlib.pyplot as plt

fg = px.bar(df,x = 'Region',y = ' Estimated Unemployment Rate (%)',color = 'Region',title = 'Unemployment Rate (state-wise) by bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg = px.bar(df,x = 'Region.1',y = ' Estimated Unemployment Rate (%)',color = 'Region',title = 'Unemployment Rate (Region-wise) by bar Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg = px.box(df, x = 'Region',y = ' Estimated Unemployment Rate (%)',color = 'Region',title = 'Unemployment Rate (state-wise) by box Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()

fg = px.box(df, x = 'Region.1',y = ' Estimated Unemployment Rate (%)',color = 'Region',title = 'Unemployment Rate (Region-wise) by box Graph',template='plotly')
fg.update_layout(xaxis={'categoryorder':'total descending'})
fg.show()
