'''
Vergleich verschiedener Methoden zur numerischen Integration

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''
import numpy as np
import scipy.integrate as sci

x_min, x_max = 0, 1

# ...
area_sum = 0
area_trapz = 0
area_int = 0

# sum
print('Sum: ' + str(area_sum))

# trapz
print('Trapz: ' + str(area_trapz))

# Numerische Integration
y_f = lambda x: x**2
print('Numerische Integration: ' + str(area_int))
