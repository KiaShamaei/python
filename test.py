# print ("hello world")
# print("this is ready ") 
# num = 5
# type(num)
#######################################
# input math to python
# import math
# num = 5.5
# print(math.ceil(num))
#######################################
# x = input ("enter 1st value : ")
# y  = input ("enter 2nd value : ")
# print (type(x))
# z = int(x) + int(y) 
# print(z)
#######################################
# x = eval(input("enter a experssion : "))
# print(x)
#####################enter arg from call in terminal #
# import sys
# x = int (sys.argv[1])
# y = int (sys.argv[2])
# result = x + y 
# print(result)
######################### if statement :  ############
# x = int(input ("enter a number : "))
# z = x % 2
# if (z == 0):
#     print("Even")
#     if( x > 13):
#         print("it is Greater")
# else:
#     print ("Odd")
# y = x % 3
# if (y == 0):
#     print("multiple")
############################ loops #################
###while
# x = 1
# while(x <= 5):
#     x = x + 1
#     print("kia")

## for 
# x = ['nanive' , 2 , 3 , 4]
# for i in x : 
#     print(i)
# for i in range(1,20):
#     if (i%5==0):
#         print(i)

####function --------
#define function
# def greeting():
#     print("this is new function")
# #call function ------
# greeting()
#define function with return value 
# def add(a,b):
#     return a + b
# result = add(10,12)
# print(result)
#----------------------define function with name parameter
# def person(name , age):
#     print(name)
#     print(age - 3)
# person( age = 30 , name = 'kia')
# multiple value in argument 
# def sum ( a , *b):
#     c = a
#     for i in b : 
#         c= i + c
#     print(c)
# sum (2 , 3 , 5 ,  6)
#key value multiple ----------
# def person(name , **data):
#     print(name)
#     print(data)
# person("kia" , city="mobi" , age=123)
## find odd and even in list
# lst = [10,11,13,12,24,25,26,80,51,41]
# def count(lst):
#     even = 0
#     odd = 0
#     for i in lst : 
#         if(i % 2 == 0):
#             even = even + 1
#         odd = odd + 1
#     return odd , even
# odd,even = count(lst)
# print("odd is :  {} even is: {}".format (odd , even))

## write fibionachi code
# def fib(n):
#     a=0
#     b=1
#     if(n==1):
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c= a+b
#             a = b
#             b = c
#             print(c)
# fib(4)
#################################
# class Comouter : 
#     def __init__(self):
#         self.name = "Navin"
#         self.age = 30
#     def update(self, newAge):
#         self.age = newAge
# c1 = Comouter()
# print(id(c1))


# class Student :
#     def __init__(self , name , number ):
#         self.name = name
#         self.number = number
#         self.com = self.Com("hp","42")
#     def show(self):
#         print(self.name , self.number)
#         self.com.showC()
#     class Com :
#         def __init__(self , name , model):
#             self.name = name 
#             self.model = model
#         def showC(self):
#             print(self.name , self.model)


# s1 = Student("kia" , "23")
# s1.show()
######################CLASS Inheritance ################

# class Parent : 
#     def __init__(self):
#         print("parent is call")



# class Child(Parent):
#     def __init__(self , name):
#         super().__init__()
#         self.name = name 
#         print("Child is call" + self.name)


# c1 = Child( "kia")

#########################class polymorphism #############
# class Myeditor : 
#     def excute(self):
#         print("editor A ")
# class MyeditorB : 
#     def excute(self):
#         print("editor B")
# class Labtop :
#     def code(self , ide):
#         ide.excute()

# labtop = Labtop()
# ide = MyeditorB()
# ideA = Myeditor()
# labtop.code(ide)
# labtop.code(ideA)
#####################################