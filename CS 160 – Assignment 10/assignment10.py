
#function to read a number
def readNum():
       num = input("Please enter an 32 digit number and I will split it: ")
       return num

#function to check to make sure you have 8 digits
def checkNum(num):
       while len(num) != 32:
              flag = 'error'
              return flag
       else:
              flag = 'true'
              return flag
       
#function to split the number into 2 strings
def splitNum(num):
       first = num[0:8]
       second = num[8:16]
       third = num[16:24]
       forth = num[24:32]
       return [first, second,third,forth]
       
#function to check to see if they are all numbers and calculate sum
def calcSum(first):
       flag = 'true'
       temp=first
       dec_value=0
       base = 1
       temp = int(first)
       while(temp): 
              last_digit = temp % 10
              temp = int(temp / 10)
              dec_value += last_digit * base
              base = base * 2
       
       if flag == 'true':
              return dec_value
       else:
              print("Not a valid number.")

#main function
def main():
       flag = 'true'
       myList = []
       num = readNum()
       flag = checkNum(num)
       if flag == 'true':
              myList = splitNum(num)
              part1 = calcSum(myList[0])
              part2 = calcSum(myList[1])
              part3 = calcSum(myList[2])
              part4 = calcSum(myList[3])
              print("Your number in Dotted pattren = ",part1, ".", part2, ".", part3, ".", part4)
       else:
              print("Not a valid 32 digit number!!")

#call main
main()
              




