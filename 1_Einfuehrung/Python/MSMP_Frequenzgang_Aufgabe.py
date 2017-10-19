'''
Frequenzgangdarstellung
Der Frequenzgang einer RCL-Schaltung soll grafisch dargestellt werden. Aufgrund des großen Kreisfrequenzbereichs
erfolgt die Darstellung logarithmisch.

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
'''

import numpy as np
import matplotlib.pyplot as plt

# Variablendefinition
R = 1
L = 1e-3
C = 1e-6
omega = np.logspace(3, 6, 500)


# Grafische Ausgabe
plt.figure(1)

plt.show()
