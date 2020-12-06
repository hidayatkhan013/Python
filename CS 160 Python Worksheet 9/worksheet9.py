
def read_write_from_file():   
    count_male=count_female=male_score=female_score=total=0
    mylines = []   
    my_dict = [] 
    myfile = open("scores.txt", "r")      
    flag=0 
    for line in myfile:
        mylines.append(line)         
    print(mylines)
    for line in mylines:
        my_dict.append((" ".join(mylines[flag].split()[1:2])," ".join(mylines[flag].split()[-1:]))) 
        print(str(flag+1)+" : "+line,end="")
        flag=flag+1
    print("\n")
    for k in my_dict:
        if k[0]=="M":
            count_male=count_male+1
            male_score=male_score+int(k[1])
        if k[0]=="F":
            count_female=count_female+1
            female_score=female_score+int(k[1])
        total=total+int(k[1])
    myfile.close()
    
    print("Female count: ",str(count_female))
    print("male count : ",str(count_male))
    print("score male :",str(male_score/count_male))
    f_score=float("{0:.2f}".format((female_score/count_female)))
    print("score Female :",str(f_score))
    print("Total avg : ",str(total/(count_female+count_male)))
    print(my_dict)

    f = open("output.txt", "w")
    f.write("Male count = "+str(count_male)+"\n")
    f.write("Female count = "+str(count_female)+"\n")
    f.write("Male average = "+str(male_score/count_male)+"\n")
    f.write("Female average = "+str(f_score)+"\n")
    f.write("Class average = "+str(total/(count_female+count_male))+"\n")
    f.close()





read_write_from_file()



