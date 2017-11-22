import numpy as np


def wavelet_transform(signal_in, sampl_freq, scales, wave_type):
    """calculate the wavelet transform of signal_in

    Args:
        signal_in (array_like): signal from that the cwt should be calculated
        sampl_freq (float): sampling frequency of signal_in
        scales (array_like): values by which the mother wavelet should be scaled
        wave_type(function): wavelet in frequency domain in form of a function that takes the input of a
        frequency vector
    Returns:
        cwt(array_like): wavelet transform of signal_in
    """

    signal_length = np.size(signal_in)

    # calculate cwt as a dot product of signal_in and a scaled version of the wavelet in frequency domain
    signal_fft = np.fft.fftshift(np.fft.fft(signal_in))
    f = np.arange(-sampl_freq/2, sampl_freq/2, sampl_freq/signal_length)

    f.shape = (1, len(f))
    scales.shape = (len(scales), 1)
    scaled_freq = np.dot(scales, f)
    wavelet = wave_type(scaled_freq)*np.sqrt(np.tile(scales, (1, signal_length)))    # ndarray of scaled matrices

    cwt = np.fft.ifft(wavelet*np.tile(signal_fft, (np.size(scales), 1)), axis=1)
    return cwt
