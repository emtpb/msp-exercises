import numpy as np


def findpeaks(data):
    """
    find local maxima of data

    Args:
        data (array_like): sampled function from which the local max are \
        calculated
    Returns:
        loc (array_like): indices of maxima
        peaks (array_like): function values at peaks
    """

    abscissa = np.arange(0, len(data))
    derivative_first = np.gradient(data)

    x_less = abs(np.diff(np.sign(derivative_first))) == 2
    x_bool = np.concatenate([x_less, np.array([False], dtype=bool)])
    y = (np.concatenate([np.array([False, False], dtype=bool),
                         x_less[0:len(x_less)-1]]))
    y_bool = (data[x_bool] > data[y])

    locs = abscissa[x_bool][y_bool]
    peaks = data[x_bool][y_bool]

    return locs, peaks
