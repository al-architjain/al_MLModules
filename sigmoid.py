"""
Arguments: 
    z - A scalar or numpy array of any size.

Return:
    sig - sigmoid value of the input z array.
"""


import numpy as np

def sigmoid(z):
    sig = (1 / ( 1 + np.exp(-z)))
    return sig
