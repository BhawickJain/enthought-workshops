# ! pip install matplotlib

"""
Filter Image
------------

Read in the "dc_metro" image and use an averaging filter
to "smooth" the image.  Use a "5 point stencil" where
you average the current pixel with its neighboring pixels::

              0 0 0 0 0 0 0
              0 0 0 x 0 0 0
              0 0 x x x 0 0
              0 0 0 x 0 0 0
              0 0 0 0 0 0 0

Plot the image, the smoothed image, and the difference between the
two.

Bonus
~~~~~

Re-filter the image by passing the result image through the filter again. Do
this 50 times and plot the resulting image.

See :ref:`filter-image-solution`.
"""

import matplotlib.pyplot as plt

img = plt.imread('dc_metro.png')

plt.imshow(img, cmap=plt.cm.hot)
plt.show()


def smooth(img):
    centre  = img[1:-1, 1:-1]
    top     = img[ :-2, 1:-1]
    bottom  = img[2:  , 1:-1]
    left    = img[1:-1, 0:-2]
    right   = img[1:-1, 2:  ]


    return (top + left + bottom + right + centre) / 5

# Bad example as it shows how I did keep the width and height of the image consistent. The centre is 1 pixel shorter in height and width compared to left, bottom, right, top.
#
# ```python
#       top    = img[  :-1,   :  ]
#       left   = img[  :  ,   :-1]
#       right  = img[  :  ,  1:  ]
#       centre = img[ 1:-1,  1:-1]
#       bottom = img[ 1:  ,   :  ] 
# ```

smoothed = smooth(img)
plt.figure()
plt.imshow(smoothed, cmap=plt.cm.hot)
plt.show()

# +
import numpy as np


def difference(smooth, img, num):
    return smooth - img[num:-num, num:-num]

# my attempt to add contrast
# difference = (difference - difference.min()) / (difference.max() - difference.min())
# # difference = np.sinh(difference)

plt.figure()
plt.imshow(difference(smoothed, img, 1), cmap=plt.cm.Greens)
plt.show()


# -

def refilter(img, num):
    smoothed = img
    for _ in range(num):
        smoothed = smooth(smoothed)
        
    return smoothed


plt.figure()
plt.imshow(refilter(img,0), cmap=plt.cm.hot)
plt.show()

# notice how you increase `num` which means the image shrinks to nothing by 220 iterations.

plt.figure()
plt.imshow(refilter(img,50), cmap=plt.cm.hot)
plt.show()

plt.figure()
plt.imshow(difference(refilter(img,50), img, 50), cmap=plt.cm.Greens)
plt.show()

plt.figure()
plt.imshow(refilter(img,100), cmap=plt.cm.hot)
plt.show()

plt.figure()
plt.imshow(refilter(img,150), cmap=plt.cm.hot)
plt.show()

plt.figure()
plt.imshow(refilter(img,190), cmap=plt.cm.hot)
plt.show()

plt.figure()
plt.imshow(refilter(img,220), cmap=plt.cm.hot)
plt.show()

plt.figure()
plt.imshow(refilter(img,230), cmap=plt.cm.hot)
plt.show()

plt.figure()
plt.imshow(refilter(img,250), cmap=plt.cm.hot)
plt.show()

# +
import filter_image_solution as fis
import timeit

plt.figure()
plt.imshow(fis.smooth(img), cmap=plt.cm.hot)
plt.show()
# -

plt.figure()
plt.imshow(fis.smooth_loop(img), cmap=plt.cm.hot)
plt.show()

# `[?]` Why is the looped method equivalent in term of outcome to the numpy method?
