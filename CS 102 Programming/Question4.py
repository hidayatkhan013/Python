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

num1_from_user = int(input("Enter First Number : "))
num2_from_user = int(input("Enter Second Number : "))
print(f"The LCM of {num1_from_user,num2_from_user} is : ", checkLcm(num1_from_user, num2_from_user))