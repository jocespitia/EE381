import math
import random


#formula = a /(1-r)
probExperiment = []

numTimes = int(input("How many times to run: "))
i = 0
for i in range(numTimes):
    sum1 = int(random.uniform(1, 10))
    print("1st sum you want to obtaint before second sum:", sum1)
    sum2 = int(random.uniform(1, 10))
    print("2nd sum you want to obtain:", sum2)
    sum1Possibilities = (sum1 - 1)/ 36
    sum2Possibilities = ((sum2 - 1) + (sum1 - 1))/36

    r = 1 - sum2Possibilities

    formula = sum1Possibilities / (1 - r)
    probExperiment.append(formula)
    print()
    print(formula, "is the probability we obtain a sum of", sum1, "before we obtain a sum of", sum2)
    print()


print(probExperiment)
#print (formula, "is the probability we obtain a sum of", sum1, "before we obtain a sum of", sum2)
        
        
        

