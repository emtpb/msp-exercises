Vorverarbeitung eines realen Messsignals
========================================

Betrachte das reale Messsignal aus `preprocessing_data.mat`.
Darin enthalten ist u.a. ein näherungsweise sinusförmiger Signalanteil.


Aufgabe
-------
Extrahiere programmatisch(!) die Parameter des sinusförmigen Signalanteils!


Tipps zur Vorgehensweise
------------------------
1. Konditioniere das Messsignal so, dass ein möglichst "reines" Sinussignal vorliegt.  
Hinweis: Ein sinnvoller Signalausschnitt darf "durch Hinsehen" ausgewählt werden.
2. Bestimme die Amplitude des Sinussignals.
3. Bestimme die Frequenz des Sinussignals, `f_sig`.
4. Simuliere ein ideales Sinussignal mit den zuvor gefundenen Parametern.  
Hinweis: Nutze zur Bestimmung der Phasenlage zunächst `phase_compensation(t, u, f_sig)`.
5. Visualisiere das Messsignal und das simulierte Signal.
6. Bonusaufgabe: Entwickle eine eigene Lösung zur Bestimmung der Phasenlage.
