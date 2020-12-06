names = ['Jim', 'Sarah', 'Jason', 'Lynne', 'Ginny', 'Joe', 'Susan']
scores = [88, 92, 95, 84, 85, 92, 89]

while True:
    name=input("Please enter the name : ")
    if name=='q':
        exit()
    if name in names:
        ind=names.index(name)
        print (name+" scored : ",scores[ind])
    else:
        print(name+" is not present in List")
        
        
