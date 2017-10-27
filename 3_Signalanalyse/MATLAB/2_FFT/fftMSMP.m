function [coeff] = fftMSMP(signal)
%fftMSMP calculates the DFT using the FFT algorithm
% IN: sig: signal from which the DFT is calculated
% OUT: dft: DFT of sig

signal = signal(:); % make sure signal is a collum vector
N = length(signal);

if N == 1   % base case
    % TODO: write fft algorithm accoring to pseudo code
else % recursive calculation
    % TODO: write fft algorithm accoring to pseudo code
end
end

