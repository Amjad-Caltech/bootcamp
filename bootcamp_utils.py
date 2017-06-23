"""Potentially useful functions and codes from the bootcamp."""

import numpy as np
import matplotlib.pyplot as plt

# This function calculates 'x' and 'y' for an ECDF plot
def ecdf(data):
    import numpy as np

    x = np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)

    return x, y

def bs_replicate(data, func=np.mean):
    """Computes a bootsrap replicate of the 'data'"""
    bs_sample = np.random.choice(data, replace=True, size=len(data))
    return func(bs_sample)

def draw_bs_reps(data, func=np.mean, size=10000):
    "draw bootstrap replicates from data"
    return np.array([bs_replicate(data, func=func) for _ in range(size)])
