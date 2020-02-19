'''
EE 381 Spring 2020 Project 1
Name: Jocelyn Espitia
ID # 014101709

Start Date: 02-10-2020
End Date:
Description: Simulate a Bermoulli RV and use it to make a simple Markov process
'''

import random

p = float(input("Enter the probability of success: "))
T = int(input("how many trial? "))

for j in range(T):
    r = random.uniform(0, 1)
    if r < p:
        print('1', end=' ')
    else:
        print('0', end=' ')
