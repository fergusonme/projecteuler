#!/usr/bin/env python
# 
# A perfect number is a number for which the sum of its proper divisors is exactly equal to 
# the number. For example, the sum of the proper divisors of 28 would be 
# 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
# 
# A number n is called deficient if the sum of its proper divisors is less than n and it 
# is called abundant if this sum exceeds n.
# 
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that 
# can be written as the sum of two abundant numbers is 24. By mathematical analysis, it 
# can be shown that all integers greater than 28123 can be written as the sum of two 
# abundant numbers. However, this upper limit cannot be reduced any further by analysis 
# even though it is known that the greatest number that cannot be expressed as the sum of 
# two abundant numbers is less than this limit.
# 
# Find the sum of all the positive integers which cannot be written as the sum of two 
# abundant numbers.

import math
import time

max_abundant = 20162 # 20162 is the greatest number that cannot be expressed 
                     # as the sum of 2 abundant numbers
                     
def divisors(n):
  yield 1
  max = int(math.sqrt(n))
  if max * max == n:
    yield max
  else:
    max += 1
  for i in range (2,max):
    if n%i == 0:
      yield i
      yield n/i
  
def is_abundant_sum(n):
  for i in abundant_nums:
    if i > n:
      return False
    if (n - i) in abundant_nums:
      return True
  return False  

abundant_nums = [x for x in xrange(12,max_abundant) if sum(divisors(x)) > x ]
sums = [False] * max_abundant

for i in xrange(len(abundant_nums)):
  for j in xrange(i,len(abundant_nums)):
    if abundant_nums[i] + abundant_nums[j] < max_abundant:
      sums[abundant_nums[i] + abundant_nums[j]] = True 

print sum([i for i in xrange(len(sums)) if not(sums[i])])

# answer = 4179871