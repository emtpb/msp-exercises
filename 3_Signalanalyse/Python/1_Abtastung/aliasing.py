import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as sio

# read an audio file and plot its spectrum
# downsample the signal (i.e. lower the sampling frequency) and compare the spectra and the new audio signal

# read wav file
[sampl_freq, y] = sio.read('r2d2whereareyou.wav')

n = np.size(y)
t = np.linspace(0, n/sampl_freq, n)

plt.figure()
plt.plot(t, y)
plt.xlabel('Time $t$ / s')
plt.title('original signal')

# TODO: create frequency array and plot spectrum of y

# downsample signal
downsampl_fact = 2               # downsampling factor
sampl_freq_new = sampl_freq/downsampl_fact    # new sampling frequency
y_downsample = y[0::downsampl_fact]
n_new = np.size(y_downsample)
t = np.linspace(0, n_new/sampl_freq_new, n_new)

# TODO: plot downsampled signal and its spectrum

# write downsampled signal to .wav
sio.write('downsample.wav', int(sampl_freq_new), y_downsample)
plt.show()
