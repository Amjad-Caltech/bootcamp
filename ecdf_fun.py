def ecdf(data):
    import numpy as np

    x = np.sort(data)
    y = np.arange(1,len(data)+1)/len(data)

    return x, y
