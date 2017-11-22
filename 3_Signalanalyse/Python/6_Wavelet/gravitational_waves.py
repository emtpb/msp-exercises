import numpy as np
import matplotlib.pyplot as plt
from wavelet_transform import wavelet_transform

# load data
lines = np.loadtxt("H1.txt", comments="#")
t = lines[:, 0]
y = lines[:, 1]
sampl_freq = 1/(t[1]-t[0])

plt.figure()
plt.plot(t, y)
plt.xlabel('Time $t$ / s')
plt.ylabel('Strain $\epsilon\cdot 1e-21$')

# TODO: define wavelet parameters
f_c = ..
f_b = ...
scales = np.linspace(1/10, 10, num=1000)

def wavelet_fun(f):
    # define wavelet function (complex morlet)
    return np.exp(-f_b ** 2 * np.pi ** 2 * (f - f_c) ** 2)

# compute wavelet transform
wt = wavelet_transform(y, sampl_freq, scales, wavelet_fun)

plt.figure()
plt.pcolormesh(t, f_c/scales, abs(wt))
plt.xlabel('Time $t$ / s')
plt.ylabel('Frequency $f$ / Hz')

plt.show()
