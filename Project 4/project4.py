#simulation of a continuous unifrom random variable
#
#
#
import math
import random
import matplotlib.pyplot as plt

n = 10000

x = [] #uniform

for i in range(n):
    r = random.uniform(0, 1)
    x.append(r) #list of random numbers

b = max(x)
a = min(x)

R = b - a #range

intervals = int(math.ceil(math.sqrt(n))) #number of bins

width = (R/intervals)
