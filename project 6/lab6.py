'''
EE 381
'''
p = float(input("Enter probability of a jump. "))
S = int(input("Enter the standing position. "))
N = int(input("Enter the boundry position."))
J = int(input("Enter the number of jumps wanted. "))

import random

for k in range(J):
    r = random.uniform(0, 1)

    if S == 0:
        S = 1
    if S == N:
        S = N - 1
    if (S < N) and (S > 0):
        if r < p:
            S = S + 1
        else:
            S = S - 1
    print(S)
