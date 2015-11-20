#!/usr/bin/env python

# The sum of the squares of the first ten natural numbers is:
#  1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is:
#  (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten
# natural numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred
# natural numbers and the square of the sum.

max_value = 100

def sum_of_square(max):   #brute force implementation, because limit of 100 isn't that large
  answer = 0
  for i in range(1,max+1):
    answer += i*i
  return answer
  
def square_of_sum(max):
  answer = 0
  for i in range(1,max+1):
    answer += i
  answer *= answer
  return answer
  
def main(max):
  difference = square_of_sum(max) - sum_of_square(max)
  return difference

print main(max_value)