### ------------------------------
# Exercise 1
### ------------------------------

Write a procedure that generates n random numbers between 0 and 100, 
prints them, and computes and prints their average.

### ------------------------------
# Exercise 2
### ------------------------------

# Write a procedure that prints a diamond pattern of size n (see below).   
You may assume that n is always an odd number.  
Hint: you may want to experiment with the 'end' named parameter of the  
'print' built-in procedure. E.g.  

          print('*', end='')

prints a star, but does not move the current printing position to the next line.   

## diamond(3)

### Desired output:  
     *
    ***
     *
     
     
## diamond(7)

### Desired output:
       *
      ***
     *****
    *******
     *****
      ***
       *
     
## diamond(15)
### Desired output:
           *
          ***
         *****
        *******
       *********
      ***********
     *************
    ***************
     *************
      ***********
       *********
        *******
         *****
          ***
           *
          


### ------------------------------
# Exercise 3
### ------------------------------

## Write a Python procedure that prints a diagonal pattern (see below). The arguments to this procedure are the number of columns (stars) in each line, the number of lines, and the length of the gap betweentwo consecutive stars on each line.




## diagonals(5, 5, 5)

### Desired output:

   *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
   *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
   *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
    *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
      *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
       *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
        *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *     *
