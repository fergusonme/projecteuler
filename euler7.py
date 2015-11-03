#!/usr/bin/env python

# By listing the first six prime numbers: 2, 3, 5, 7, 11, 13, we can see that the
# sixth prime is 13.
#
# What is the 10,001st prime number?

import math

prime_number = 10001

#test if a number is prime or not  
def is_prime(n):
  if n == 1:
    return False
  elif n == 2:
    return True
  max = int(math.floor(math.sqrt(n)))
  for i in range(2,max+1):
    if n % i == 0:
      return False
  return True 
  
def main(number):
  i = 1
  counter = 1
  while counter <= number:
    if is_prime(i):
      counter += 1
      prime = i
    i += 1
  return prime

print main(prime_number)

# answer = 104743
    