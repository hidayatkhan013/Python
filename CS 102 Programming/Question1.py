def convertOctal(dec):
    oct_save = 0
    places = 1
    while (dec != 0):
        oct_save = oct_save + (dec % 8) * places
        dec = int(dec / 8)
        places = places * 10;
    return oct_save;

print ("----------------------- Question 1 -----------------------")
decimal_number = int(input("Enter any decimal number : "))
print(f"Decimal Number {decimal_number} equal to octal number : "+str(convertOctal(decimal_number)))



def checkString(str_user): 
    count_lower = 0
    count_upper = 0	
    count_special=0
    count_digits=0
    string_check=('[@_!#$%^&*()<>?/\|}{~:]')
    for i in str_user: 
        if(i.isupper()):
            count_upper=count_upper + 1
        elif(i.islower()):
            count_lower=count_lower + 1
        elif i in string_check:
            count_special=count_special+1
        elif i.isdigit():
            count_digits=count_digits+1

    print("Number of symbols: ",count_special)
    print("Number of digits: ",count_digits)
    print("Number of Upper case letter: ",count_upper)
    print("Number of Lower case letter: ",count_lower)

print ("----------------------- Question 2 -----------------------")

str_user = str(input("Enter Any String : "))
checkString(str_user)


def oddNumbers(num):
    for i in range(1,num):
        if i%2 !=0:
            print(i,end=" ")
print()
print ("----------------------- Question 3 -----------------------")
user_input_nummber=int(input("Enter any Number : "))
oddNumbers(user_input_nummber)


def checkLcm(num1,num2):
    greater_Number=0
    lcm_of_num=0
    if num1 > num2:
       greater_Number = num1
    else:
       greater_Number = num2
    while(True):
       if((greater_Number % num1 == 0) and (greater_Number % num2== 0)):
           lcm_of_num = greater_Number
           break
       greater_Number += 1
    return lcm_of_num


print ("----------------------- Question 4 -----------------------")

num1_from_user = int(input("Enter First Number : "))
num2_from_user = int(input("Enter Second Number : "))
print(f"The LCM of {num1_from_user,num2_from_user} is : ", checkLcm(num1_from_user, num2_from_user))



def a_plus_b_squre(num1,num2):
    result=0
    result=(num1**2)+(num2**2)+(2*num1*num2)
    return result
def a_minus_b_squre(num1,num2):
    result=0
    result=(num1**2)+(num2**2)-(2*num1*num2)
    return result

def a_sq_minus_b_sq(num1,num2):
    result=0
    result=(num1-num2)*(num1+num2)
    return result


print ("----------------------- Question 5 -----------------------")

num1_from_user = int(input("Enter First Number : "))
num2_from_user = int(input("Enter Second Number : "))
print("The value of (a+b)^2: ",a_plus_b_squre(num1_from_user,num2_from_user))
print("The value of (a-b)^2:  ",a_minus_b_squre(num1_from_user,num2_from_user))
print("The value of (a^2-b^2):  ",a_sq_minus_b_sq(num1_from_user,num2_from_user))