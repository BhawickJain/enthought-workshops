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

Python arrays have a contiguous representation in memory with meta-data attached which describes its interpretation. So for example, the type of the items and shape are meta-data and when the shape is changed with the `.reshape()` function, the data buffer is unchanged. This is very efficient and computationally affordable [[Nump-Man-Internals](#Nump-Man-Internals)].

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

## References

<a id="Nump-Man-Internals">[Nump-Man-Internals]</a> 
Numpy Interals v1.21 Manual [[URL](https://numpy.org/doc/stable/reference/internals.html)]

<a id="ChabotGh-Workshop">[ChabotGh-Workshop]</a> 
Introduction to Numerical Computing with NumPy Workshop - Github Repo — Alex Chabot-Leclerc [[URL](https://numpy.org/doc/stable/reference/internals.html)]

