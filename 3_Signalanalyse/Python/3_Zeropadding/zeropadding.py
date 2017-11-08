from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
plt.close("all")

# PART 1
sampl_freq = 50e6       # sampling frequency

# gaussian modulated sine
f_center = 1e6          # center frequency
bandwidth = 0.6         # relative bandwidth
n = 200               # number of samples
t = np.linspace(0, n/sampl_freq, n)   # time

# without zeropadding
_, y = signal.gausspulse(t-t[-1]/2, fc=f_center, bw=bandwidth, retquad='true')

plt.figure()
plt.plot(t*1e6, y)
plt.xlabel('Time $t$ / µs')
plt.title('signal without zeropadding')

# fouriertransform
# TODO: calculate and plot absolute value of fft

# with zeropadding
number_zeros = 1000         # number of zeros padded
y_padded = np.concatenate((y, np.zeros(number_zeros)))      # padded signal
t_padded = np.linspace(0, np.size(y_padded)-1, np.size(y_padded))/sampl_freq

plt.figure()
plt.plot(t_padded*1e6, y_padded)
plt.xlabel('Time $t$ / µs')
plt.title('signal with zeropadding')

# fouriertransform
# TODO: calculate and plot absolute value of fft_padded

# PART 2
# add higher frequencies
c = 23                  # shift of center frequency
_, y_high_freq = signal.gausspulse(t-t[-1]/2, fc=f_center*c, bw=bandwidth/c, retquad='true')

# add low and high frequency part
y_add = y + y_high_freq
plt.figure()
plt.plot(t*1e6, y, 'b', label='low frequency')
plt.plot(t*1e6, y_high_freq, 'r', label='high frequency')
plt.plot(t*1e6, y_add, 'g', label='sum')
plt.xlabel('Time $t$ / µs')
plt.legend()

# TODO: calculate and plot absolute value of fft

# padded signal
y_add_padded = np.concatenate((y_add, np.zeros(number_zeros)))

# TODO: calculate and plot absolute value of fft

plt.show()
