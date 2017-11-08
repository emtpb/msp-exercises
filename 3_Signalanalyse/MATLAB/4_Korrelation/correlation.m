% calculate the longitudinal and transversal speed of sound using analytic
% correlation

clear all
close all
clc

% geometry parameters
l = 16.9e-3;    % waveguide length
D = 6e-3;       % waveguide diameter

load('signals.mat')     % load y_send, y_rec and sampl_freq
t = (0:length(y_rec)-1)./sampl_freq;
figure
plot(t*1e6, y_send, 'LineWidth', 2)
hold on
plot(t*1e6, y_rec, 'r', 'LineWidth', 2)
xlabel('Time {\itt} / µs')
ylim([-1.2, 1.2])
legend('sending signal', 'received signal')

% calculate the envelope(the envelope of a signal y can be calulated by 
% the absolute value of its analytic signal) 
% TODO: calculate y_rec_env and y_send_env and plot these in the figure
% above

% correlate the envelopes
% TODO: use xcorr to correlate y_send and y_rec, does the order of the two
% signals matter?
[corr_ana, lag] = ...


figure
plot(lag/sampl_freq, corr_ana)
xlabel('Time \tau / s')

% find peaks
[pks,locs] = findpeaks(corr_ana);
% sort peaks in descending order
peaks_sorted = flipud(sortrows([pks, locs]));

% plot largest peaks
hold on
stem(lag(peaks_sorted(1:3, 2))/sampl_freq, correlation_ana(peaks_sorted(1:3, 2)), 'r')

% calculate t_0 and t_1
t_0 = lag(peaks_sorted(1, 2))/sampl_freq;
t_1 = lag(peaks_sorted(2, 2))/sampl_freq;

delta_t = t_1-t_0;

% TODO:calculate longitudinal and transversal wave velocities
