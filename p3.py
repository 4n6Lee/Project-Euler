#   Script:     p3.py
#   Full:       Project Euler Problem 3 Solution
#   Author:     Lee Terrell
#   Website:    4n6Lee.com
#
#   Problem Description:
#       The prime factors of 13195 are 5, 7, 13 and 29.
#       What is the largest prime factor of the number 600851475143 ?

import math
from datetime import datetime
startTime = datetime.now()

number = 600851475143
primeFactors = []

# Construct a list of odd factors of the given number
# Note: I iterated through only odd numbers below the square root of the given number because the end result requires
#       only prime numbers.
for x in range(1, int(math.sqrt(number))+1, 2):
    if number % x == 0:
        if x not in primeFactors:
            primeFactors.append(x)

# Remove non-prime numbers from the list of odd factors
for f in primeFactors.copy():
    for x in range(2, int(math.sqrt(f))+1):
        if f % x == 0:
            if f in primeFactors:
                primeFactors.remove(f)

print(primeFactors[len(primeFactors) - 1])  # Output the largest prime factor
print(datetime.now() - startTime)           # Output the execution time