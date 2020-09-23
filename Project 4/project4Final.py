# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
EE 381 spring 2020
Project 4
Simulation using inverse transform method
Name: Jocelyn Espitia
I.D. #: 014101709
Start Date: 
End Date: 04-20-2020
'''
import math
import random
import matplotlib.pyplot as quarantine
n = 1000000
x = [] # list for random numbers
y = []
Lambda = 0.5
for i in range(n):
 r = random.uniform(0,1)
 x.append(r) # List of unifomly distributed random numbers
 e = (-1 / Lambda) * math.log(1 - r, math.e) #Inverse CDF
 y.append(e)

b = max(x)
a = min(x)
R = b - a # Range
intervals = int(math.ceil(math.sqrt(n))) # The number of bins
width = (R / intervals) # Class Width
quarantine.subplot(2, 1, 1)
quarantine.hist(x, intervals, density = width)

quarantine.subplot(2, 1, 2)
quarantine.hist(y, intervals, density = width)
