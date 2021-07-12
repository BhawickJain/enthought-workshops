```python
! pip install numpy
```

```python
import numpy as np

np.__version__  #1.21.0
```

```python
a = np.array([11, 2, 3 ,4])
f = np.array([1.2, 2.3, 4.5, 5.6])
```

```python
a + f
# array([12.2,  4.3,  7.5,  9.6])
```

```python
a.dtype
# dtype('int64')
```

```python
f.dtype
# dtype('float64')
```

```python
g = a + f
g.dtype
# dtype('float64')
```

`int64` is upcasted to `float64`

```python
# ufuncs (Universal Functions)

np.sin(a)
# array([-0.99999021,  0.90929743,  0.14112001, -0.7568025 ])
```

```python
# Elementwise application of the function.
```

Array Indexing
```
| 11 | 22 | 34 |
0    1    2    3 ... Index
```

```python
# Two Dimensinoal Array
```

```python
a = np.array([[0, 2, 4, 6],[1, 3, 5, 7]])
a.shape
```

```python
a.size
```

```python
a.ndim
```

```python
a
```

       -----------> 1 
    |  [0, 2, 4, 6]
    v  [1, 3, 5, 7]
    0

```python
a[0]
```

You select row position (or whatever the 0 axis is)

```python
a[:, 1]
```

a[ axis=0, axis=1, ... axis=n ] Whatever remains comes out as an array


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
b = np.array([[[1,2,3], [1,2,3], [1,2,3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6]], [[7, 8, 9], [7, 8, 9], [7, 8, 9]]])
```

```python
b.ndim
```

```python
b.size
```

```python
b
```

```python
b[1]
```

```python
b[:,1]
```

```python
b[:, :, 1]
```

```python
a
```

```python
a[-1,:]
```

```python
a[:, -1]
```

Select Second Last columns

```python
a[:,-2:-1] # Does preserve original shape.
           # Colon notation enables shape preservation
```

Get Elements of the Second Last Column

```python
a[:, -2]  # Does not preserve shape.
```

Select Last Two Columns

```python
a[:,-2: ]
```

Select every other column

```python
a[:, ::2]
```

Select last column of every other column

```python
a[:, ::2][:, -1]
```

```python
a[:, ::2][:, -1:]
```

Select every third column

```python
a[:, ::3]
```

`[?]` Does every other n element notation `a[::n]` always return the first element `a[1]`?
`[>]` Yes.


Select every third column omitting first item

```python
c = np.arange(45,70,2)
c
```

```python
c[2::3]
```

```python
def select_everyother_n_omitting_first(a, n):
    return a[n-1::n]
```

```python
select_everyother_n_omitting_first(c, 3)
```

array[lower:upper:step]
c[2::3] means, start at index 2, all the way to the end, take every third.


Take every other element of the last 6 items

```python
c[-6::2]
```

Take every other element starting from that 6th last item to the first.

```python
# Omitting a bound leads NumPy to select the rest.
c[-6::-2]
```

Take every element starting from 6th last to the first (i.e. in reverse).

```python
c[-6::-1]
```

Take element element from 6th last to the 8th last in reverse

```python
c[-6:-8:-1]
```

```python
# Invalid example as the upper and lower cross under the positive step operation.
c[-6:-8:1]
```

```python
d = np.arange(0,5)
d
```

What is the difference between `d[1:3]` and  `d[1:-2]`?
> `d[1:3]` guarantees an array of size two elements. `d[1:-2]` does not guarantee that as if the array is larger, more elements are returned. If the array was a set of pixels of an image `d[1:-2]` is like cropping the array by -2, while `d[1:3]` only takes the second and third part.

```python
d[1:3]
```

```python
d[1:-2]
```

```python
e = np.arange(0,6)
```

```python
e[1:-2]
```

```python
# This would always§ return the last two elements
e[-2:]
```

```python
a[:, ::2]
```

`[?]` What is the pattern here? What set of slicing notations guarantee a certain size is return and which don't?

```python
a[:, [1, -1]]
```

```python
np.arange(25).reshape(5, 5)
```

```python
a
```

```python
a[:,-2] = [2, 1]
```

```python
a
```

```python
a[:,-2:-1] = [[3], 
              [2]]
a
```

```python
a[:, -2] = [0, 0]
a
```

Dunder methods, special methods, Python data model

```python
a[0]
```

```python
a.__getitem__(0)
```

```python
a.__setitem__(0,100)
a
```

```python
np.array([1, 2, 3])
```

```python
np.array.__call__([1, 2, 3])
```

```python
len([1, 2, 3])
```

```python
[1, 2, 3].__len__()
```

```python
np.array([[0, 2, 0, 6],
       [1, 3, 0, 7]])
```

```python
len(a)
```

```python
a
```

```python
a = np.array([-1, -3, 1, 4, -6, 9, 3])
```

```python
a < 0
```

```python
a[a<0] = 0
a
```

```python
a = np.arange(0,25).reshape(5,5)
```

```python
a
```

```python
a[[3, 0, 2, 3], [1, 2, 3, 4]]
```

```python
# little easier to see
select = np.array([[3,1], [0,2], [2,3], [3,4]])
a[select[:,0], select[:,1]]
```

```python
# numbers divisible by three
# notice how 0 is also included as divisable by three.
a[a%3==0]
```

```python
a[np.array(a%3==0,dtype='bool') * np.array(a!=0,dtype='bool')]
```

```python
np.array([a==0],dtype='bool')
```

```python
np.array([1, 1, 1]) * np.array([0, 1, 0])
```

```python

```

```python
a = np.ones((3,3), dtype='int32') * 3
a
```

```python
a * 3
```

```python
a * [1, 2, 3]
```

```python
a * [1, 2]
```

```python
a * [[1], [2], [3]]
```

```python
a * [[[1], [2], [3]], [[4], [5], [6]]]
```

```python
np.array([1, 2, 3]) * np.array([[1], [2], [3], [4]])
```

```python
a = np.ones(15, dtype='int32').reshape((5,3))
a
```

```python
b = np.ones(3, dtype='int32').reshape(3) * 3
b
```

```python
a * b
```

```python
a = np.array([[1,2,3],
              [4,5,6]])

a.sum()
```

```python
a.sum(axis=0)
```

```python
a.sum(axis=1)
```

```python
a.sum(axis=1).sum(axis=0)
```

```python
a.sum()
```

```python
a.prod()
```

```python
a.min()
```

```python
a.max()
```

```python
a.argmin()
```

```python
a.argmax()
```

```python
a.ptp() # peak to peak (max - min)
```

```python
a.mean()
```

```python
a.std() # standard deviation
```

```python
a.var() # variance
```

```python
np.array([0,1,0]).any()
```

```python
np.array([0,0,0]).any()
```

```python
np.array([1,1,0]).all()
```

```python
np.array([1,1,1]).all()
```

```python
np.array([0,0.1,0]).any() # non-zero are considered true
```

```python
np.array([0,10,0]).any() # non-zero are considered true
```

```python
np.array([0,-10,0]).any() # non-zero are considered true
```

```python
np.unravel_index(a.argmax(), a.shape)
```

```python
a
```

```python
a = np.arange(-2, 2) ** 2
a
```

```python
mask = a % 2 == 0
mask
```

```python
np.where(mask)
```

```python
a.where(mask)
```

```python
import numpy as np

a = np.array([[11, 22, 34],
              [35, 40, 41]])

a.strides
```

```python
a.T
```

```python
a.T.strides
```

```python
a.dtype.metadata
```

```python
a[:, ::2]
```
