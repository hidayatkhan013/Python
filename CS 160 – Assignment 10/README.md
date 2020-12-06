# CS 160 – Assignment 10

## Problem Description:

Write a program in Python to read a 32-bit integer and output its corresponding value in
dotted decimal notation. For example the number
1000000011111111000000110000 1111 would become 128.255.3.15.

## Inputs

```
Your Python program should accept a 32-bit integer as a raw string.
```
## Output

```
Your program should print the dotted decimal notation.
```
## Approach

```
First, you will want to get your input as a string rather than an integer, because we'll
want to break up the string into four pieces with 8 bits each. It is easy to break up
strings into pieces but much harder to do this for integers.
```
```
The second step will be to break this string up into pieces.
```
```
The third step will be to make a function that takes an eight-character string of ones
and zeroes as input and calculates it's corresponding decimal integer value for the
output. The tricky part here is to figure out what to do as you extract each bit from the
string. A loop would be helpful here along with an if statement, but watch out! The
number 1 is not the same thing as the character '1' and you want to check for characters
from your string, not numbers! Once you've computed the total contributed by each bit
in your string, you should return that total value. The videos in my previous modules
and this module will help you write this program. Please see references below.
```
```
The final step is to combine the first three steps in a small program. You should get the
input as a string, break it into four pieces with the square bracket and colon syntax,
send each of those pieces to your decimal conversion function, and print out the results
of each function call. Be sure to remember to separate each of the four decimal numbers
with a dot!
```

## Examples of output

Please enter the 32-bit integer: 10000000111111110000001100001111  
The dotted decimal notation is: 128.255.3.  



