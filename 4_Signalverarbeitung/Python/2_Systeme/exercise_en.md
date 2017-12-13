Discrete-time systems
=====================

Exercise 1: Modelling of discrete-time systems
----------------------------------------------

1. Generate a rectangular signal `u_test_in` with the parameters:
  * Sampling frequency `f_s` = 1 MHz
  * `N = 2048` samples
  * Base frequency `f_base` = 2 kHz
  * Amplitude `u_hat` = 1 V
2. Write a function `sys(b, a, data_in)` that, for an input progression `data_in`, computes the output progression `data_out` of a discrete-time system that is characterized by the coefficient vectors `b` and `a`.
3. Apply `sys()` to the test signal. Use `b = np.array([0.1367, 0.1367])` and `a = np.array([1, -0.7265])`.
4. What can you state about the system's properties?
5. Repeat with `b = np.array([0.8633, -0.8633])` and `a = np.array([1, -0.7265])`.  
What is different? What can you state about this system's properties?


Exercise 2: System analysis in time and frequency domain
--------------------------------------------------------

Continue using the systems from exercise 1.

1. Determine the frequency response OR the impulse response of both systems.
2. Visualize the function.  
Note: Visualize the frequency response as a Bode diagram, observe axis scaling!
3. Determine and visualize the other function (impulse response or frequency response).
4. Substantiate your statements from exercise 1.4 and 1.5 based on the graphs.
5. Can you make additional statements about the two systems?
