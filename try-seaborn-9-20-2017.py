#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:33:44 2017

@author: wxs
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
# next line makes plots appear in the console
# to undo enter %matplotlib
# %matplotlib inline

titanic = sns.load_dataset("titanic")
iris = sns.load_dataset("iris")
tips = sns.load_dataset("tips")

sns.set_style("whitegrid")
g = sns.lmplot(x="tip", y="total_bill", data=tips, aspect=2)
g = g.set_axis_labels("Tip", "Total bill(USD)")
g = g.set(xlim=(0, 10), ylim=(0, 100))
plt.title("Title")

# -----------------------------------------------------------------------------

g = sns.FacetGrid(titanic, col="survived", row="sex")
g = g.map(plt.hist, "age")    # inline does not work with iPython

sns.factorplot(x="pclass", y="survived", hue="sex", data=titanic)
sns.lmplot(x="sepal_width", y="sepal_length", hue="species", data=iris)

# ----------------------------------------------------------------------------

sns.stripplot(x="species", y="petal_length", data=iris)
sns.swarmplot(x="species", y="petal_length", data=iris)

plt.figure()    # starts a new figure
plt.clf()    # clears current figure

sns.barplot(x="sex", y="survived", hue="class", data=titanic)

plt.clf()
sns.pointplot(x="class", y="survived", hue="sex", data=titanic,
              palette={"male": "g", "female": "m"}, markers=["^", "o"],
              linestyles=["-", "--"])

plt.clf()
sns.boxplot(x="alive", y="age", hue="adult_male", data=titanic)

plt.clf()
sns.boxplot(data=iris, orient="h")

plt.clf()
sns.violinplot(x="age", y="sex", hue="survived", data=titanic)

# ----------------------------------------------------------------------------

plt.clf()
h = sns.PairGrid(iris)    
h = h.map(plt.scatter)

sns.pairplot(iris)

i = sns.JointGrid(x="x", y="y", data=iris)    # Gives error
i = i.plot(sns.regplot, sns.distplot)

sns.jointplot("sepal_length", "sepal_width", data=iris, kind='kde')

# ----------------------------------------------------------------------------

plt.clf()
sns.regplot(x="sepal_width", y="sepal_length", data=iris)

plot = sns.distplot(iris["sepal_width"], kde=False, color="b")












