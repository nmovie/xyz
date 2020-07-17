# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 14:28:58 2020

@author: Dell
"""

import pandas as pd
dataset=pd.read_excel("DescriptiveStatistics1.xlsx",sheet_name=0)
dataset.head()
dataset['CurrentSalary'].mean()
