f=open("txt.txt","r")
f1 = open("abc.txt", "w")

#copy data in txt to abc 
for data in f :
    f1.write(data)

