% calculate STFT of different signals
clear all
close all
clc

% read signal
[y, sampl_freq] = audioread('head.wav');

% plot signal
t = (0:length(y)-1)/sampl_freq;
figure
plot(t, y)
xlabel('Zeit {\itt} / s')

% calculate spectrogram
% TODO: [spec, f, t] = spectrogram(...);

% TODO:plot logarithmic spectrogram
