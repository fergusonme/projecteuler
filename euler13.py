#!/usr/bin/env python

# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

file = open('input13.txt','r')
with file as f:
  content = [line.rstrip('\n') for line in f]
content = map(int, content)
sum_final = sum(content)
print "Answer:", str(sum_final)[0:10]

  
