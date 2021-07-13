"""
Wind Statistics
----------------

Topics: Using array methods over different axes, fancy indexing.

1. The data in 'wind.data' has the following format::

        61  1  1 15.04 14.96 13.17  9.29 13.96  9.87 13.67 10.25 10.83 12.58 18.50 15.04
        61  1  2 14.71 16.88 10.83  6.50 12.62  7.67 11.50 10.04  9.79  9.67 17.54 13.83
        61  1  3 18.50 16.88 12.33 10.13 11.17  6.17 11.25  8.04  8.50  7.67 12.75 12.71

   The first three columns are year, month and day.  The
   remaining 12 columns are average windspeeds in knots at 12
   locations in Ireland on that day.

   Use the 'loadtxt' function from numpy to read the data into
   an array.
"""

# +
from numpy import loadtxt

data = loadtxt("wind.data")
data.shape

dates = data[:, :3]
winds = data[:, 3:]
# -

data[:4,:]

# set_printoptions enable you to adjust the __repor__ of np.arrays
# default threshold of 1000
np.set_printoptions(threshold=50)

data

"""
Big data is data you can't fit in your screen and your head - Alex Chabot-Leclerk

2. Calculate the min, max and mean windspeeds and standard deviation of the
   windspeeds over all the locations and all the times (a single set of numbers
   for the entire dataset).
"""

# +
all_max = data[:, 3:].max()
all_min = data[:, 3:].min()
all_mean = data[:, 3:].mean()
all_std = data[:, 3:].std()

all_min, all_max, all_mean, all_std
# -

"""
3. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds at each location over all the days (a different set of numbers
   for each location)
"""

# +
loc_max = data[:, 3:].max(axis=0)
loc_min = data[:, 3:].min(axis=0)
loc_mean = data[:, 3:].mean(axis=0)
loc_std = data[:, 3:].std(axis=0)

loc_min, loc_max, loc_mean, loc_std
# -

"""
4. Calculate the min, max and mean windspeed and standard deviations of the
   windspeeds across all the locations at each day (a different set of numbers
   for each day)
"""

# +
day_min = data[:, 3:].min(axis=1)
day_max = data[:, 3:].max(axis=1)
day_mean = data[:, 3:].mean(axis=1)
day_std = data[:, 3:].std(axis=1)

day_min, day_max, day_mean, day_std
# -

"""
5. Find the location which has the greatest windspeed on each day (an integer
   column number for each day).
"""

import numpy as np
np.unravel_index(data[:, 3:].argmax(axis=1), data[:, 3:].shape)[1] + 3 # index relation to index

"""
6. Find the year, month and day on which the greatest windspeed was recorded.
"""

np.where(data==all_max)
data[2161, 14]
data[2161, [0, 1, 2]] # 2/12/1966

np.unravel_index(data[:, 3:].argmax(), data[:, 3:].shape)

# find max value in for each day in each location, then find max along day. 
# Row number nicely corresponds to max value in data.
data[:, 3:].max(axis=1).argmax()

"""
7. Find the average windspeed in January for each location.
"""

jan_data = data[data[:,1]==1]
jan_data

jan_data[:, 3:].mean(axis=0)

"""
You should be able to perform all of these operations without using a for
loop or other looping construct.

Bonus
~~~~~

1. Calculate the mean windspeed for each month in the dataset.  Treat
   January 1961 and January 1962 as *different* months. (hint: first find a
   way to create an identifier unique for each month. The second step might
   require a for loop.)



"""
2. Calculate the min, max and mean windspeeds and standard deviations of the
   windspeeds across all locations for each week (assume that the first week
   starts on January 1 1961) for the first 52 weeks. This can be done without
   any for loop.

Bonus Bonus
~~~~~~~~~~~

Calculate the mean windspeed for each month without using a for loop.
(Hint: look at `searchsorted` and `add.reduceat`.)

Notes
~~~~~

These data were analyzed in detail in the following article:

   Haslett, J. and Raftery, A. E. (1989). Space-time Modelling with
   Long-memory Dependence: Assessing Ireland's Wind Power Resource
   (with Discussion). Applied Statistics 38, 1-50.


See :ref:`wind-statistics-solution`.
"""
