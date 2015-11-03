#!/usr/bin/env python

# The four adjacent digits in the 1000-digit number that have the greatest product are
# 9 x 9 x 8 x 9 = 5832.

# Find the 13 adjacent digits in the 1000-digit number that have the greatest product.
# What is the value of the product?

# Included the input number in a text file 'input_8.txt'

file = open('input_8.txt','r')
file_contents = file.read()
digits_to_read = 13

def multiply_digits(number_of_digits, string_in, increment):
  output = 1
  for i in range(0,number_of_digits):
    output *= int(string_in[increment])
    increment += 1
  return output

def main(file, digits):
  i, output = 0, 1
  while i <= (len(file) - digits):
    product = multiply_digits(digits, file, i)
    if product > output:
      output = product
      string = ""
      for i in range(digits):
        string += file[i]
    i += 1
  print "The greatest product comes from the adjacent digits: ", string
  print "The greatest product is: ", output
  return output
   
main(file_contents, digits_to_read)

file.close()