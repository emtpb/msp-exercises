function phi = phase_compensation(t, u, f_sig)
% Deliberatly uncommented - find your own solution!
    u_sim_raw = sin(2*pi*f_sig*t);
    [Phi, lags] = xcorr(u./max(u), u_sim_raw);
    [~, Phi_max] = max(Phi(lags>=-25 & lags<=25));
    delta_t = (Phi_max-25)*mean(diff(t));
    phi = delta_t * (2*pi*f_sig);
end
