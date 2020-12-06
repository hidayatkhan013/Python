def  sort(num1,num2,num3):
    list=[num1,num2,num3]
    list.sort()
    print(list)

def  evenSquares(num):
    k=2
    for i in range(num):
        if i%k==0:
            print(i**2)

def reverse(num):
    reverse_num=0
    while(num>0):
        reminder=num%10
        reverse_num=reverse_num*10+reminder
        num=num//10
    print("Reverse of the number :",reverse_num)

def funStrings(myList):
    for i in myList:
        if "a" in i:
            print(i)
def  GCD(num, den):
    if num > den:
        smaller = den
    else:
        smaller = num
    for i in range(1, smaller+1):
        if((num % i == 0) and (den % i == 0)):
            hcf = i 
    return hcf

def fraction():
    value_from_user=input("Enter any Fraction Like (1/2) : ")
    print(value_from_user)
    numerator =value_from_user.split('/')
    m=GCD(int(numerator[0]),int(numerator[1]))
    print(int(numerator[0])/m,"/",int(numerator[1])/m) 
if __name__== "__main__":
    num1=input("please enter 1st number : ")
    num2=input("please enter 2nd number : ")
    num3=input("please enter 3rd number : ")
    sort(int(num1),int(num2),int(num3))
    num3=input("please enter number to generate even squre : ")
    evenSquares(int(num3))
    num3=input("please enter number to Reverse it : ")
    reverse(int(num3))
    num1=input("please enter 1st number to calculate GCD : ")
    num2=input("please enter 2nd number to calculate GCD  : ")
    print("The G.C.D is", GCD(int(num1), int(num2)))
    num2=input("How many subjects do want to enter? : ")
    Subjects=[]
    for i in range(int(num2)):
        Subjects.append(input(str(i+1)+" Enter subject : "))
    funStrings(Subjects)
    fraction()