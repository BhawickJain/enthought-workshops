---
title: Notes of Introduction to Numerical Computing with NumPy by Alex Chabot-Leclerc
date: 06/07/2021 
author:
 - Bhawick Jain
or: 20210706194228
---

Github Repo: https://github.com/enthought/numpy-tutorial-scipyconf-2019

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
The `.shape` returns a tuple.

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

Numpy provides Universal Functions (ufuncs)

```python
np.sin(a)
```
Also capable of vectorized (pair-wise) operation.

`[?]` What are some of the python list-like and non-list-like behaviours of numpy arrays?  
`[>]` Index notation and mutibility are list-like but type coercion and vectorized operations are non-list-like.

Python arrays have a contiguous representation in memory with meta-data attached which descripes its interpretation. So for example, the type of the items and shape are meta-data and when the shape is changed with the `.reshape()` function, the data buffer is unchanged. This is very efficient and computationally affordable [[1]](#1).

## References

<a id="1">[1]</a> 
Numpy Interals v1.21 Manual [URL](https://numpy.org/doc/stable/reference/internals.html)
