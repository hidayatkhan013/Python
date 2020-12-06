#------------------------------
# Exercise 1
#------------------------------

# Write a procedure that generates n random numbers between 0 and 100, 
# prints them, and computes and prints their average.

from random import seed
from random import randint

def avg_of_random(num):
    seed(1)
    avg=0
    for i in range(num):
        value = randint(0, 100)
        avg+=value
        print("Random number # "+str(i+1)+" is ",value)
    print("average of "+str(num) +"random numbers is",avg/num )

# Desired output
#   Random number # 1 is 80
#   Random number # 2 is 6
#   Random number # 3 is 64
#   Random number # 4 is 18
#   Random number # 5 is 22
#   Random number # 6 is 32
#   Random number # 7 is 59
#   Random number # 8 is 45
#   Random number # 9 is 95
#   Random number # 10 is 71
#   Average of 10 random numbers is 49.2

avg_of_random(20)

# Desired output
#   Random number # 1 is 9
#   Random number # 2 is 7
#   Random number # 3 is 37
#   Random number # 4 is 59
#   Random number # 5 is 5
#   Random number # 6 is 33
#   Random number # 7 is 87
#   Random number # 8 is 5
#   Random number # 9 is 4
#   Random number # 10 is 89
#   Random number # 11 is 99
#   Random number # 12 is 32
#   Random number # 13 is 93
#   Random number # 14 is 53
#   Random number # 15 is 96
#   Random number # 16 is 16
#   Random number # 17 is 59
#   Random number # 18 is 75
#   Random number # 19 is 84
#   Random number # 20 is 11
#   Average of 20 random numbers is 47.65

#------------------------------
# Exercise 2
#------------------------------

# Write a procedure that prints a diamond pattern of size n (see below). 
# You may assume that n is always an odd number.
# Hint: you may want to experiment with the 'end' named parameter of the
# 'print' built-in procedure. E.g.
#
#          print('*', end='')
#
# prints a star, but does not move the current printing position to the next line.

def diamond(n):
    for i in range(1, n, 2):
        print(" "*(n//2-i//2), "*"*i)
    for i in range(n, 0, -2):
        print(" "*(n//2-i//2), "*"*i)
    

diamond(3)

# Desired output:
#     *
#    ***
#     *


diamond(7)

# Desired output:
#       *
#      ***
#     *****
#    *******
#     *****
#      ***
#       *


diamond(15)

# Desired output:
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#     *************
#      ***********
#       *********
#        *******
#         *****
#          ***
#           *

#------------------------------
# Exercise 3
#------------------------------

# Write a Python procedure that prints a diagonal pattern (see below). The arguments to this procedure are 
# the number of columns (stars) in each line, the number of lines, and the length of the gap between
# two consecutive stars on each line.

def diagonals(columns, lines, gap):
    for M in range(lines):
        for lk in range(M%gap): 
            print(" ",end="")
        for kk in range(columns):
            print("*",end="")  
            for k in range(gap):
                print(" ",end="")
        print()
    
    

diagonals(20, 40, 5)
#diagonals(5, 5, 5)

# Desired output:
#
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#         *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
#       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     
