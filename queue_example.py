l=[]

while True:
 print('''
        press 1 for insert the elemnets in the queue.
        press 2 for remove the elements into the queue.
        press 3 for display the first & Last value of the queue.
        press 4 for display the all elements of the queue.
        press 5 for exit the operation.  ''')
 c=int(input("enter the instruction: "))

 if c==1:
    a=int(input("how much items do you add in the queue: "))
    for b in range(1,a+1):
      d=input("enter the item : ")
      l.append(d)
    print(l)

 elif c==2:
    if len(l)==0:
      print("queue is empty ")
    else:
      print('''
      press 1 for delete the last element of the queue :
      press 2 for delete the perticular Item of the queue :
      press 3 for delete the first Item of the queue :
      press 4 for clear the queue :  ''')
      x=int(input("enter the operation : "))
      if x==1:
        l.pop()
        print(l)

      elif x==2:
        y=input("which item do you want to delete :")
        # if y not in l.count(y):
        #  print("item is not in the stack")
        try:
         # else:
         l.remove(y)
         print(l)
        except:
          print("Item not in the queue")

      elif x==3:
        del l[0]
        print(l)

      elif x==4:
        l.clear()
        print(l)



 elif c==3:
    print('''
    press 1 for display the first value of the queue
    press 2 for display the last value of the queue
     ''')
    z=int(input("enter the value do you want to see : "))
    if z==1:
     if len(l) == 0:
      print("Queue is empty")
     else:
      print("First value of the queue : ", l[0])

    elif z==2:
     if len(l) == 0:
      print("Queue is empty")
     else:
      print("Last value of the queue : ", l[-1])

    else:
      print("INVALID REQUEST")

 elif c==4:
    # if len(l) == 0:
    #   print("[]")
    # else:
    print(l)

 elif c==5:
   break

 else:
   print("INVALID OPERATION")
