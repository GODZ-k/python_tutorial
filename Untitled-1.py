
# # adv="tanmay"
# # addr="machhra"
# # # print("welcome"+ adv)
# # # print("welcome {}".format(adv))
# # data=f"hello my name is {adv}, and i am from {addr}"
# # print(data)
# import random
# def guess(x):
#     com_guess=random.randint(1,x)
#     guess=0
#     while guess != com_guess:
#        guess=int(input("Please enter your guess: "))
#        if guess < com_guess:
#            print("your guess is too low")
#        else:
#            print("your gusee is too high")
#     print(f"conrations your gusess no is {guess} and random is {com_guess}")

# guess(2)
import random
def computer_guess(x):
    l=1
    h=x
    feedback=''
    while feedback !='c':
        guess=random.randint(l, h)
        feedback=input(f"is {guess} to high (h) or {guess}to low  (l) or correct {guess} (c)")
        if feedback == "h":
            h=guess-1
            print(f" your guess{guess} is too high")
        elif feedback == "l":
            l=guess+1
            print(f" your guess{guess} is too low")
    print("congrat")
computer_guess(10)