# single inheritance -----------------------------------
# class A:
#     def classA(self):
#         print('class A')

# class B(A):
#     def classB(self):
#      print('class B')

# a=B()
# a.classB()
# a.classA()

# multilevel inheritance ------------------------------
# class A:
#     def classA(self):
#         print('class A')

# class B(A):
#     def classB(self):
#      print('class B')

# class C(B):
#     def classC(self):
#       print('class C')

# a=C()
# a.classB()
# a.classA()
# a.classC()

# multiple inheritance -------------------------------
class A:
    def classA(self):
        print('class A')

class B:
    def classB(self):
     print('class B')


class C(A,B):
    def classC(self):
      print('class C')

a=C()
# a=B()
a.classB()
a.classA()
a.classC()