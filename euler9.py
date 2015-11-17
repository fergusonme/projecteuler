#!/usr/bin/env python
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#

from functools import reduce
import operator

sum = 1000

potentialtriplets = [[a, b] for a in range(1,sum) for b in range(1,sum)
  if a < b 
  and ((a**2 + b**2)**(0.5))%1 == 0
  and a + b < sum
  and a + b + (a**2 + b**2)**(0.5) == sum]

a,b = potentialtriplets[0][0], potentialtriplets[0][1]
c = sum - a - b
print a*b*c