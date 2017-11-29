import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np
from wvd import wvd

# parameter
sampl_freq = 100
N = 1024
t = np.arange(0, N)/sampl_freq

# create signal
f_1 = 1
f_2 = 5

# TODO: create signal

# plot signal
# TODO: plot signal

# Wigner-Ville-Distribution
wv, ff, tt = wvd(y, 1, N/2, sampl_freq)

# TODO: plot its absolute value using pcolormesh
