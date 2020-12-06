from math import sqrt
values = input("Enter p1 x and y coordinates (x1,y1) : ")
list = values.split(",")
p1 = tuple(list)
values = input("Enter p2 x and y coordinates (x2,y2) : ")
list = values.split(",")
p2 = tuple(list)
distance=sqrt((int(p1[0])+int(p2[0]))**2+(int(p1[1])+int(p2[1]))**2)
print("The Euclidean distance between p1 and p2 is: ",distance)

