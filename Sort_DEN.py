# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:59:54 2015

@author: kyu
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import numpy as np
import pandas as pd

# import data into different channel capacities indexed by label_well 

def get_restoration(fname):
    
    df_B = pd.read_csv(fname, low_memory = False)
    
    name = df_B['SEQN']
    
    # subset for coronary tooth count
    CTC = df_B.filter(like="CTC")
    
    
    restoration = []
    for row in CTC.iterrows():
        count = 0
        for tooth in row[1]:
            if tooth == 'R' or tooth == 'T' or tooth == 'X':
                count = count + 1
        restoration.append(count)
    
    df_rest = pd.DataFrame(restoration, columns = ['restorations'])
    df_rest['SEQN'] = name
    
    # sort
    grouped = get_sort(restoration)
    df_rest['Grouped Restoration'] = grouped
    
    #output to excel
    out_name = 'mod_'+ fname[:8] + '.xls'
    df_rest.to_excel(out_name)
    
    return grouped


# count function:
def get_sort(rest_data):
    sorter = []
    for x in rest_data:
        if x == 0:
            sorter.append(0)
        elif x > 0 and x <= 3:
            sorter.append(1)
        else:
            sorter.append(2)
    return sorter
    
# get restoration for all:

a = get_restoration('OHXDEN_A.csv')
plt.subplot(411)
plt.hist(a)
b = get_restoration('OHXDEN_B.csv')
plt.subplot(412)
plt.hist(b)
c = get_restoration('OHXDEN_C.csv')
plt.subplot(413)
plt.hist(c)
d = get_restoration('OHXDEN_G.csv')
plt.subplot(414)
plt.hist(d)

