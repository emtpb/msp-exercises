import numpy as np
import scipy.signal as signal


def phase_compensation(t, u, f_sig):
    """Deliberately uncommented - find your own solution!"""
    u_sim_raw = np.sin(2*np.pi*f_sig*t)
    Phi = signal.correlate(u/np.max(u), u_sim_raw)
    lags = np.arange(-np.floor(Phi.shape[0]/2), np.ceil(Phi.shape[0]/2))
    Phi_max = np.argmax(Phi[np.logical_and(lags >= -25, lags <= 25)])
    delta_t = (Phi_max-25)*np.mean(np.diff(t))
    return delta_t * (2*np.pi*f_sig)
