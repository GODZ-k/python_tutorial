while True:
 class bike:

    def __init__(self):

        print('''
            1  Display the available stock
            2 Request a bike for Rent(100rs ->2qty)
            3 Exit
         ''')
        x=int(input())
        y=100
        if(x ==1):
         print("Total available stock :", y)

        elif(x==2):
          c=int(input("Enter the qty would you like to rent : "))
          if c<=y:
            d=c*2
            y=y-c
            print("total price :",d)
            print("total available stock : ", y)
            # break
          else:
            print("sorry ! we have onle {y} in this stock ")
        # else:
        #   break

 play=bike()




