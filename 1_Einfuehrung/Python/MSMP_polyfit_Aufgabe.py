"""
Probleme bei polyfit
Es werden Messdaten des Materialfeuchtemesssystems NIROMM (EMT)
verwendet. Quarzsand unterschiedlicher Materialfeuchten psi wird mit
Infrarotimpulsen unterschiedlicher Strahlungswellenlängen bestrahlt und
die reflektierte Strahlung gemessen. Bei höheren Feuchten wird mehr
Strahlung durch die Wassermoleküle absorbiert und demnach weniger
reflektiert. Der Zusammenhang zwischen den Messspannungen und der
Materialfeuchte soll durch Polynome geeigneten Grades beschrieben werden.
Problem ist die geeignete Wahl des Polynomgrades.

* Materialfeuchten psi von 0 bis 7 %MF (psi, [0 0.3 0.4 0.5
0.6 0.7 0.8 0.9 1.0 1.1 1.2 2.0 3.0 4.0 5.0 7.0], 16 Stützstellen)
* Für diese Übung wird nur Messkanal 1 (u1) betrachtet.

Messtechnische Signalanalyse mit MATLAB und Python, Vorlesung/Übung

(c) Elektrische Messtechnik, Universität Paderborn - http://emt.upb.de
"""

import numpy as np
import matplotlib.pyplot as pp
import scipy.io

# Variablen laden und definieren
mat = scipy.io.loadmat('MSMP_polyfit_messdaten')
psi = mat['psi'][0]
u1 = mat['u1'][0]

p_grad = 8


# Grafische Ausgabe
pp.figure()
pp.plot(psi, u1, '.', markersize=12)
pp.grid(True)
pp.xlim([-0.1, 7.1])
pp.ylim([1.5, 3])
pp.xlabel('Materialfeuchtigkeit $\psi$')
pp.ylabel('Spannung $u_1 / \mathrm{V}$')
pp.legend(['Messwerte'])

pp.show()
