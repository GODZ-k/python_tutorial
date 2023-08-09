import random

while True:
 ucount=0
 count=0
 print('''
 Rock paper scissor game :
          1: Play yes
          2: no | Exit
  ''')

 x=int(input("choose an option : "))
 if x==1:
    play=int(input("How much times do you want to play this game : "))
    for a in range(1,play+1):   # game will play only five times
     print('''
     What do you want to choose :
      1 Rock
      2 Paper
      3 Scissor
     ''')
     l=['Rock','Paper','Scissor']
     b=random.choice(l)
     y=int(input("please select one option : "))
     if y== 1:
       print("You selected Rock")
       if b==l[0]:
        print("computer selected Rock")
        print("match drow")
        ucount=ucount+1
        count=count+1

       elif b==l[1]:
        print("computer selected paper")
        print("Computer win")

        count=count+1

       else:
        print("computer selected scissor")
        print("You win")
        ucount=ucount+1




     elif y==2:
       print("you selected Paper")
       if b==l[0]:
        print("computer selected Rock")
        print("You win")
        ucount=ucount+1

       elif b==l[1]:
        print("computer selected paper")
        print("Match drow")
        ucount=ucount+1
        count=count+1

       else:
        print("computer selected scissor")
        print("Computer win")
        count=count+1


     elif y==3:
      print("you selected Scissor")
      if b==l[0]:
        print("computer selected Rock")
        print("Computer win")
        count=count+1

      elif b==l[1]:
        print("computer selected paper")
        print("You win")
        ucount=ucount+1

      else:
        print("computer selected scissor")
        print("Match drow")
        ucount=ucount+1
        count=count+1



     else:
      print("please enter valid option")

# for display the final result of the game


    fout=int(input("PRESS 1 FOR FINAL RESULT : "))
    if fout==1:
     if count>ucount:
      print("Computer Win.......")
      print("Your score :",ucount)
      print("Computer score :",count)

     elif count==ucount:
      print("Match drow.......")
      print("Your score :",ucount)
      print("Computer score :",count)

     else:
      print("You Win.......")
      print("Your score :",ucount)
      print("Computer score :",count)

    else:
     print("Invalid input")


 elif x==2:
   break



