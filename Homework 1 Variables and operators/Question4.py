list_numbers = [3, 29, 40, 42, 73, 85, 102, 114, 128, 129, 135, 144]
number=int(input("Enter any number : "))
flag=False
flag2=False
for i in list_numbers:
    if number ==i:
        print("Number present in list")
        flag=False
        flag2=True
        break
    else:
        flag=True
        if i>number:
            index=list_numbers.index(i)
            flag2=True
            print("The number should be insert at index ",index)
            break
if flag:
    print("Number Not present in list")
if not flag2:
    print("The number should be insert Last index")
        