import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from convert_to_timeseries import convert_data_to_timeseries

# Input file containing data
input_file = 'data_timeseries.txt'

# Load data
data1 = convert_data_to_timeseries(input_file, 2)    
data2 = convert_data_to_timeseries(input_file, 3)
dataframe = pd.DataFrame({'first': data1, 'second': data2})

# Print max and min
print('\nMaximum:\n', dataframe.max())     #### maximum floating stock datavalues of column1  and column2 
print('\nMinimum:\n', dataframe.min())

# Print mean
print('\nMean:\n', dataframe.mean())
print('\nMean row-wise:\n', dataframe.mean(1)[:10])  #### ie  (floating value1 + Floating value2

# Plot rolling mean
dataframe.rolling(window=24).mean().plot()

'''
# Print correlation coefficients
print('\nCorrelation coefficients:\n', dataframe.corr())

# Plot rolling correlation
plt.figure()
pd.rolling_corr(dataframe['first'], dataframe['second'], window=60).plot()
'''
plt.show()

