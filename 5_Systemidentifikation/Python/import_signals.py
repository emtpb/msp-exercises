import scipy.io as io
import numpy as np
import matplotlib.pyplot as pp

mat_data = io.loadmat('../signals/doepfer_freq_mod.mat')
output_signal = np.squeeze(mat_data['output_signal'])
input_signal = np.squeeze(mat_data['input_signal'])
time = np.squeeze(mat_data['time'])

pp.figure()
pp.plot(time, input_signal, label='Input signal')
pp.plot(time, output_signal, label='Output signal')
pp.grid(True)
pp.xlabel('Time $t$ / s')
pp.xlabel('Voltage $U$ / V')
pp.show()
