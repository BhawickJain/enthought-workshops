---
title: Notes of Introduction to Numerical Computing with NumPy by Alex Chabot-Leclerc
date: 06/07/2021 
author:
 - Bhawick Jain
or: 20210706194228
---

Github Repo: [[ChabotGh-Workshop](#ChabotGh-Workshop)]

Simple problem statement

```python
>>> a = [1,2,3,4,5]
>>> b = [10,11,12,13,14]

>>> a + b
[1,2,3,4,5,10,11,12,13,14]
```

This is an unexpected result if you thought `a` and `b` are matrices. In standard python arrays you need perform a pairwise addition as follows:

```python
>>> c = []
>>> for i,j in zip(a,b):
        c.append(i,j)
```

This is a single dimensional matrix, and addition. There are an enormous number of matrix operations which needs to process efficiently without the pain of having to code that yourself. This is where NumPy begins.

```python
import numpy as np

a = np.array([1,2,3,4])
b = np.array([10,11,12,13])

c = a + b
c
# [11,13,15,17]
```
The numpy array enables those operation and `c` in this instance of also a numpy array.

```python
type(c)
# numpy.ndarray
```
the `nd` part refers to `n` dimensional array.

numpy arrays must have items of the same type which can be accessed by
```python
a.dtype
# dtype('int64')
```
```python 
f = np.array([1.2, 4.5, 4.3])
f.dtype
# dtype('float64')
```
```python
a
# array([1,2,3,4])

a[0]
# 1

a[0] = 10
a
# array([10,2,3,4])

a[0] = 11.5
a
# array([11,2,3,4])
```
You can access an item in the array through their index and even change the value, however as it must conform to the `dtype` of the array the new value will be casted over. For `float64`, the value 11.5 is truncated to 11 into `int64`.

`[?]` explore casting properties in numpy across different dtypes  


```python
a.ndim
# 1

a.shape
# (4,)
```
The `.shape` returns a tuple, the lenght of tuple represents the number of dimensions.

```python 

a.size
# 4
```
The `.size` is the number of items in the array.

Element-wise operation by default
```python
a + f

a * f

a / f

f ** a

a * 10
```

This means you are not doing standard matrix operations, instead this conceptual iteration is referred to a vectorized operation

Numpy provides Universal Functions (aka UFuncs)

```python
np.sin(a)
```
Also capable of vectorized (pair-wise) operation.

```python
>>> a = np.array([11, 2, 3, 4])
>>> np.sin(a)
array([-0.99999021,  0.90929743,  0.14112001, -0.7568025 ])
```

`[?]` What are some of the python list-like and non-list-like behaviours of numpy arrays?  
`[>]` Index notation and mutibility are list-like but type coercion and vectorized operations are non-list-like.


### Slicing

```
var[lower:upper:step]
```
step is also referred to as stride

```python
>>> c = np.arange(45, 70, 2)

>>> c[0:4] # index 0 to, but including index 4
[45, 47, 49, 51]

>>> c[0:4] # from index 0 to, but not including index 4
           # take every second (other) one.
[45, 49]

>>> c[::4] # take every value up to index 4
[45, 47, 49, 51]

# Notice first value is always returned

>>> c[-2:] # take the last two
[68, 70]

>>> c[:-2] # take everything but the last two
            # this operation does not guarantee
            # a fixed sizes return.
[45, 47, ..., 64, 66]

>>> c[2:] # take every item from the third item.
           # no size guarantee
[49, 51 ... 68, 70]

>>> c[:2] # size of 2 guaranteed.

>>> c[-1:-6:-1] # from last to, but not including
                # 6th last in reverse direction
                # Move from Upper pointer to Lower
                # Pointer
[70, 68, 66, 64, 62]

>>> c[-1:-6] # lower and upper pointers cross
             # so yield empty array
[]

```

```python
>>> a = np.array([[0, 2, 4, 6],[1, 3, 5, 7]])
array([[0, 2, 4, 6],
       [1, 3, 5, 7]])

>>> a[:,-2:-1] # Does preserve original shape.
               # Colon notation enables shape preservation
array([[4],
       [5]])

>>> a[:, -2] # Does not preserve original shape.
array([4, 5])

>>> a[:, -2:] # Select Last two results
array([[4, 6],
       [5, 7]])

>>> a[:, ::2] # Select every other column
array([[0, 4]
       [1, 5]])

>>> a[:, ::2][:, -1] # Last Column of every other column
array([4, 5])

>>> a[:, ::2][:, -1:] # Shape Preserved
array([[4],
       [5]])

>>> a[:, [1, -1]] # take second and last row
array([2, 6],
      [3, 7])
```


3D Array example

```python
>>> b = np.array([[[1,2,3], [1,2,3], [1,2,3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [7, 8, 9]]])
array([[[1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]],

       [[4, 5, 6],
        [4, 5, 6],
        [4, 5, 6]],

       [[7, 8, 9],
        [7, 8, 9],
        [7, 8, 9]]])

>>> b[1]
array([[4, 5, 6],
       [4, 5, 6],
       [4, 5, 6]])
```
```
    0
   /
  /
 /
 ---------------- 2
|
|
|
|
1
```

```python
>>> e = a[1] # equal to a[1, :]
array([0, 2, 4, 6])

```
`a[1, :]` tells your future self or another reader that `a` is at least of two dimensions whilst `a[1]` does not. `a[1]` is will also accept a one-dimensional array and probably break some code downstream. So something to think about in terms of code quality. In fact in this specific example a[-1, :] is even better as it tell you and the reader that you want the last row of the (at least) two dimensional array. Whatever caused the input to have a bad array, by using a more explicit notation you enable the error to thrown earlier and closer to the cause.

``` python
>>> a[:,::2 ] # take every row but take every other column
array([[0, 4],
       [1, 5]])

>>> a.fill(-4.8)
>>> a
array([[-4, -4, -4, -4],
       [-4, -4, -4, -4]])
```

You can assign against a slice, below a scalar value is [broadcasts](https://numpy.org/doc/stable/user/basics.broadcasting.html) into the shape of the slice. This changes `a` in memory.

```python
>>> a[:, 1::2] = 4
>>> a
array([[-4, 4, -4, 4],
       [-4, 4, -4, 4]])
```

`[?]` Do you need to match the shape of the array say when assigning `a[:, 1:2]`?  

### Python Dunders

Dunders drive Pythons Syntactic sugar, below is a demo of the key ones that define the Numpy notation experience. A more comprehensive guide to is Fluent Python - Luciano Ramalho [[2015-Ramanho](#2015-Ramanho)].

```python
>>> a = np.array([[0, 2, 0, 6],
       [1, 3, 0, 7]])

>>> a[0]
array([0, 2, 0, 6])

>>> a.__getitem__(0)
array([0, 2, 0, 6])

>>> a.__setitem__(0)
array([[100, 100, 100, 100],
       [  1,   3,   0,   7]])

>>> len(a)
2

>>> a.__len__()
2

>>> np.array([1, 2, 3])
array([1, 2, 3])

>>> np.array.__call__([1, 2, 3])
array([1, 2, 3])
```

### Fancy indexing

Indexing by Position

```python
>>> a = np.arange(0, 80, 10)
>>> index = [1, 2, -3]
>>> y = a[indices]
>>> print(y)
[10, 20, 50]

>>> a[indices] = 99
>>> a 
array([0, 99, 99, 30, 40, 99, 60, 70])
```
Indexing by Boolean — aka Masking

```python
>>> mask = np.array([0, 1, 1, 0, 0, 1, 0, 0]), dtype=bool)
>>> y = a[mask]
>>> y
array([99, 99, 99])
```
It is unsual to have build a boolean mask by hand, often other functions are used that return a boolean mask of a numpy array which can be used to fancy index out the true values.

```python
>>> a = np.array([-1, -3, 1, 4, -6, 9, 3])
>>> mask = a < 0
>>> mask
array([ True,  True, False, False,  True, False, False])

>>> a[mask]
```
You can combine fancy indexing with its mask like so:
```python
>>> a[a < 0]
array([-1, -3, -6])

>>> a[a < 0] = 0

>>> a
array([0, 0, 1, 4, 0, 9, 3])
```

This is identical to how pandas dataframe indexing works — at least conceptually.
`[?]` What are the differences between the operations and indexing/slicing Pandas.Dataframe/Series offers and Numpy.Arrays?  

### Multi-Dimensional Arrays

You can think of a 4 dimensional array as an array of 3 dimensional arrays.

You add dimensions as the following:
```python
(4,)         # 1 dim

(2, 4)       # 2 dim

(3, 2, 4)    # 3 dim

(2, 3, 2, 4) # 4 dim
```
Notice how newly added dimension is always on axis 0 and first dimension added is on axis n for that ndim array. The rule is that newly added axis is always the lowest dimension.

This may be because ensures axis 0 is always the fastest changing index when parsing through the data buffer of the `numpy.array`. The high axes simply become holders of more arrays of an lower dimensional array. This is to ensure the array is row-major which is how the c-family of languages represent data in memory. FOTRAN and MATLAB columns major, i.e. when you parse through the memory buffer of a FOTRAN array, you are moving in the column-direction (left to right) in the array instead of down (row-wise).

One nice property of Numpy.Array shapes is that the last dimension can be seen as the number of columns. This mean `axis=-1` is always the last axis of the array.

When using reduce functions, you will reduce the lowest axis in the array default whichi is 0.

### Array Calculation Methods

Rules:
1. Operations between multiple array objects are first checked for proper shape match.
2. Mathematical operators (+ - * / exp, log, ...) apply element by element, on the values.
3. Reductions operations (mean, std, skew, kurt, sum, prod, ...) apply to the whole array, unless an axis is specified.
4. Missing values propagate unless explicitly ignored (nanmean, nansum, ...)

`np.nan` properties
```python
>>> np.nan
nan

>>> np.nan + 1
nan
```

`[?]` What is array broadcasting?
`[>]` It is numpy's sane default that an array of the lower dimension to match another array of a dimension by duplicating values in direction of an extra dimension until the shape in that dimension matches. The operation is then repeated for each extra dimension until the dimensions match. Note that the shape in existing dimensions must match otherwise a shape error is thrown.

Some examples

```python
# broadcast for a 3x3 array
>>> 3
[[3, 3, 3],
 [3, 3, 3],
 [3, 3, 3]]

>>> [1, 2, 3]
[[1, 2, 3],
 [1, 2, 3],
 [1, 2, 3]]
```

```python
>>> a = np.ones((3,3), dtype='int32') * 3
>>> a
array([[3, 3, 3],
       [3, 3, 3],
       [3, 3, 3]], dtype=int32)

>>> a * 3
array([[9, 9, 9],
       [9, 9, 9],
       [9, 9, 9]], dtype=int32)

>>> a * [1, 2, 3]
array([[3, 6, 9],
       [3, 6, 9],
       [3, 6, 9]])

>>> a * [1, 2] # dimension match but shape does not.
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
/tmp/ipykernel_34/4212024589.py in <module>
----> 1 a * [1, 2]

ValueError: operands could not be broadcast together with shapes (3,3) (2,)

>>> a * [[1], [2], [3]]
array([[3, 3, 3],
       [6, 6, 6],
       [9, 9, 9]])

>>> a * [[[1], [2], [3]], [[4], [5], [6]]]
array([[[ 3,  3,  3],
        [ 6,  6,  6],
        [ 9,  9,  9]],

       [[12, 12, 12],
        [15, 15, 15],
        [18, 18, 18]]])

>>> np.array([[1], [2], [3]]) * np.array([1, 2, 3])
array([[1, 2, 3],
       [2, 4, 6],
       [3, 6, 9]])
```
Broadcasting is a key feature that enables matrices and scalar values to play nicely together.

When adding new axis it adds them on the left as axis 0

```
a (5, 3)
b (3,)

a + b
a (5, 3)
b ( , 3) # duplicating axis = 1 across axis = 0 five times to match shape.
```

Reduction functions

When applying a reduction function, the entire array is reduced to a single value. 

`[?]` Is this different to Pandas Reduce functions?  

```python
>>> a = np.array([[1, 2, 3]
                  [4, 5, 6])

>>> a.sum()
21

>>> a.sum(axis=0)
array([5, 7, 9])

>>> a.sum(axis=1)
array([6, 15])

>>> a.sum(axis=1).sum(axis=0)
21
```
You need to specify an axis, inorder to prevent this.

Other reduce functions

```python
>>> a = np.array([[1,2,3],
              [4,5,6]])
```
# Mathematical Functions
```
>>> a.sum()
21

>>> a.sum(axis=0)
array([5, 7, 9])

>>> a.sum(axis=1)
array([ 6, 15])

>>> a.sum(axis=1).sum(axis=0)
21

>>> a.prod() # multiply everything together
720

>>> a.min()
1

>>> a.max()
6

>>> a.argmin() # index pos of first min
0

>>> a.argmax() # index pos of first max
5


# argmax() and argmin() give a flat index
# that is it refers to the nth item in the
# in the data buffer.

# to get an index that respects the
# dimensionality of the orignal array
# use .unravel_index

>>> np.unravel_index(a.argmax(), a.shape)
(1,2) # index 1 in ax 0, index 2 in ax 1

#       0  1  2
#   0 [[1, 2, 3],
#   1  [4, 5, 6]]

# Use the where function which finds
# index position against a truth
# array which represent anything.

# finding out all max values is one
# example
>>> np.where(a == a.max())
(array([2, 3]),)
# returns index coordinate

# This is different from fancy index
# masking which returns values of the
# array that are True in the mask
# instead of their index coordinate.


>>> a.ptp() # peak to peak (max - min)
5

>>> a.mean()
3.5


# Statistical

>>> a.std() # standard deviation
1.707825127659933

>>> a.var() # variance
2.9166666666666665


# Truth value testing

>>> np.array([0,1,0]).any()
True

>>> np.array([0,0,0]).any()
False

>>> np.array([1,1,0]).all()
False

>>> np.array([1,1,1]).all()
True

# Python treat non-zero values as True
# this holds in NumPy

>>> np.array([0,0.1,0]).any() # non-zero are considered true
True

>>> np.array([0,10,0]).any() # non-zero are considered true
True

>>> np.array([0,-10,0]).any() # non-zero are considered true
True
```


Most NumPy function can be used as methods, `a.min()` and as functions `np.min(a)`. Generally methods run faster. Most also have Axis options availble to limit / manage the reduction process. 

## NumPy Memory Representation
NumPy arrays have a contiguous representation in memory (much standard Python Arrays) with an additional meta-data attached which describes its interpretation. 

Some examples of metdata
- dtype
- data (pointer to the first item in the array)
- strides (the number elements it needs to jump to go the next item in a specific direction of a dimension)

So for example, the type of the items and shape are meta-data and when the shape is changed with the `.reshape()` function, the data buffer is unchanged - instead the strides change.This is very efficient and computationally affordable [[Nump-Man-Internals](#Nump-Man-Internals)].

```
 | 11 | 22 | 34 | 35 | 40 | 41 |   ... data
 0    1    2    3    4    5    6   ... Index
 a8   a9   aa   ab   ac   ad   ae  ... Memory Address

Interpretation
~~~~~~~~~~~~~~~~~~~~

array([[11, 22, 34],
       [35, 40, 41]])

Metadata
————————
Strides: axis 0: 4
         axis 1: 1

Shape: (3, 2)

Data Pointer: a8


```

## Transpose operation
```
a.T
```
In a transpose operation, the `np.array.shape` tuple and the `np.array.strides` will swap axes.
`[?]` Does that mean as certain shapes, it maybe suboptimate to do an operation as the dimension you are working on has much larger strides?  

## Slice
```
a[:, ::2]
```
The Data Pointer for the start in Memory does not change, but the strides triple in axis 1 to only show every third column value.
data pointer won't change, the strides will triple in the example. Change in shape and data pointer can be changed by index.

## Fancy indexing

In fancy indexing a new array is created.
`[?]` Does that make fancy indexing expensive?

Reshaping is free.

### Flattening Arrays
`[?]` When will the `ravel` function return a copy of an array and when it won't?
`[?]` What is the difference between the Flatten and Ravel function?  

## References

<a id="Nump-Man-Internals">[Nump-Man-Internals]</a> 
Numpy Interals v1.21 Manual [[URL](https://numpy.org/doc/stable/reference/internals.html)]

<a id="ChabotGh-Workshop">[ChabotGh-Workshop]</a> 
Introduction to Numerical Computing with NumPy Workshop - Github Repo — Alex Chabot-Leclerc [[URL](https://numpy.org/doc/stable/reference/internals.html)]

<a id="2015-Ramanho">[2015-Ramanho]</a>
Fluent Python — Luciano Ramanho (O'Reilly)(2015) [[Github](https://github.com/fluentpython)] [[O'Reilly Book](https://www.oreilly.com/library/view/fluent-python/9781491946237/)]
