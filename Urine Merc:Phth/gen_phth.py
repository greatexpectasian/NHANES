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
    A_m = (A[column])
    B_m = (B[column])
    C_m = (C[column])
    D_m = (D[column])
    E_m = (E[column])
    F_m = (F[column])
    #G_m = mean(G[column])
    
    A_s = std(A[column])
    B_s = std(B[column])
    C_s = std(C[column])
    D_s = std(D[column])
    E_s = std(E[column])
    F_s = std(F[column])
    #G_s = std(G[column])
    
    
    X = [1999, 2001, 2003, 2005, 2007, 2009]
    Y = [A_m, B_m, C_m, D_m, E_m, F_m]
    Y_s = [A_s, B_s, C_s, D_s, E_s, F_s]
    return (X, Y, Y_s)

##########################################

data = get_trend('WTSPH2YR')

plt.boxplot(data[1], labels = data[0], showmeans=True)
plt.ylim([0, 2])









