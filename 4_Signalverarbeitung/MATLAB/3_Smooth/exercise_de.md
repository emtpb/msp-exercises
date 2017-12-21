Design und Anwendung eines Mittelwert-Filters
=============================================

1. Wie müssen die Filterkoeffizienten für ein Mittelwertfilter der Ordnung `N` gewählt werden?  
Hinweis: Es handelt sich um ein FIR-Filter.
2. Analysiere den Frequenzgang des Filters für `N = 2`.
3. Wende das Filter auf das Testsignal aus `ma_filtering.mat` an.
4. Visualisiere das Originalsignal und das gefilterte Signal.

5. Für `N = 2` wird das Signal noch nicht ausreichend stark geglättet.
Wähle eine geeignete Filterordnung `N`, um das Signal hinreichend zu glätten.  
Hinweis: Beurteile "durch Hinsehen", wann das Signal glatt ist.
6. Welches Problem wird bei der Wahl einer höheren Filterordnung sichtbar?
7. Filtere das Originalsignal erneut mit der gewählten Filterordnung `N`.  
Verwende dafür jedoch die Funktion `filtfilt()` statt `lfilter()`. Was ist anders?
8. Der Vergleich der beiden gefilterten Signale ist nicht fair.
  * Warum?
  * Was müsste getan werden, um den Vergleich fair zu machen?
