pos = -1

def search (list , n):
    for i in range(len(list)):
        if list[i] == n :
            globals()["pos"] = i
            return True
    return False

list = [2,3,4,6,10,19,11,19]
n=10
if search(list,n):
    print("Found at" , pos+1)
else :
    print("Not found ...")