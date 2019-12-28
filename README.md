# hamiltonFilter
Implements Hamilton(2016) alternate to the HP filter.

Hamilton's original paper, "Why You Should Never Use the Hodrick-Prescott Filter", can be found here: https://econweb.ucsd.edu/~jhamilto/hp.pdf. In general, Hamilton's argument is that the "cycle" can be best understood as the deviation of a time series' value from one's prediction of it. Specifically, given the last p values of the time series, what is one's h-period ahead forecast? And how did the actual data deviate from this prediction? 
\\
This filter assumes a linear projection using OLS, as Hamilton suggests (richer models involving nonlinearities are shown to be unnecessary). 

Parameters: 
array:  Pandas Series
        The time series to apply the filter to

p:      int
        Number of most recent lags of data of the time series. Default, as suggested by Hamilton, is 4
        
h:      int
        Number of periods-ahead forecast to determine the "trend"
        
Returns:
pred:   Pandas Dataframe
        The series of h-period ahead linear forecasts of the time series, based on p periods of data
        
cycle:  Pandas Dataframe
        The deviations of the actual data from the predicted time series
