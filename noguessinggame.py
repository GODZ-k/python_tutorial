import random
print("number must be less then 1000 ")
while True:

 x=int(input("enter your no : "))
 if x<1000:
    y=random.randint(0,1000)
    print("random no is :",y)
    if x>y:
      print("your no is greather then random no")
    else:
      print("your no is less then random no")
 else:
    print('please enter valid no ')