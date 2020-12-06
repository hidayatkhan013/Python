# Homework 1: Variables and operators

### Software Tools in decision support

## Instructions

Due date: 22.04.2020 at 23:59.

1. Please, upload your Python files until due date as .zip in Moodle.
2. Name the file namestudentID.zip, e.g. maier1234567.zip.


## Exercises

1. (1 point) Write a program that takes two coordinates from the user, stores them in tuples
and calculates the Euclidean distance between them.
The Euclidean distance between two pointsp 1 with coordinates (x 1 , y 1 ) andp 2 with coordi-
nates (x 2 , y 2 ) is calculated as follows:

```
d(p 1 , p 2 ) =
```
#### √

```
(x 1 +x 2 )^2 + (y 1 +y 2 )^2
```
You will need to add this command to the first line of your program: from math import
sqrt. Functionsqrtreturns the square root value of a number or expression in the paren-
thesis: sqrt(4) yields the value 2.

```
In the end, your program should report something like this:
```
```
The Euclidean distance between p1 and p2 is: # calculated value
```
2. (2 points) Consider the following route.

#### 0

#### 4

#### 3

#### 1

#### 2

a. Write a program that creates the presented route using a list.
b. Check if the first element in the route is equal to the last element. Print to screen if the
result isTrueorFalse.
c. Count the number of stops (items on the list) ofnewrouteand print to screen.
d. Check the position of node 2 innewrouteand print it.
e. Check what element is in position 4 of the list.

```
Your program should report something similar to this:
```
First and last element are the same: # boolean result


Number of stops: # number of stops
Node 2 is in position: # the position of 2
Position 4 holds element: # element currently in position 4

3. (1 point) Write a program that takes an integer number from the user and reports: -
If the number is odd or even - If it is a prime number - Its square value

```
Your program should report:
```
```
The number you typed was: # the number from the user
It is a # odd or even number
It is # a prime or not a prime number
Its square value is: # the calculated value
```
4. (1 point) Given the following list of integers in ascending order, write a program that
asks a number from the user and returns if the number is on the list or not. If the number
is not on the list, report to the user in which position the number should be added to the
list so that it keeps the ascending order.

```
list_numbers = [3, 29, 40, 42, 73, 85, 102, 114, 128, 129, 135, 144]
```

