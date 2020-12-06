def oddNumbers(num):
    for i in range(1,num):
        if i%2 !=0:
            print(i,end=" ")
user_input_nummber=int(input("Enter any Number : "))
oddNumbers(user_input_nummber)