% calculate wvd of sine signals

clear all
close all
clc

% parameters
sampl_freq = 100;       % sampling frequency
N = 1024;               %  number of samples
t = (0:N-1)/sampl_freq; % time vector

% create signal
f_1 = 1;
f_2 = 5;

% TODO:create signal y

% TODO: plot signal

% Wigner-Ville-Distribution
[wv, f, t] = wvd(y, 1, N/2, sampl_freq);

% TODO: plot absolute value of wvd using pcolor
