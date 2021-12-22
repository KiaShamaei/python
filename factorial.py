

# def fact (a):
#     sum = 1
#     for i in range(1, a + 1):
#         sum = sum * i
#     print(sum)
def factRecursive(a):
    if(a==1):
        return(a)
    a = a * factRecursive(a -1)
    return a

print(factRecursive(5))





