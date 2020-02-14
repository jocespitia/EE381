'''
EE 381 Spring 2020 Project 1
Name: Jocelyn Espitia
ID # 014101709

Start Date: 02-10-2020
End Date: 02-12-2020
Description: The code implements a linear congruential random number generator, RNG. It will output a uniform 
distribution of numbers on the interval [0, 1).
'''
import math
#below are the constants used in the formula
N = 10000 #The norm
A = 4987 #The adder
M = 122021 #The multiplier
Coin = []
#---------------------------
# Get seed from clock
S = int(input("Enter a seed: "))
#----------------------------

for i in range(1000000):
    S = (M * S + A) % N #RNG Formula
    v = S / N #nums in [0,1)
    coin = math.floor(2*v)
    Coin.append(coin)
#print (Coin)
#Generation of coin flips complete
#----------------------------

game = [] #record of the run of each game
count = 0 #accumulator, num of games
win = 0 #accumulator, num of wins

for i in Coin:
    game.append(i)
    if i == 1: #stop at a head
        count = count + 1 #record count of completed game
        L = len(game) #number of flips in game
        if L % 2 == 1: #is it an odd flip?
            win = win + 1
        game = [] #wipe memory of game to start fresh
p = win / count #frequency simulation
print(p)
        
            
