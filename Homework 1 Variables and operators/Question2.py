my_list = [0,4,2,1,3]
flag=True
if my_list[0]==my_list[-1]:
    flag=True
else:
    flag=False
print("First and last element are the same: ",flag)

count=0
for new_route in my_list:
    if new_route==2:
        print("Node 2 is in position: ",count)
    count +=1
print("Number of stops: ",count)
print("Position 4 holds element: ",my_list[3])
