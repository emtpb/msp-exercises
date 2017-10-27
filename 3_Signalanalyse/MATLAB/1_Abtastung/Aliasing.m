% read an audio file and plot its spectrum
% downsample the signal (i.e. lower the sampling frequency) and compare the spectra and the new audio signal

clear all
close all
clc

%% load signal and plot
% read file
[y, sampl_freq] = audioread('r2d2whereareyou.wav');

n = length(y);                   % signal length
delta_t = 1/sampl_freq;
t = 0:delta_t:(n-1)/sampl_freq;  % time vector

% plot signal
figure
plot(t, y)
xlabel('Time {\itt} / s')
ylabel('Original signal')

% play signal
sound(y, sampl_freq)

% spectrum
% TODO: create frequency vector and plot spectrum of y

%% downsample
p = 2;      % downsampling factor
sampl_freq_downsample = sampl_freq/p;   % new downsampling frequency
y_downsample = downsample(y, p);
n_downsample = length(y_downsample);
t = 0:1/sampl_freq_downsample:(n_downsample-1)/sampl_freq_downsample;

% TODO: plot downsampled signal and its spectrum

sound(y_downsample, sampl_freq_downsample)
% audiowrite('downsample.wav', y_downsample, sampl_freq_downsample);
