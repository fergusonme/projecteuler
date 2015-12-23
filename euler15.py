#!/usr/bin/env python
# 
# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the 
# right and down, there are exactly 6 routes to the bottom right corner.
# 
# How many such routes are there through a 20 x 20 grid?

import math


# solution to this problem can be found using formula for combinations. specifically
# 40 nCr 20. pick 20 of the 40 moves to be down moves (or right moves).

side = 20
print math.factorial(side*2) / math.factorial(side) / math.factorial(side)

# answer = 137846528820