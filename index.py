# ROCK SCISSORS PAPER 1.0

import random 

# print("Welcome to Rock, Scissors, Paper version 1.0! Tell us your name!")
# player_name = input()
# cpu = "CPU"
# print("Hello, " + player_name + "!")
# print("Now, make your choice between Rock, Scissors, Paper")
# player_choice = input()
# CHOICES = ["rock", "scissors", "paper"]
# cpu_choice = random.choice(CHOICES)

# if player_choice not in CHOICES:
#     print ("Please insert a valid choice! Restart the game!")
# else:
#     print  ("CPU choice:" + cpu_choice)

#     if player_choice == cpu_choice:
#         result = "tie"
#     elif (player_choice == "paper" and cpu_choice == "rock") or \
#         (player_choice == "scissors" and cpu_choice == "paper") or \
#         (player_choice == "rock" and cpu_choice == "scissors"):
#         result = "You won!"
#     else:
#         result = "CPU is the winner"

#     print("result: " + result)

# print("Thanks for playing, " + player_name)

# -----------------------------------------

# ROCK SCISSORS PAPER 2.0

# print("Welcome to Rock, Scissors, Paper version 2.0! Tell us your name!")
# player_name = input()
# cpu = "CPU"
# print("Hello, " + player_name + "!")
# print("How many games you want to play?")
# games = int(input())
# for game in range(games):
#     print ("Game " + game)
#     print("Now, make your choice between Rock, Scissors, Paper")
#     player_choice = input()
#     CHOICES = ["rock", "scissors", "paper"]
#     cpu_choice = random.choice(CHOICES)

#     if player_choice not in CHOICES:
#         print ("Please insert a valid choice! the game will shutdown")
#         break
#     else:
#         print  ("CPU choice:" + cpu_choice)

#         if player_choice == cpu_choice:
#             result = "tie"
#         elif (player_choice == "paper" and cpu_choice == "rock") or \
#             (player_choice == "scissors" and cpu_choice == "paper") or \
#             (player_choice == "rock" and cpu_choice == "scissors"):
#             result = "You won!"
#         else:
#             result = "CPU is the winner"

#         print("result: " + result)

# print("Thanks for playing, " + player_name)

# -----------------------------------------

# ROCK SCISSORS PAPER 3.0

# print("Welcome to Rock, Scissors, Paper version 3.0! Tell us your name!")
# player_name = input()
# cpu = "CPU"
# print("Hello, " + player_name + "!")
# print("How many games you want to play?")

# games = int(input())
# player_points  = 0
# cpu_points = 0

# for game in range(games):
#     print (f"Game {game + 1}")
#     print("Now, make your choice between Rock, Scissors, Paper")
#     player_choice = input()
#     CHOICES = ["rock", "scissors", "paper"]
#     cpu_choice = random.choice(CHOICES)

#     if player_choice not in CHOICES:
#         print ("Please insert a valid choice! the game will shutdown")
#         break
#     else:
#         print  ("CPU choice:" + cpu_choice)

#         if player_choice == cpu_choice:
#             result = "tie"
#         elif (player_choice == "paper" and cpu_choice == "rock") or \
#             (player_choice == "scissors" and cpu_choice == "paper") or \
#             (player_choice == "rock" and cpu_choice == "scissors"):
#             result = "You won!"
#             player_points += 1
#         else:
#             result = "CPU is the winner"
#             cpu_points += 1

#         print("result: " + result)
# print (f"{player_name} points:  {player_points}")
# print (f"{cpu} points:  {cpu_points}")
# if player_points > cpu_points:
#     print("You won!")
# elif player_points < cpu_points:
#     print ("CPU Won!")
# else:
#     print ( "Tie!")
# print("Thanks for playing, " + player_name)

# -----------------------------------------

# ROCK SCISSORS PAPER 4.0

print("Welcome to Rock, Scissors, Paper version 4.0! Tell us your name!")
player_name = input()
cpu = "CPU"
print("Hello, " + player_name + "!")

invincible_mode = input('Do you want to play with invincible mode?') == "yes"

if invincible_mode:
    print("Invincible mode actived")
else:
    print("Invincible mode not actived")

print("How many games do you want to play?")

games = int(input())
player_points  = 0
cpu_points = 0

for game in range(games):
    print (f"Game {game + 1}")
    print("Now, make your choice between Rock, Scissors, Paper")
    player_choice = input()
    CHOICES = ["rock", "scissors", "paper"]
    if player_choice not in CHOICES:
        print ("Please insert a valid choice! the game will shutdown")
        break
    else:
        if invincible_mode:
            if player_choice == "paper":
                cpu_choice = "rock"
            elif player_choice == "scissors":
                cpu_choice = "paper"
            elif player_choice == "rock":
                cpu_choice = "scissors"
        else:
            cpu_choice = random.choice(CHOICES)
        print  ("CPU choice:" + cpu_choice)

        if player_choice == cpu_choice:
            result = "tie"
        elif (player_choice == "paper" and cpu_choice == "rock") or \
            (player_choice == "scissors" and cpu_choice == "paper") or \
            (player_choice == "rock" and cpu_choice == "scissors"):
            result = "You won!"
            player_points += 1
        else:
            result = "CPU is the winner"
            cpu_points += 1

        print("result: " + result)
print (f"{player_name} points:  {player_points}")
print (f"{cpu} points:  {cpu_points}")
if player_points > cpu_points:
    print("You won!")
elif player_points < cpu_points:
    print ("CPU Won!")
else:
    print ( "Tie!")
print("Thanks for playing, " + player_name)


