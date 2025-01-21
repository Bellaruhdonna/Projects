# # a= [1,2,3,4]
# # print((len(a))%2 ==0)


# # stu= ["a","b","c","d","e","f","g","h","i","j"]
# # x= len(stu)//2
# # print (stu [x:-1])

# marks= int(input("entermarks: "))

# if marks in range (0,100):
#     if marks in range(0,49):
#         print( "not passed")
#     elif marks in range (50,70):
#         print("good")
#     else:
#         print("best")

# else:
#     print("invalid")

# bike_money= 100000
# saved_money=0
# day= 1

# while saved_money<bike_money:
#     if day%2==0:
#         saved_money= saved_money+1000
#     elif day%2 !=0:
#         saved_money= saved_money+500

#     elif day==0:
#         saved_money= saved_money+0


#     else:
#         saved_money= saved_money+ 0

#     day+=1

# print(day)
# print(saved_money)

# bike_money = 100000
# saved_money = 0
# day = 1

# while saved_money < bike_money:
#     if day % 2 == 0:  # Even day
#         saved_money += 1000
#     else:  # Odd day
#         saved_money += 500
#     day += 1



# print("Total days required:", day - 1)
# print("Total money saved:", saved_money)

bike_money = 100000
saved_money = 0
day = 1

while saved_money < bike_money:
    if day % 2 == 0:  # Even day
        saved_money += 1000
    else:  # Odd day
        saved_money += 500
    day += 1

# Adjusting day to reflect the correct number of days taken
day -= 1

print("Total days required:", day)
print("Total money saved:", saved_money)


