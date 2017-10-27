% calculate the dft via different algorithms

clear all
close all
clc

%% calculated DFT using different algorithms
% define parameters
f_0 = 1;                        % signal frequency
N = 2048;                       % number of samples (power of 2)
number_periodes = 1;            % sampled periodes
sampl_freq = N/number_periodes; % sampling frequency

n = 0:N-1;                      % discrete time vector

% generate and plot y
y = cos(2*pi*f_0.*n/sampl_freq);% signal

figure
stem(n, y, 'LineWidth', 2)
xlabel('Index {\itn}')

% calculate dfts using different algorithms
% dft_msmp
tic
dft = dftMSMP(y);
dft_time = toc;
% fft_msmp
tic
ft = fftMSMP(y);
ft_time = toc;

% plot results from different algorithms
figure
hold all
stem(abs(dft), 'LineWidth', 2)
stem(abs(ft), 'LineWidth', 2)
legend('DFT MSMP', 'FFT MSMP')
xlabel('Index {\itk}')

disp(['Time for DFT: ', num2str(dft_time), 's'])
disp(['Time for FFT: ', num2str(ft_time), 's'])

%% OPTIONAL:
% TODO: plot the computation time as a function of the length of y using
% different algorithms



    