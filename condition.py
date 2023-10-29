# a = int(input("enter the no: "))
# print(a)
# a = eval(input("enter the no: "))
# b = eval(input("enter the no: "))
# print(a+b)

# if else condition
# a = eval(input("enter the no: "))
# if a%2==0:
#     print("even")
# else:
#     print("odd")


# # if elif condition
# a=eval(input("enter your no: "))
# if a>=60:
#     print("first division")
# elif a>=40 and a<60:
#     print("socond division")
# elif a<40 and a>=33:
#     print("third division")
# else:
#     print("fail")

# python calculator
# a=int(input("enter the first no: "))
# b=int(input("enter the second no: "))
# opt =input("enter the operator... ")
# if opt=="+":
#     print(a+b)
# elif opt=="-":
#     print(a-b)
# elif opt=="/":
#     print(int(a/b))
# elif opt=="*":
#     print(a*b)
# elif opt=="**":
#     print(a^b)
# else:
#     print("Sorry")

# for loop
# range(start,condition,increment) start 0 by default
# for i in range(1,9,-1):
# for i in range(10,-1):
    # print(i)

# table of 2
# for i in range(1,11):
#  print("2 *",i, "=", 2*i )


# while loop
# i=0
# while i<10:
#     print("hello")
#     i=i+1
#     print(i)

#     a=10
#     while a>0:
#         print(a,"hello")
#         a-=1

# w="welcome to home"
# print(w[9])
# print(w[-1])
# b= w[slice(1,5)]
# or
# print(w[0:7])
# print(w[1::2]) # show string values increment with 2 called slice
# print(b)
# print(w[slice(0,-1)])
# print(w[2:-1])
# print(w[-1::-1])

 # string iteration :
# a="welcome to home"
# b=len(a)
# for c in range(b):
    # print(a[c])
# for reverse iteration : method 1
# for c in range(b-1,-1,-1):
    # print(a[c])
# method 2
# a="welcome to home"
# a=a[-1::-1]
# b=len(a)

# for c in range(b):
#     print(a[c])

# method 3
# w="hello welcome to home"
# for a in w:
#     print(a)


# python string function
# a="welCome To home"    #use for convert the capital letters into small letters
# b=a.lower()
# b=a.upper()       #use for convert the small letters into capital letters
# b=a.capitalize()      #use for convert the first letter of the sentence into capital letter
# b=a.title()            # use to convert the first letter of the string into capital letter
# print(b)


# python string function
# w="welcome"
# b='12121212'
# c="welcome1231"
# d="welcome121@"
# print(w.find('e',2))   # 2 is showing searching starts from second index  . it finding the letter e
# print(w.index('e',2))  # same as find but if letter is not in the string that i am searcing it show the error but find() shows the -1 .
# print(w.isalpha())    # it show the true if string have all the letters in character
# print(b.isdigit())      # it show the true if string have all the letters in digit
# print(w.isdigit())
# print(c.isalnum())
# print(d.isalnum())


# a=chr(65) # convert int into ASCII character
# a=ord('e')   # convert ASCII into int
# print(a)

# use for add the string in the already defined string
# w="wecome {fname} to {lname} home " .format(fname='hello',lname='name')
# w="hello {}  to {}".format('welcome','home')
# w="hello {1:^10} to {0}".format('home','welcome')  #^ for center the text ,> for right the text , < for left the text
# w="hello {a} to {b}".format(a=str(input("enter the first data : ")),b=str(input("enter the second data : ")))
# print(w)

# l=['welcome','to','home']
# print(l[1::1])
# b=len(l)
# for a in range(b):
#     print(l[a])
# for reverse
# for a in  range(b-1,-1,-1):
#     print(l[a])
# print(l[1::2])
# print(l[0],l[1])
# print(l[-1::-1])
# for a in l:
#     print(a)


#list method
# l=[10,20,30,40]
# del l[0]   del delete the element that i want
# l.pop(2)   #pop return the deleted elements
# l.remove(20)  # for remove the item into the list we gives the value of the items
# l.clear()  # it clears the list
# l.insert(0,10) # add 10 at the 0 index of the list
# l.append(10)  # add value 10 at the last position of the list
# a=[20,20]
# print(l)

# l.append(a)

# l.extend(a) it is also used for add the items in the list at the last position
# print(l)


# a=[10,20,30,40]
# l=[input("enter the list item 1:")]
# # y=[input("enter the list item 2:")]
# a.extend(l)
# print(a)

# list comprihension
# l=[]
# for i in range(1,100):
#     l.append(i)


# print(l)

# method 2
# m=[n for n in range(1,101)]
# m=[n for n in range(1,101) if n%2==0]

# print(m)



# n=[m for m in range(1,100,1)]
# print(a)


# list function
# count() it counts the repeated value of the list
# max() show max value of the list
# min() show min value of the list
# sorted()  show the value in accending order
# reverse() show the list values in decending order
# index() show the index of the value


# l=[10,10,10,20,20,50,20,90,80,70,30,50,30,55,77,85,854,298,84]
# a=l.count(10)
# a=max(l)
# a=min(l)
# l.sort()
# l.reverse()
# a=l.index(85)
# print(l)


# star pattern
# x=int(input("enter the no: "))
# for i in range(1,x):
#     for j in range(i):
#      print("*",end="")
#     print("")

# for a in range(x,0,-1):
#     for b in range(a):
#        print("*",end="")
#     print("")



# zip function  - iteration over 2+ lists at the same time
# l=[10,20,30,40]
# l1=[50,60,70,80,90]
# a=len(l)
# # for a,b in zip(l,l1):
#     # print(a,b)

# for t in range(a):
#     print(l[t],l1[t])


# take the input from the use for the list data

# l=[]
# for h in range(1,4):
#     a=input("enter the no:")
#     l.append(a)
# print(l)


# covert string into list
# str='tanmay'
# a=str.split()
# print(a)




#  stack example
# l=[]

# while True:
#  print('''
#         press 1 for insert the elemnets in the stack.
#         press 2 for remove the elements into the stack.
#         press 3 for display the last value of the stack.
#         press 4 for display the all elements of the stack.
#         press 5 for exit the operation.  ''')
#  c=int(input("enter the instruction: "))

#  if c==1:
#     a=int(input("how much items do you add in the stack: "))
#     for b in range(1,a+1):
#       d=input("enter the item : ")
#       l.append(d)
#     print(l)

#  elif c==2:
#     if len(l)==0:
#       print("stack is empty ")
#     else:
#       print('''
#       press 1 for delete the last element of the stack :
#       press 2 for delete the perticular Item of the stack :
#       press 3 for delete the first Item of the stack :
#       press 4 for clear the stack :  ''')
#       x=int(input("enter the operation : "))
#       if x==1:
#         l.pop()
#         print(l)

#       elif x==2:
#         y=input("which item do you want to delete :")
#         # if y not in l.count(y):
#         #  print("item is not in the stack")
#         try:
#          # else:
#          l.remove(y)
#          print(l)
#         except:
#           print("Item not in the stack ")

#       elif x==3:
#         del l[0]
#         print(l)

#       elif x==4:
#         l.clear()
#         print(l)



#  elif c==3:
#     if len(l) == 0:
#       print("stack is empty")
#     else:
#      print("Last value of the stack : ", l[-1])

#  elif c==4:
#     # if len(l) == 0:
#     #   print("[]")
#     # else:
#     print(l)

#  elif c==5:
#    break

#  else:
#    print("INVALID OPERATION")



# Queue example
# l=[]

# while True:
#  print('''
#         press 1 for insert the elemnets in the queue.
#         press 2 for remove the elements into the queue.
#         press 3 for display the first & Last value of the queue.
#         press 4 for display the all elements of the queue.
#         press 5 for exit the operation.  ''')
#  c=int(input("enter the instruction: "))

#  if c==1:
#     a=int(input("how much items do you add in the queue: "))
#     for b in range(1,a+1):
#       d=input("enter the item : ")
#       l.append(d)
#     print(l)

#  elif c==2:
#     if len(l)==0:
#       print("stack is empty ")
#     else:
#       print('''
#       press 1 for delete the last element of the queue :
#       press 2 for delete the perticular Item of the queue :
#       press 3 for delete the first Item of the queue :
#       press 4 for clear the queue :  ''')
#       x=int(input("enter the operation : "))
#       if x==1:
#         l.pop()
#         print(l)

#       elif x==2:
#         y=input("which item do you want to delete :")
#         # if y not in l.count(y):
#         #  print("item is not in the stack")
#         try:
#          # else:
#          l.remove(y)
#          print(l)
#         except:
#           print("Item not in the stack ")

#       elif x==3:
#         del l[0]
#         print(l)

#       elif x==4:
#         l.clear()
#         print(l)



#  elif c==3:
#     print('''
#     press 1 for display the first value of the queue
#     press 2 for display the last value of the queue
#      ''')
#     z=int(input("enter the value do you want to see : "))
#     if z==1:
#      if len(l) == 0:
#       print("Queue is empty")
#      else:
#       print("First value of the queue : ", l[0])

#     elif z==2:
#      if len(l) == 0:
#       print("Queue is empty")
#      else:
#       print("Last value of the queue : ", l[-1])

#     else:
#       print("INVALID REQUEST")

#  elif c==4:
#     # if len(l) == 0:
#     #   print("[]")
#     # else:
#     print(l)

#  elif c==5:
#    break

#  else:
#    print("INVALID OPERATION")
