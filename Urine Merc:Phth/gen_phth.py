# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 10:53:28 2015

@author: kyu
"""

import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import pandas as pd


A = pd.read_csv('PHPYPA_A.csv')
B = pd.read_csv('PHPYPA_B.csv')
C = pd.read_csv('PHPYPA_C.csv')
D = pd.read_csv('PHTHTE_D.csv')
E = pd.read_csv('PHTHTE_E.csv')
F = pd.read_csv('PHTHTE_F.csv')
G = pd.read_csv('PHTHTE_G.csv')

def get_trend(column):
    
    B_SEQN = B['SEQN']
    C_SEQN = C['SEQN']
    D_SEQN = D['SEQN']
    E_SEQN = E['SEQN']
    F_SEQN = F['SEQN']
    G_SEQN = G['SEQN']

    B_m = (B[column])
    C_m = (C[column])
    D_m = (D[column])
    E_m = (E[column])
    F_m = (F[column])
    G_m = (G[column])
    
    
    
    X = ['SEQN2001', 2001, 'SEQN2003', 2003, 'SEQN2005', 2005, 'SEQN2007',\
                                    2007, 'SEQN2009', 2009, 'SEQN2011', 2011]
    Y = [B_SEQN, B_m, C_SEQN, C_m, D_SEQN, D_m, E_SEQN,E_m, F_SEQN, \
                                                            F_m, G_SEQN, G_m]
    df = pd.DataFrame()
    
    count = 0
    for value in X:
        df[value] = Y[count]
        count = count + 1
    
    
    to_name  = column + '.csv'
    df.to_csv(to_name)
    return (df)
    
##########################################

MEP = get_trend('URXMEP')
MHP = get_trend('URXMHP')
MNP = get_trend('URXMNP')
MNM = get_trend('URXMNM')
MHH = get_trend('URXMHH')
MOH = get_trend('URXMOH')
MIB = get_trend('URXMIB')



# put into datafile for output


## reorganize data for jmp
#plt.boxplot(data[1], labels = data[0], showmeans=True)
#plt.ylim([0, 2])









