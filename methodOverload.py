# class Calculate :
#     def __init__(self,n1,n2):
#         self.n1 = n1
#         self.n2 = n2
#     def sum(self,a,b) : 
#         s= a + b
#         return s

# cal = Calculate(50, 60)
# print(cal.sum(5,6))

# class A : 
#     def __init__(self,a,b,):
#         self.a = a
#         self.b = b 
#     def show(self):
#         print("a")

# class B(A) :
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.a = a
#         self.b = b
#         self.c = c


# b = B(12,13,15)
# b.show()


# class A:
#     def __init__(self,a):
#         self.a = a
#     def show(self,a):
#         print("a first")
#     def show(self , a, b):
#         print("seconf ----")

# a = A(1)
# a.show("a")

# from pythonlangutil.overload import Overload, signature

# class A:
#     @Overload
#     @signature()
#     def stackoverflow(self):    
#         print ('first method')

#     @stackoverflow.overload
#     @signature("str")
#     def stackoverflow(self, i):
#         print ('second method', i)

   
# a = A()
# a.stackoverflow("2")
