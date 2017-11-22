import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sio
import scipy.signal as sig

# read and normalize signal
sampl_freq, y = sio.read('hello.wav')
y = y/max(y)

# plot signal
t = np.arange(0, len(y))/sampl_freq
plt.figure()
plt.plot(t, y)
plt.xlabel('Zeit $t$ / s')

# calculate spectrogram
# TODO: f, t, spec = sig.spectrogram(...)

# logarithmic scaling and remove inf
spec_log = np.log(spec)
idx_inf = np.isinf(spec_log)
spec_log[idx_inf] = 0

# TODO:plot spectrogram
