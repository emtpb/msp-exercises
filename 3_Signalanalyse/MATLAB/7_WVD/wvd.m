function [wv, ff, tt] = wvd(signalIn, resolution, winSize, smplFrequ)
% WVD creates a Wigner-Ville spectrogram 
%
% Input parameters:
% signalIn: real input time series
% resolution: resolution, number of samples between windows 
% (for full resolution:  1)
% winSize: window size, becomes length of frequency axis
% (a good default: length(signalIn)/2)
% smplFrequ: samples per second of signal
%
% Output parameters:
% wv: the W-V spectrum, each row represents a frequency, each column a 
% time instant
% ff: frequency vector (optional)
% tt: time vector (optional)
% 	
% Display using: 
%
% imagesc(tt,ff,wv);
% axis xy
% 	
% or:		
%
% surf(tt,ff,wv);
% shading interp
%
% Case Bradford, February 2005, http://case.caltech.edu/tfr/)
% Adapted from Rene Laterveer, 1999

if size(signalIn,1) ~= 1
    signalIn = transpose(signalIn);
end

% make even number of points, at given resolution
npts = floor(floor(length(signalIn) / resolution) / 2) * 2;

% make sure that we entered in an integer for the window
winSize = floor(winSize);

% round window length down to nearest odd integer
oddwin = (floor((winSize - 1) / 2) * 2) + 1;

% half point (for indexing reasons we need it later, we're
% filling two columns per loop, so we only index through half)
halfwin = (oddwin + 1) / 2 - 1;

% create tt and ff
tt = (0:npts - 1) * resolution / smplFrequ;
ff = (0:winSize - 1) * (smplFrequ / 2) / (winSize - 1);

% pad with zeros
signalIn = [zeros(1, oddwin - 1), signalIn, zeros(1, oddwin - 1)];

% initialize 
wv = zeros(winSize, npts);

r = zeros(1, winSize);
idx = 1:halfwin;

for n = 0 : npts/2 - 1
    
    t = 2 * n * resolution + oddwin;
    r(1) = signalIn(t) * conj(signalIn(t)) + 1i * ...
        signalIn(t + resolution) * conj(signalIn(t + resolution));
    v1 = signalIn(t + idx) .* conj(signalIn(t - idx));
    v2 = signalIn(t + resolution + idx) .* ...
        conj(signalIn(t + resolution - idx));
    r(idx + 1) = v1 + 1i * v2;
    r(winSize - idx + 1) = conj(v1) + 1i * conj(v2);
    
    rf = fft(r, winSize);
    
    wv(:, 2 * n + 1) = real(rf);
    wv(:, 2 * n + 2) = imag(rf);
    
end

end
