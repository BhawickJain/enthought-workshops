# -*- coding: utf-8 -*-
# ! pip install numpy

# +
import numpy as np

np.__version__  #1.21.0
# -

a = np.array([11, 2, 3 ,4])
f = np.array([1.2, 2.3, 4.5, 5.6])

a + f
# array([12.2,  4.3,  7.5,  9.6])

a.dtype
# dtype('int64')

f.dtype
# dtype('float64')

g = a + f
g.dtype
# dtype('float64')

# `int64` is upcasted to `float64`

# +
# ufuncs (Universal Functions)

np.sin(a)
# array([-0.99999021,  0.90929743,  0.14112001, -0.7568025 ])

# +
# Elementwise application of the function.
# -

# Array Indexing
# ```
# | 11 | 22 | 34 |
# 0    1    2    3 ... Index
# ```

# +
# Two Dimensinoal Array
# -

a = np.array([[0, 2, 4, 6],[1, 3, 5, 7]])
a.shape

a.size

a.ndim

a

#        -----------> 1 
#     |  [0, 2, 4, 6]
#     v  [1, 3, 5, 7]
#     0

a[0]

# You select row position (or whatever the 0 axis is)

a[:, 1]

# a[ axis=0, axis=1, ... axis=n ] Whatever remains comes out as an array

# ```
#     0
#    /
#   /
#  /
#  ---------------- 2
# |
# |
# |
# |
# 1
# ```

b = np.array([[[1,2,3], [1,2,3], [1,2,3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [7, 8, 9]]])

b.ndim

b.size

b

b[1]

b[:,1]

b[:, :, 1]

a

a[-1,:]

a[:, -1]

# Select Second Last columns

a[:,-2:-1] # Does preserve original shape.
           # Colon notation enables shape preservation

# Get Elements of the Second Last Column

a[:, -2]  # Does not preserve shape.

# Select Last Two Columns

a[:,-2: ]

# Select every other column

a[:, ::2]

# Select last column of every other column

a[:, ::2][:, -1]

a[:, ::2][:, -1:]

# Select every third column

a[:, ::3]

# `[?]` Does every other n element notation `a[::n]` always return the first element `a[1]`?
# `[>]` Yes.

# Select every third column omitting first item

c = np.arange(45,70,2)
c

c[2::3]


def select_everyother_n_omitting_first(a, n):
    return a[n-1::n]


select_everyother_n_omitting_first(c, 3)

# array[lower:upper:step]
# c[2::3] means, start at index 2, all the way to the end, take every third.

# Take every other element of the last 6 items

c[-6::2]

# Take every other element starting from that 6th last item to the first.

# Omitting a bound leads NumPy to select the rest.
c[-6::-2]

# Take every element starting from 6th last to the first (i.e. in reverse).

c[-6::-1]

# Take element element from 6th last to the 8th last in reverse

c[-6:-8:-1]

# Invalid example as the upper and lower cross under the positive step operation.
c[-6:-8:1]

d = np.arange(0,5)
d

# What is the difference between `d[1:3]` and  `d[1:-2]`?
# > `d[1:3]` guarantees an array of size two elements. `d[1:-2]` does not guarantee that as if the array is larger, more elements are returned. If the array was a set of pixels of an image `d[1:-2]` is like cropping the array by -2, while `d[1:3]` only takes the second and third part.

d[1:3]

d[1:-2]

e = np.arange(0,6)

e[1:-2]

# This would always§ return the last two elements
e[-2:]

a[:, ::2]

# `[?]` What is the pattern here? What set of slicing notations guarantee a certain size is return and which don't?

a[:, [1, -1]]

np.arange(25).reshape(5, 5)


