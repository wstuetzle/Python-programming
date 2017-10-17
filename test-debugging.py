#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 13:23:04 2017

@author: wxs
"""

import numpy as np
import numpy.random as rd
import pandas as pd
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import pdb


def table(df, split_by, target_var, summary_function):
    pdb.set_trace()
    result = dict()
    for val in set(df[split_by]):
        print(val)
        is_in = df[split_by == val]
        print(is_in)
        count = sum(is_in)
        summary = summary_function(df[target_var][is_in])
        result[val] = {"count": count, "summary": summary}
    return(result)


titanic = sns.load_dataset("titanic")
table(titanic, "sex", "survived", np.mean)
