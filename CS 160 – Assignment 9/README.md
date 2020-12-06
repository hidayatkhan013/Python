# CS 160 – Assignment 9

## Problem Description:

In this program we are going to explore a very elementary ‘database’ using Python. Your
program should create and store a list of 20 student names and their corresponding scores.
Then prompt the user to enter a student name and then display the student’s name along
with his/her corresponding score. The user should be able to keep looking up student
scores until he/she enters the single character ‘q’ to quit the program.

## Inputs

```
Your Python program should accept a name as input and keep asking for names until
they enter ‘q’ to quit.
```
## Output

```
Your program should print the corresponding student’s name and score. Please see
examples of output below.
```
## Approach

1. Start by entering and running the following Python code
    names = ['Jim', 'Sarah', 'Jason', 'Lynne', 'Ginny',
    'Joe', 'Susan']
    print (names)
    You should see that Python displays your list of names.
2. Now see what happens when you change the second line to
    print (names[0] + ‘, ‘ + names[1])
    You should see that Python prints the first two names. It is worth noting that
    names[0] displays the first name in the list and names[1] displays the second
    name.
3. Now write a loop to display all the names in the list, one per line. Your program
    will look like this
    for i in range (0, 7):
    print (...)
    where you have to fill in the ...
4. Now add a second list to your program comprising integers, which will represent
    the scores the students got on a particular test:
    scores = [88, 92, 95, 84, 85, 92, 89]
    The idea is that n-th score in the score list corresponds to the n-th student in the
    names list.


5. Modify your program in Python to prompt the user to enter a student name and
    then display the student’s name along with his/her corresponding score.

```
========== RESTART: C:/Temp/list.py =============
Please enter the name: Ginny
Ginny scored 85
```
### >>>

6. Finally, extend your program so the user can keep looking up student scores until
    he/she enters the single character ‘q’ to quit the program.

## Examples of output

Please enter the name: Ginny
Ginny scored 85
Please enter the name: Susan
Susan scored 89
Please enter the name: Jim
Jim scored 88
Please enter the name: q



