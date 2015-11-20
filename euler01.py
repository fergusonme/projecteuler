#!/usr/bin/env python

#find the sum of the numbers between 1 and 1000 that are divisible
#by 3 or 5

sum = 0
for x in range(1,1000):
  if (x%3 == 0) or (x%5 == 0):
    sum = sum + x
print sum  

#answer = 233168