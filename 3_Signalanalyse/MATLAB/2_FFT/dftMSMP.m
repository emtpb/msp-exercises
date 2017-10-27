function [dft] = dftMSMP(sig)
%dftMSMP calculates the DFT directly without exploiting any symmetries
% IN: sig: signal from which the DFT is calculated
% OUT: dft: DFT of sig

sig = sig(:);
N = length(sig);

dft = zeros(N, 1);  % initialization
n = 0:N-1;

for k = 0:N-1
    exponential = exp(-i*2*pi/N*k.*n');
    dft(k+1) = sum(sig.*exponential);   % calculate dft for each k
end

end

