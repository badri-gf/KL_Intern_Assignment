class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def addition(self):
        return a+b
    def subtraction(self):
        return a-b
    def multiplication(self):
        return a*b
    def division(self):
        return a/b
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
first=calculator(a,b)
k=int(input("enter the mode of operation : 1.add 2.sub 3.multiply 4.division"))
if(k==1):
    print(first.addition())
elif(k==2):
    print(first.subtraction())
elif(k==3):
    print(first.multiplication())
elif(k==4):
    print(first.division())