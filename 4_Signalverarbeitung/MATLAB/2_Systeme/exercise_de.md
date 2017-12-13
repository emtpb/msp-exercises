Zeitdiskrete Systeme
====================

Aufgabe 1: Modellierung zeitdiskreter Systeme
---------------------------------------------

1. Erzeuge ein Rechtecksignal `u_test_in` mit den folgenden Parametern:
  * Abtastfrequenz `f_s` = 1 MHz
  * `N = 2048` Abtastwerte
  * Grundfrequenz `f_base` = 2 kHz
  * Amplitude `u_hat` = 1 V
2. Schreibe eine Funktion `sys(b, a, data_in)`, die für eine Eingangsfolge `data_in` die Ausgangsfolge `data_out` eines zeitdiskreten Systems, das durch die Koeffizientenvektoren `b` und `a` charakterisiert ist, berechnet.
3. Wende `sys()` auf das Testsignal an. Setze dabei `b = np.array([0.1367, 0.1367])` und `a = np.array([1, -0.7265])`.
4. Was kannst Du über die Systemeigenschaften aussagen?
5. Wiederhole mit `b = np.array([0.8633, -0.8633])` und `a = np.array([1, -0.7265])`.  
Was ändert sich? Was kannst du hier über die Systemeigenschaften aussagen?


Aufgabe 2: Systemanalyse im Zeit- und Frequenzbereich
-----------------------------------------------------

Nutze weiterhin die Systeme aus Aufgabe 1.

1. Bestimme den Frequenzgang ODER die Impulsantwort beider Systeme.
2. Visualisiere die ermittelte Funktion.  
Hinweis: Frequenzgang als Bode-Diagramm visualisieren, Skalierungen beachten!
3. Bestimme und visualisiere die andere Funktion (Impulsantwort oder Frequenzgang).
4. Begründe deine Aussagen aus Aufgabe 1.4 und 1.5 anhand der Grafiken.
5. Kannst du anhand der Grafiken weitere Aussagen über die Systeme treffen?
