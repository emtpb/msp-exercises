% create signal (gausspulse) and its spectrum; then plot the spectrum of the zeropadded signal

clear all
close all
clc

%% PART 1
sampl_freq = 50e6;      % sampling frequency

% signal generation (gausspulse)
f_center = 1e6;         % center frequency
bandwidth = 0.6;        % relative bandwidth
tc = gauspuls('cutoff', f_center, bandwidth, [], -40);
t_center = -tc : 1/sampl_freq : tc;
y = gauspuls(t_center, f_center, bandwidth);
t = (0:length(y)-1)./sampl_freq;

% plot signal
plot(t*1e6, y)
xlabel('Time {\itt} / µs')
title(['Time domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y))])

% TODO: define frequency vector and plot absolute value of fft

% zeropadding
number_zeros = 1000;
y_padded = [y, zeros(1, number_zeros)];
t_padded = (0:length(y_padded)-1)./sampl_freq;
figure
plot(t_padded*1e6, y_padded)
xlabel('Time {\itt} / µs')
title(['Time domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_padded))])

% TODO: define frequency vector and plot absolute value of fft

%% PART 2
% add signal with higher frequencies
c = 23;
disp(['Zusaätzliche Mittenfrequenz: ', num2str(f_center*c/1e6), ' MHz'])

y_high_freq = gauspuls(t_center, f_center*c, bandwidth/c);
y_add =y + y_high_freq;
figure
plot(t, y)
hold on
plot(t, y_high_freq, 'r')
hold on
plot(t, y_add, 'g')
xlabel('Time {\itt} / µs')
title(['Time domain. f_{sampl} = ', num2str(sampl_freq/1e6), ' MHz; N = ', num2str(length(y_add))])
legend('lower freq.', 'high freq.', 'sum')

% TODO: plot absolute value of fft

y_add_padded = [y_add, zeros(1, number_zeros)];

% TODO: plot absolute value of fft






