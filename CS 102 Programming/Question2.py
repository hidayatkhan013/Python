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



str_user = str(input("Enter Any String : "))
checkString(str_user)
