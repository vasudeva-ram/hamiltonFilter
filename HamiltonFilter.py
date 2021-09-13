# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 22:53:21 2019

Hamilton Filter: Implements Hamilton(2016) alternate to HP filter

@author: Vasudeva
"""
import numpy as np
import pandas as pd

def hamiltonFilter(array, p: int = 4, h: int = 8):
    """ Takes an array and returns two arrays - the predicted evolution of
    the series ("trend"), and the deviation from that prediction ("cycle").
    """
    
    ind = array.index
    nm = array.name
    array = np.asarray(array)
    y = pd.DataFrame(array, columns = ['Y'])
    y.dropna(inplace=True)    
    
    # Creating X matrix - break off as separate function
    x = y[['Y']].copy()
    x.rename(columns = {'Y':'lagP'}, inplace=True)
    x['lagP'] = x['lagP'].shift(h)
    
    i = 0
    while i < (p-1):
        name = 'lagP' + str(1+i)
        x[name] = x['lagP'].shift(1+i)
        i += 1
        
    x.insert(loc=0, column='const',value=1)
    x.set_index(ind, inplace = True)
    
    # Prepping for OLS - break off as separate function
    lags = h + p -1
    y = y[lags:]
    x = x[lags:]
#    n = y.shape[0]
    
    #OlS - break off as separate function
    xT = x.T
    inv = pd.DataFrame(np.linalg.pinv(xT@x))
    xTy = xT@(np.asarray(y))
    betas = np.dot(inv, xTy)
    pred = x@betas
    ind2 = pred.index
    pred.rename(columns = {0:'Y'}, inplace=True)
    y.set_index(ind2, inplace = True)
    cycle = y.subtract(pred)
    cycle.rename(columns = {'Y': nm}, inplace=True)
    
    return pred, cycle
