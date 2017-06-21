"""Potentially useful functions and codes from the bootcamp.""""

import numpy as np
import matplotlib.pyplot as plt

# This function calculates 'x' and 'y' for an ECDF plot
def ecdf(data):
    import numpy as np

    x = np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)

    return x, y
