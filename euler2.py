#!/usr/bin/env python

#find the sum of the fibonacci numbers below 4000000 that are even

sum = 0
fib1 = 1
fib2 = 2

#use a while loop that will always evaluate as true

while 1:
  fib3 = fib1 + fib2
  if (fib3 > 4000000):
    break  #break out of the loop if the next number is over 4 million
  if (fib3%2 == 0):
    sum += fib3
  fib1 = fib2
  fib2 = fib3
print "final: ", sum + 2 #include the 2 that comes from initial input

# answer = 4613732