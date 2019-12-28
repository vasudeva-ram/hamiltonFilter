# hamiltonFilter
Implements Hamilton(2016) alternate to the HP filter.

Hamilton's original paper, "Why You Should Never Use the Hodrick-Prescott Filter", can be found [here](https://econweb.ucsd.edu/~jhamilto/hp.pdf). In general, Hamilton's argument is that the "cycle" can be best understood as the deviation of a time series' value from one's prediction of it. Specifically, given the last p values of the time series, what is one's h-period ahead forecast? And how did the actual data deviate from this prediction? 

This filter assumes a linear projection using OLS, as Hamilton suggests (richer models involving nonlinearities are shown to be unnecessary). 

## Parameters: 
array:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pandas Series  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The time series to apply the filter to

p:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Number of most recent lags of data of the time series. Default, as suggested by Hamilton, is 4
        
h:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; int  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Number of periods-ahead forecast to determine the "trend"

## Returns:
pred:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pandas Dataframe  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The series of h-period ahead linear forecasts of the time series, based on p periods of data
        
cycle:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pandas Dataframe  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The deviations of the actual data from the predicted time series
