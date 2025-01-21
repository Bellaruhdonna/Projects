import random

def roll():
    max_value= 6
    min_value= 1

    roll= random.randint (min_value ,max_value)
    return roll

    
while True:
    players= input("enter:")
    if players.isdigit():
       players= int(players)
       if 2<=players<=4:
           break
       else:
           print("must be between 2 and 4")
    else:
        print("invalid input")

max_score= 10
# for i in range(players):
player_scores =  [0 for _ in range (players)] #list comprehension

while max(player_scores)< max_score:
    for player_idx in range (players):
        print("player", player_idx+1, "turn started")
        print("your total score is ", player_scores[player_idx])
        current_score=0

        while True:
            should_roll = input("would you like to roll?")
            if should_roll.lower() != "yes":
            
               break

            value= roll()
            if value== 1:
               print("turn done!")
               current_score= 0
    
               break
            else:
                current_score+=value
                print(value)

                print(current_score)

        player_scores[player_idx]+= current_score 
        print ("your total score is: ", player_scores[player_idx])

max_score= max(player_scores)
winning_idx= player_scores.index(max_score)
print("Player number", {winning_idx+1}, "is winner with score", max_score)






