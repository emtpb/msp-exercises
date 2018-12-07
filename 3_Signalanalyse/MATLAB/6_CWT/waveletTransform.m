function[cwt] = waveletTransform(signalIn, samplFreq, scales, waveType)
%WAVELETTRANSFORM calculates the wavelet transform of signalIn
% IN:
% signalIn:   signal from that the cwt should be calculated
% samplFreq:  sampling frequency of signalIn
% scales:     values by which the mother wavelet should be scaled
% waveType:   wavelet in frequency domain in form of a function 
%             handle that takes the input of a frequency vector
% OUT:
% cwt:    wavelet transform of signalIn

            
signalIn = signalIn(:)';
scales = scales(:);
signalLen = size(signalIn, 2);

% compute cwt as a dot product of signalIn and scaled versions of
% the wavelet in frequency domain
signalFft = fftshift(fft((signalIn)));
f = (-samplFreq/2 : samplFreq/signalLen : samplFreq/2-samplFreq/signalLen);

% scale the wavelet according to 'scales'
scaledFreq = (scales*f);
wavelet = waveType(scaledFreq).*sqrt((repmat(scales, 1, signalLen)));

cwt = ifft(wavelet.* repmat((signalFft), size(scales, 1), 1), [], 2);

end