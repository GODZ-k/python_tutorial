# class student:
#     __name='tanmay'
#     def  __init__(self):
#         print(self.__name)
#         self.__displayinfo()

#     def  __displayinfo(self):
#         print("hello")


# a=student()
# a.__displayinfo()

# class student:
#     def __init__(self):
#         self.__name=""
#     def getname(self):
#         return self.__name
#     def setname(self,name):
#         self.__name=name

# a=student()
# a.setname("hello welcome to the world")
# name=a.getname()
# print(name)

# overriding
# class A:
#     def hello(self):
#         print("welcome")
# class B(A):
#     def hello(self):
#         # super().hello() this super () functio is used for both class function either inherit or not
#         print("to the world")

# a=B()
# a.hello()

# method overriding
# object one but different arguments or methods
# class area:
#     def A(self,a=None,b=None):
#         if a!=None and b!=None:
#             print(a*b)
#         elif a!=None:
#             print(a*a)
#         else:("nothing")
# c=area()
# # c.A(10)
# # c.A(10,20)