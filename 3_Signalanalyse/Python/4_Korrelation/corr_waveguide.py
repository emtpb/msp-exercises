import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import scipy.signal as sig
from findpeaks import findpeaks

# geometry parameters
l = 16.9e-3     # waveguide length
D = 6e-3        # waveguide diameter

mat = scipy.io.loadmat('signals.mat', squeeze_me=True)

sampl_freq = mat['sampl_freq']
y_send = mat['y_send']
y_rec = mat['y_rec']

t = np.arange(0, len(y_rec))/sampl_freq

plt.figure()
plt.plot(t*1e6, y_send, label='sending signal')
plt.plot(t*1e6, y_rec, 'r', label='received signal')
plt.xlabel('Time $t$ / s')
plt.ylim(-1.2, 1.2)
plt.legend()

# calculate the envelope(the envelope of a signal y can be calulated by the
# absolute value of its analytic signal)
# TODO: calculate y_rec_env and y_send_env and plot these in the figure
# above

# correlate the envelopes
# TODO: use xcorr to correlate y_send and y_rec, does the order of the two
# signals matter?
corr_ana = sig.correlate(...,  mode='full')
lag = np.arange(-len(y_send_env)+1, len(y_send_env))

plt.figure()
plt.plot(lag/sampl_freq*1e6, corr_ana)
plt.xlabel('Time $\tau$ / s')

locs, peaks = findpeaks(corr_ana)

sort_idx = np.flipud(np.argsort(peaks))
peaks_sort = peaks[sort_idx]
locs_sort = locs[sort_idx]

plt.stem(lag[locs_sort[0:2]]/sampl_freq*1e6, peaks_sort[0:2])

# calculate t_0 and t_1
t_0 = lag[locs_sort[0]]/sampl_freq
t_1 = lag[locs_sort[1]]/sampl_freq

# calculate longitudinal and transversal wave velocities
# TODO:calculate longitudinal and transversal wave velocities
