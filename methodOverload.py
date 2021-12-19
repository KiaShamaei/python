# class Calculate :
#     def __init__(self,n1,n2):
#         self.n1 = n1
#         self.n2 = n2
#     def sum(self,a,b) : 
#         s= a + b
#         return s

# cal = Calculate(50, 60)
# print(cal.sum(5,6))

class A : 
    def show(self):
        print("class A is calling...")
class B(A) :
    def show(self):
        print("class B is calling...")
s = B()
s.show()
