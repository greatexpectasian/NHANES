# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 11:48:26 2015

@author: kyu
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import numpy as np
import pandas as pd


fname = 'OHXDEN_A.csv'
df_B = pd.read_csv(fname, low_memory = False)
    
name = df_B['SEQN']
# subset for coronary tooth count
CSC = df_B.filter(like="CSC")


    
   
restoration = []
for row in CSC.iterrows():
    count = 0
    for tooth in row[1]:
        #if tooth == 56789:
            
        if tooth 