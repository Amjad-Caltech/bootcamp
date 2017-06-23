def coeff_of_var(data):
    """computes the coefficient of variation of a data set.
    This is the standard deviation divided by the absolute value of the mean"""
    import numpy as np

    return np.std(data)/np.abs(np.mean(data))
