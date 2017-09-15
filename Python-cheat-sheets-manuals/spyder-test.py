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
