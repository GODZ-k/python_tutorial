# class---------------

# class A:
#     a=10
#     def fun(self):
#         print(20+30)

# a=A()
# print(a.a)
# a.fun()

# constructor----------------
class A:
    a=10
    def __init__(self):  # we dont need to call this constructor 
        print("welcome to tanmay")

    def fun(self):
        self.c=self.a+self.a
        print(self.c)

a=A()
a.fun()