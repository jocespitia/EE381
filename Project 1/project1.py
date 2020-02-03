'''
EE 381 Spring 2020 Project 1
Name: Jocelyn Espitia
ID # 014101709

Start Date: 01-27-2020
End Date: 02-03-2020
Description: The code implements a linear congruential random number generator, RNG. It will output a uniform 
distribution of numbers on the interval [0, 1).
'''
import math
    
def RNG():
    r= [] # list of random numbers
    #below are the constants used in the formula
    N = 10000 #The norm
    A = 4857 #The adder
    M = 8601 #The multiplier
    # -------------------------------------------

    import time
    S = time.perf_counter()
    #---------------------------------------------

    for k in range(25):
        S = (M * S + A) % N #formula for the RNG
        v = S / N #r is a decimal number in [0, 1)
        r.append(v)
    return r

def die(r):
    print("Die Roll: ")
    for k in range(25):
        die = math.floor(6*r[k] + 1)
        print(die, end= ' ')
        
def coin(r):
    print("\nCoin Toss: ")
    for k in range(25):
        coin = math.floor(2*r[k])
        if coin == 0:
            print("Tails")
        else:
            print("Heads")
        

r = RNG()
die(r)
print()
coin(r)
    
