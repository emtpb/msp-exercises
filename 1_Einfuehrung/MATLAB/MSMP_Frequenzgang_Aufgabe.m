%% Frequenzgangdarstellung
% Der Frequenzgang einer RCL-Schaltung soll grafisch dargestellt werden.
% Aufgrund des groﬂen Kreisfrequenzbereichs erfolgt die Darstellung
% logarithmisch.
% 
% Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/‹bung
% 
% (c) Elektrische Messtechnik, Universit‰t Paderborn - http://emt.upb.de

%% Version
%   Dateiname: MSMP_Frequenzgang_Aufgabe.m

%% Initialisierung
close all; clear all; clc;

%% Variablendefinition
R = 1;    L = 1e-3;    C = 1e-6;  
omega = logspace(3, 6, 500); 


%% Grafische Ausgabe
