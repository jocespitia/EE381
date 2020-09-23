'''
EE 381 spring 2020
Project 4
Simulation using inverse transform method
Name:
I.D. #:
Start Date:
End Date:
'''
import math
import random
import matplotlib.pyplot as quarantine
n = 1000000
x = [] # list for random numbers
for i in range(n):
 r = random.uniform(0,1)
 x.append(r) # List of unifomly distributed random numbers

b = max(x)
a = min(x)
R = b - a # Range
intervals = int(math.ceil(math.sqrt(n))) # The number of bins
width = (R / intervals) # Class Width
quarantine.hist(x, intervals, normed = width)
