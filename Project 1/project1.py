'''
EE 381 Spring 2020 Project 1
Name: Jocelyn Espitia
ID # 014101709

Start Date: 01-27-2020
End Date:
Description: The code implements a linear congruential random number generator, RNG. It will output a uniform 
distribution of numbers on the interval [0, 1).
'''

#below are the constants used in the formula
N = 10000 #The norm
A = 4857 #The adder
M = 8601 #The multiplier
# -------------------------------------------

import time
S = time.time_ns() - time.process_time_ns()
#---------------------------------------------

for k in range(10):
    S = (M * S + A) % N #formula for the RNG
    r = S / N #r is a decimal number in [0, 1)
    print('%.4f' %r)


