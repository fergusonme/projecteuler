#!/usr/bin/env python
# 
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then 
# there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# 
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
# 
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
# contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of 
# "and" when writing out numbers is in compliance with British usage.


# making a dictionary for the "unique" numbers that build up all the other numbers. The
# key is the number and the value is its length when written out. 
numbers = {
  1 : 3, 
  2 : 3, 
  3 : 5,
  4 : 4,
  5 : 4,
  6 : 3,
  7 : 5,
  8 : 5,
  9 : 4,
  10 : 3,
  11 : 6,
  12 : 6,
  13 : 8,
  14 : 8,
  15 : 7,
  16 : 7,
  17 : 9,
  18 : 8,
  19 : 8,
  20 : 6,
  30 : 6,
  40 : 5,
  50 : 5,
  60 : 5,
  70 : 7,
  80 : 6,
  90 : 6,
  100 : 7,
  1000 : 8
}

def sum_values():
  one_9, ten_19, twenty_99, hundred_999 = 0, 0, 0, 0
  # sum values 1-9
  for i in range(1,10):
    one_9 += numbers[i]
  # sum values 10-19
  for i in range(10,20):
    ten_19 += numbers[i]    
  # sum values 20-99
  for i in range(20,100,10):
    twenty_99 += numbers[i]*10 + one_9
  # sum values 100-999
  hundred_999 = one_9 * 100 + (one_9 + ten_19 + twenty_99) * 9 + numbers[100]*9 + (numbers[100] + 3)*99*9
  return one_9 + ten_19 + twenty_99 + hundred_999 + numbers[1] + numbers[1000]

sum_out = sum_values()
print sum_out

# answer = 21124

