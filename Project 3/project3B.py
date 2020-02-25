'''
EE 381 Spring 2020 Project 3B
Name: Jocelyn Espitia
ID # 014101709

Start Date: 02-19-2020
End Date: 02-24-2020
Description: Simulate a Bermoulli RV and use it to make a simple Markov process
'''
import random
RecLoc = []

p_A = float(input("Enter the probability of leaving '0' and going to '1': "))
q_B = float(input("Enter the probability of leaving '1' and going to '25': "))

S = int(input("Enter either '0' or '1' as a starting state: "))
RecLoc.append(S)

for i in range(25):
    r = random.uniform(0, 1)
    if S == 0 and r < p_A:
        S = 1 #moved to node one
    elif S == 1 and r < q_B:
        S = 0 #moved to node zero
    RecLoc.append(S)

for i in RecLoc:
    print(i, end = ' ')
