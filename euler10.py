#!/usr/bin/env python
#
# The sum of primes below 10 is 2 + 3 + 5 + 7 = 17
#
# Find the sum of all the primes below 2 million.

import euler7  #re-using my code for problem number 7

max, sum = 2000000, 5

for i in range(5,max,2):
  if euler7.is_prime(i):
    sum += i

print sum

# answer = 142913828922