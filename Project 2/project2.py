'''
EE 381 Spring 2020 Project 1
Name: Jocelyn Espitia
ID # 014101709

Start Date: 01-27-2020
End Date: 02-03-2020
Description: The code implements a linear congruential random number generator, RNG. It will output a uniform 
distribution of numbers on the interval [0, 1).
'''
import time
import math

Coin = 0 #initialize variable, zero is tail

while Coin == 0:

    #below are the constants used in the formula
    N = 95999 #The norm
    A = 4857 #The adder
    M = 901 #The multiplier

    
    S = time.time() - time.process_time()

    for i in range(10):
        S = (M * S + A) % N #formula for the RNG
        v = S / N #r is a decimal number in [0, 1)
        time.sleep(0.005)
    Coin = math.floor(2*v)
    print(Coin)
