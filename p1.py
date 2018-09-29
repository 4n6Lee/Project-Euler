#   Script:     p1.py
#   Full:       Project Euler Problem 1 Solution
#   Author:     Lee Terrell
#   Website:    4n6Lee.com
#
#   Problem Description:
#       If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#       Find the sum of all the multiples of 3 or 5 below 1000.

from datetime import datetime
startTime = datetime.now()

ceiling = 1000
factors = [3, 5]
multiples = []
sum = 0

for f in factors:                       # For each factor
    for x in range(f,ceiling,f):        # For each multiple of that factor
        if x not in multiples:          # If the multiple isn't already accounted for
            multiples.append(x)         # Add the multiple to the list

for x in multiples:                     # For each multiple in the list
    sum+=x                              # Add that multiple to the sum

print(sum)                              # Output the sum
print(datetime.now() - startTime)       # Output the execution time