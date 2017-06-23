def ecdf(data, formal=False, buff=0.1, min_x=None, max_x=None):
    """
    Generate `x` and `y` values for plotting an ECDF.

    Parameters
    ----------
    data : array_like
        Array of data to be plotted as an ECDF.
    formal : bool, default False
        If True, generate `x` and `y` values for formal ECDF.
        Otherwise, generate `x` and `y` values for "dot" style ECDF.
    buff : float, default 0.1
        How long the tails at y = 0 and y = 1 should extend as a
        fraction of the total range of the data. Ignored if
        `formal` is False.
    min_x : float, default None
        Minimum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.
    max_x : float, default None
        Maximum value of `x` to include on plot. Overrides `buff`.
        Ignored if `formal` is False.

    Returns
    -------
    x : array
        `x` values for plotting
    y : array
        `y` values for plotting
    """

    import numpy as np

    if formal == False:
        x = np.sort(data)
        y = np.arange(1,len(data)+1)/len(data)
        return x, y

    else:
#calculate the actual x and y based on the data
        data_x = np.sort(data)
        data_y = np.arange(1,len(data)+1)/len(data)

#determine the range of x to be plotted based on the inputs of the function
        if min_x != None:
            x_start = min_x
        else:
            x_start = data_x[0] - buff*(data_x[-1] - data_x[0])

        if max_x != None:
            x_end = min_x
        else:
            x_end = data_x[-1] + buff*(data_x[-1] - data_x[0])

        # x = np.zeros(2*len(data_x[>= x_start and =< x_end]))
        # y = np.zeros(2*len(data_x[>= x_start and =< x_end]))
        #
        # for i in range(2*len(data_x[>= x_start and =< x_end])):
        #     if x[i] < data_x[0]:
        #         y[i] = 0
        #     else:
        #         for j in range(len(data_x)):
        #             if x[i] >= data_x[j]:
        #                 y[i] = data_y[j]


        x = np.linspace(x_start, x_end, 400)
        y = np.linspace(x_start, x_end, 400)

        for i in range(len(x)):
            if x[i] < data_x[0]:
                y[i] = 0
            else:
                for j in range(len(data_x)):
                    if x[i] >= data_x[j]:
                        y[i] = data_y[j]

        return x, y
