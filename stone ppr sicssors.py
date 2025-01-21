import random

def my_game():
    print ("welcome")

options = {1: "rock", 2: "sissors", 3:"paper"}
choose= int(input("enter no:"))
if choose not in options:
   print("invalid")
   return

bot= random.randint(1,3)

if bot== choose:
    print("tie")

elif((choose==1 and bot== 2)
    (choose==2 and bot==3)
    (choose==3 and bot== 1)):
    print ("won")
else:
    print ("loose")

my_game()