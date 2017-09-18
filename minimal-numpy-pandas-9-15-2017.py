# Experiment with Numpy and Pandas to find minimal subset needed for Stat180
# --------------------------------------------------------------------------

import numpy as np
import pandas as pd
import sys

#-----------------------------------------------------------------------------
# From python_tutorial_for_cse446.pdf

def hello_world():
    print("hello world")

hello_world()

a = 5
type(a)
str(a) + ","

False or not ((2 == 3) and (7 <= 5))

def compare(a, b):
    if a > b:
        print("a is larger!")
    elif a < b:
        print("b is larger!")
    else:
        print("a and b are equal!")


compare(5, 7)
compare(5, 5)


# output: 0, 1, 2, 3, 4,
for i in range(5):
    sys.stdout.write(str(i)+",")

# There will be nothing written!
for i in range(6, 2):
    sys.stdout.write(str(i)+",")

# output: 6, 5, 4, 3
for i in range(6, 2, -1):
    sys.stdout.write(str(i)+",")

i = 5
while i >= 0:
    i -= 1
i

range(5)
l = range(5)
type(l)
l
l = list(range(5))
type(l)
l

def reverse_list(l):
    for i in range(round(len(l)/2)):
        tmp = l[i]
        l[i] = l[-(i+1)]
        l[-(i+1)] = tmp
    l.append("hey!")


l = [2, [0, 1], "hi", -9, -7]
reverse_list(l)
l









# May not need tuples

# Lists

bla = range(1, 6)
bla
bla[0]






# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Demo file for Spyder Tutorial
# Hans Fangohr, University of Southampton, UK

def hello():
    """Print "Hello World" and return None"""
    print("Hello World")

# main program starts here
hello()

#=================================================
# Experiment with numpy

import numpy as np


a = np.array([1,2,3])
aa = np.array(a)
aa
aa[0] = 5
a
aa



def vector(list_of_elements):
    vect = np.array(list_of_elements)
    return(vect)

bla = vector([1, 2, 3])
bla[0]
bla[1]

b = np.array([[1.5, 2, 3], [4, 5, 6]])
b[0, 0]
b[0, 2]

c = np.array([[[1.5, 2, 3], [4, 5, 6]], [[1.5, 2, 3], [4, 5, 6]]])
c
len??
print(a)

# See if we can define a method "length" for an array

class Array:
    def length(self):
        return (len(self))


a.__name__
a.mean??
np.mean(a)
np.median(a)
np.ndim(a)
np.ndim(c)
np.size(a)

b[:][0:2]

reverse?

range(20)

L = list(range(10))
A = np.array(L)
len(A)
A

np.array([range(i, i+3) for i in [2, 4, 6]])
np.dtype(A)
a.dtype

np.itemsize(A)

A
A[5::]
A[:5]
A[::2]
A[0:5:]
A[[1,4,5]]
np.copy(A[[1,4,5]])
np.reshape(A, (2, 5))
A[A < 3]
A < 3
A
np.sum(A <= 0)
bool?

mean = [0, 0]
cov = [[1,2], [2,5]]
X = np.random.multivariate_normal(mean, cov, 100)
np.shape(X)
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
plt.scatter(X[::, 0], X[::, 1])

A
a
a = np.array([1, 5, 3, 6])
np.sort(a)
np.sorted(a)
a[np.argsort(a)]

np.dtype?



##################################################
import pandas as pd

df = pd.DataFrame(np.random.rand(20,5))
df.head()
df.describe()

D = {"one" : 1}
D["one"]
D = {"one":1, "two":2}
D["two"]

data = pd.Series(np.linspace(0.25, 1, num =4), index = ["a", "b", "c", "d"])

A[range(3, 9, 2)]



population_dict = {'California': 38332521,
                   'Texas': 26448193,
                   'New York': 19651127,
                   'Florida': 19552860,
                   'Illinois': 12882135}

population = pd.Series( population_dict)
population

area_dict = {'California': 423967,
             'Texas': 695662,
             'New York': 141297,
             'Florida': 170312,
             'Illinois': 149995}

area = pd.Series(area_dict)
area

states = pd.DataFrame({"area":area, "population":population})
states["area"]
states.index
states.bla = "fifi"
states.bla
A
A.bla = "fifi"
pd.DataFrame({"area":area})
states[states.index == "California"]["area"]
states["California", "area"]
population["California"]
states.loc["California", "area"]
states.loc[:, "area"]
states.loc["California", :]
states.loc["California":"Illinois", :]
