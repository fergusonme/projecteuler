#!/usr/bin/env python

sum = 0
fib1 = 1
fib2 = 2
while 1:
  fib3 = fib1 + fib2
  if (fib3 > 4000000):
    break
  if (fib3%2 == 0):
    sum += fib3
  fib1 = fib2
  fib2 = fib3
print "final: ", sum + 2