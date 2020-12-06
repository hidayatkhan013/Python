# Python Worksheet 9

## Problem Description:

In this program we are going to read from a text file and write to a text file. The data to be
read can be found in scores.txt, which is attached to this assignment. Each line in the text
file has a name, gender, school (CC for Community College and UN for University), and a
score. Your program should read the data, and calculate the average score for males and
females and the total average score for all students in the list. This result must be written
to an output file called output.txt.

## Inputs

Your Python program should read data from a text file called scores.txt

## Output

Your program should print the corresponding student’s name and score. Please see
examples of output below.

## Approach

1. Start by reading the contents of the file, scores.txt that I have provided with this
    assignment.
2. You should see that Python displays your contents if you use the print statement.
3. Now use the string functions and split the contents into separate lines first.
4.Now write a loop to display all the data in the list, one per line. Your program
    will look like this
    for line in lines:
       print(i, ":", line)​where line, lines and i are my variables.
5.Now, you will have to do some further splitting of each line into a list of strings.
6.Once you have each token (name, gender, school and score) for each line, you
    can use if statements to check for M or F and calculate the average. Please see
    the example output below and the references from the pdf document.
7. Finally, write your averages to an output file called output.txt. Don’t forget to
    close your output file when you are done.

## Examples of output

['Marga F CC 95', 'Alex M CC 86', 'Tony M UN 99', 'Mona F UN
88', 'Emily F CC 95', 'Mark M UN 88', 'Bill M UN 75', 'Anna F CC
99', 'Ben M CC 66']
- 1 : Marga F CC 95
- 2 : Alex M CC 86
- 3 : Tony M UN
- 4 : Mona F UN
- 5 : Emily F CC
- 6 : Mark M UN
- 7 : Bill M UN
- 8 : Anna F CC
- 9 : Ben M CC
Male count = 5  
Female count = 4  
Male average = 82.8  
Female average = 94.25  
Class average = 87.89  



