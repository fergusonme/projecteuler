#!/usr/bin/env python

#find the largest prime factor of a large number

number = 600851475143
example = 13195

import math
  
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

def main(test_number):
  prime_factors = []
  i = 2
  while i <= test_number:
    if test_number%i == 0:  #check if i is a factor for the number
      if is_prime(i):       #check if i is a prime number
        prime_factors.append(i)   #i is a prime factor, add to our array and factor the number
        test_number = test_number/i
        i = 2 #reset i and start the loop over with the smaller test_number value
    else:
      i += 1 
  return prime_factors
  
#print main(number)

#answer = 6857