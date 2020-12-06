number=int(input("enter any number : "))
print("The number you typed was: ",number)
if number%2==0:
    print("It is a "+str(number)+" Even Number")
else:
    print("It is a "+str(number)+" Odd Number")
flag=False
for i in range(2,number):
    if (number % i) == 0:
        print("It is "+str(number) +" Not a prime Number")
        flag=False
        break
    else:
        flag=True
if flag:
    print("It is "+str(number) +" a prime Number")
print("Its square value is: ",number**2)
