#!/usr/bin/env python

# 2520 is the smallest number that can be divided by each of the 
# numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible
# by all of the numbers from 1 to 20?

max_divisor = 20

def gcd(a,b):   #find the greatest common denominator using euclidean algorithm
  while b != 0:
    t = b
    b = a%b
    a = t
  return a

#find the least common multiple of two numbers using reduction of gcd
def lcm(a,b):  
  output = (abs(b)/gcd(a,b))*abs(a)
  return output

#iterate over the range we want, find the rolling answer of the LCM of i and the answer
#from the previous step
def main(max):
  answer = 1
  i = 1
  while i <= max:
    answer = lcm(answer,i)
    i += 1
  return answer

print main(max_divisor)

# answer = 232792560