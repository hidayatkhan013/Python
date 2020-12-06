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

num1_from_user = int(input("Enter First Number : "))
num2_from_user = int(input("Enter Second Number : "))
print("The value of (a+b)^2: ",a_plus_b_squre(num1_from_user,num2_from_user))
print("The value of (a-b)^2:  ",a_minus_b_squre(num1_from_user,num2_from_user))
print("The value of (a^2-b^2):  ",a_sq_minus_b_sq(num1_from_user,num2_from_user))