Preprocessing real measurement data
===================================

Consider the real measurement data in `preprocessing_data.mat`.
It contains, among others, an approximately sinusoidal signal component.


Task
----
Programmatically(!) extract the parameters of the sinusoidal signal component.


Strategy hints
--------------
1. Apply signal conditioning to retrieve a "pure" sinus signal.  
Note: A suitable part of the signal may be selected by "looking closely".
2. Determine the sinus signal's amplitude.
3. Determine the sinus signal's frequency, `f_sig`.
4. Simulate an ideal sinus signal with the previously found parameters.  
Note: For determining the phase, use `phase_compensation(t, u, f_sig)` for now.
5. Visualize the measured and simulated signals.
6. Bonus task: Develop your own solution for determining the phase.
