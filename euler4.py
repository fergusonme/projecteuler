#!/usr/bin/env python

#A palindromic number reads the same both ways. The largest palindrome
# made from the product of two 2-digit numbers is 9009 = 91 x 99.

#Find the largest palindrome from the product of two 3-digit numbers.

minimum = 100 #set the minimum and maximum for the numbers being multiplied
limit = 999

def ispalindrome(string):
  if str(string) == str(string)[::-1]: #test to see if it is a palindrome by checking if
    return True                        #it is equivalent to inverted string
  else:
    return False
    
def main(smallest,largest):
  palindromes=[]
  for i in range(smallest,largest):
    for j in range(smallest,largest):
      product = i*j                     #multiply i and j for all values and check if palindromes
      if ispalindrome(product):
        palindromes.append(product)
  return max(palindromes)

print main(minimum,limit)