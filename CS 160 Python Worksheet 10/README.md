# Python Worksheet 10

## Practice with functions:

1. Name your file ws10.py
2. Write functions to do the following:
3. Part 1:
    a. Write a function called sort(num1, num2, num3). It takes three whole
       numbers as parameters. The function does not return anything.
    b. This function outputs the 3 numbers in ascending order.
4. Part 2:
    a. Write a function called evenSquares(num) that accepts a number ​ **num** ​as an
       argument and prints all even squares between 1 and ​num ​inclusive. ​ **You**
       **must use the range function for this.**
5. Part 3:
    a. Write a function called reverse(num) that takes a two digit number as a
       parameter. Use int to do this. Do not use strings.
    b. It should return one number that is now the reverse of the original number.
    c. For example, reverse(95) should return 59.
    d. Hint: Use // for integer or whole number division, meaning it will not give
       you decimal numbers. Divide the number by 10 or use % to get the
       remainder to separate the two digits.
6. Part 4:
    a. Call this funStrings(myList). It takes a list of strings as a parameter.
    b. Use a for loop, and print all the words that have the letter ‘a’ in them.
    c. Hint: Use the ​ **if ‘a’ in strvar:** ​ syntax to check if there is something in
       a string.
7. Part 5:
    a. Write a function called GCD(num, den) that accepts 2 integers as parameters.
    b. Compute the GCD of the 2 numbers.
    c. Return this value.
    d. Hint: The classic algorithm for computing the GCD, known as Euclid’s
       algorithm, goes as follows: Let num and den be variables containing the two
       numbers. If den is 0, then stop - num contains the GCD. Otherwise, compute
       the remainder when num is divided by den. Copy den into num and copy the
       remainder to den. Then repeat the process, starting with testing whether
       den is 0.


8. Part 6:
    a. Write a function called fraction() that asks the user to enter a fraction, then
       reduces the fraction to lowest terms. You read a fraction like 4 / 8 and split
       at the ‘/’.
    b. Then call the GCD function and send the numerator and denominator to it.
    c. When the GCD returns, store it in a variable and divide the numerator and
       denominator by it and print ½.
    d. Your function should read any fraction and print it in the lowest terms.
9. Part 7:
    a. Call this function main().
    b. Call sort(12, 31, -2).
    c. Then call evenSquares(28). This will print the even squares from 1 to 28.
    d. Next call reverseNum(98). This will return a number that is the reverse of
       the number you passed. Print it.
    e. Then call funStrings(myList) and send the list of words to this. It will print
       the words that have the letter ‘a’. Use any list of words like this:
       Subjects = [‘Math’, ‘Algebra’, ‘Computer Science’, ‘Biology’, and so on.....]
    f. Then call fraction() which will read a fraction from the user and print it in its
       lowest terms.
10.Finally call main().


