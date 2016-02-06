#!/usr/bin/env python
# The Fibonacci sequence is defined by the recurrence relation:
# 
# Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
# 
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
# 
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

fib1, fib2 = 1, 2
max = 1E1000
i = 4

while 1:
  fib3 = fib1 + fib2
  if (fib3 > max):
    break
  fib1 = fib2
  fib2 = fib3
  if len(str(fib3)) == 1000:
    print i
    break
  i += 1

# answer = 4782