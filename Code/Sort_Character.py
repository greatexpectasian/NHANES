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


def get_sr(fname):
        
    df_B = pd.read_csv(fname, low_memory = False)
        
    name = df_B['SEQN']
    # subset for coronary tooth count
    CSC = df_B.filter(like="CSC")
       
    sr = []
    for row in CSC.iterrows():
        count = 0
        for tooth in row[1]:
            str_t = str(tooth)
            if tooth == 56789.0 or np.isnan(tooth):
                count = count
            else:
                rest = str_t.count('5') + str_t.count('6') + str_t.count('7') + \
                                    str_t.count('8') + str_t.count('9')
                count = count + rest
        sr.append(count)
        
        
    df_sr = pd.DataFrame(sr, columns = ['Surface_Rest_num'])
    df_sr['SEQN'] = name
    
    grouped = get_sort(sr)
    df_sr['Surface_Rest_Group'] = grouped

    #output to excel
    out_name = 'mod_surface'+ fname[:8] + '.xls'
    df_sr.to_excel(out_name)
    
    return sr

def get_sort(rest_data):
    sorter = []
    for x in rest_data:
        if x == 0:
            sorter.append(0)
        elif x > 0 and x <= 8:
            sorter.append(1)
        elif x > 8:
            sorter.append(2)
        else:
            sorter.append(nan)
    return sorter












a = get_sr('OHXDEN_A.csv')
b = get_sr('OHXDEN_B.csv')
c = get_sr('OHXDEN_C.csv')
d = get_sr('OHXDEN_G.csv')

