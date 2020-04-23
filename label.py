#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:40:16 2020

@author: harshit
"""

import pandas as pd
data = pd.read_csv('news2.csv')

for i in range(2000):
    data['Label'] = 0
for i in range(2000):
    data.loc[data['headline_category'] == 'india', 'Label'] = 1
for i in range(2000):
    data.loc[data['headline_category'] == 'unknown', 'Label'] = 2

    
data.to_csv('news_label.csv')

data1 = pd.read_csv('kmeans_clustered_output.txt', sep=',')