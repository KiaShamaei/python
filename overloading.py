class Student :
    def __init__(self,m1 ,m2 ):
        self.m1 = m1
        self.m2 = m2
    def __add__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3


m1 = Student(10, 15)
m2 = Student(20, 25)

# sum = m1 + m2 ----this is make error to solve make __add__ overloading in student
sum = m1 + m2
print(sum.m1)