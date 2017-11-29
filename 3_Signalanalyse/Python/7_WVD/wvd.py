import numpy as np
import math as math


def wvd(signal_in, resolution, win_size, sampl_freq):
    """calculate the Wigner-Ville distribution (WVD) of signal_in

    Args:
        signal_in (array_like): signal from that the cwt should be calculated
        resolution (float): resolution, number of samples between windows (for full resolution:  1)
        winSize (flaot): window size, becomes length of frequency axis (a good default: len(signalIn)/2)
        sampl_frequ (float): samples per second of signal
    Returns:
        cwt(array_like): WVD of signal_in
        ff(array_like): frequency array
        tt(array_like): time array
    """
    number_pts = math.floor(math.floor(len(signal_in)/resolution)/2)*2

    win_size = math.floor(win_size)

    odd_win = (math.floor((win_size-1)/2) * 2)+1

    half_win = (odd_win+1)/2-1

    tt = np.arange(0, number_pts)*resolution/sampl_freq
    ff = np.arange(0, win_size)*(sampl_freq/2)/(win_size-1)

    signal_padded = np.concatenate([np.zeros(odd_win-1), signal_in, np.zeros(odd_win-1)])

    wv = np.zeros((win_size, number_pts))

    r = np.zeros(win_size, dtype=complex)
    idx = np.arange(1, half_win + 1, dtype=int)

    for n in range(0,  int(number_pts/2)):

        t = 2 * n * resolution + odd_win -1
        r[0] = signal_padded[t] * np.conj(signal_padded[t])+1j*signal_padded[t+resolution] * \
            np.conj(signal_padded[t+resolution])
        v1 = signal_padded[t+idx]*np.conj(signal_padded[t-idx])
        v2 = signal_padded[t+resolution + idx]*np.conj(signal_padded[t+resolution-idx])
        r[idx] = v1+1j*v2
        r[win_size-idx] = np.conj(v1)+1j*np.conj(v2)

        r_fft = np.fft.fft(r, win_size)

        wv[:, 2*n] = np.real(r_fft)
        wv[:, 2*n+1] = np.imag(r_fft)

    return wv, ff, tt
