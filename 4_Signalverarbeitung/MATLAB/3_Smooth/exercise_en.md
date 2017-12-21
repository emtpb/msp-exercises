Design and application of a smoothing filter
============================================

1. How must the filter coefficients be chosen for a smoothing filter of order `N`?  
Note: It is an FIR filter.
2. Analyze the frequency response of the filter using `N = 2`.
3. Apply the filter to the test signal in `ma_filtering.mat`.
4. Visualize the original and filtered signal.

5. For `N = 2`, the smoothing is insufficient.
Choose a suitable filter order `N`, so that the signal is properly smoothed.  
Note: Decide whether the signal is "smooth enough" by looking at the graph.
6. Which problem becomes visible when using higher filter orders?
7. Filter the original signal again, using your chosen filter order `N`.  
However, use the function `filtfilt()` instead of `lfilter()`. What is different?
8. Comparing the two filtered signals is unfair.
  * Why?
  * What would have to be done to make the comparison fair?
