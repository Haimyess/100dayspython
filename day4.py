import random
import my_module

# print("Day 4")
# print(my_module.my_first_module)

# Print a float random number 
# random_num = round(random.random() * 10)
# random_num_no_round = random.random() 
# print(random_num)
# print(random_num_no_round)

# Print a random int no decimals  
# random_ranges = random.randint(5, 10)
# print(random_ranges)


# ----------------------------------
# -----------Heads and Tails--------
# ----------------------------------

# random_heads_tails = random.randint(0,1)
# print(random_heads_tails)

# if random_heads_tails == 0 : print("heads")
# else: print('Tails')


# ----------------------------------
# --------------Lists---------------
# ----------------------------------


my_friends = ["Andres", "Vova", "Fabio"]
another_friend_name = "Ale"
my_friends.append(another_friend_name)
# print(len(my_friends))


random_friend = random.randint(0, len(my_friends)-1)
# print(random_friend)
# print(my_friends[random_friend])


# Another option
# Get one item from a list 
# random.choice(my_friends)

# countries_i_have_been_america = ["Chile", "Argentina", "Peru", "Mexico", "EEUU", "Panama", "Brasil"]


# joint_list =[countries_i_have_been_america, my_friends]
# print(joint_list[1][0])



# ---------------------------------------------------------
# --------------Rock paper and scissors game---------------
# ---------------------------------------------------------


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


alternatives = [rock, paper, scissors]
random_number_computer = random.randint(0, len(alternatives) - 1)

your_answer = int(input("What do you choose? Type 0 for rock, 1 for Paper and 2 for scissors.\n"))
computer_answer = alternatives[random_number_computer]

if(your_answer >= 0 and your_answer <= 2):
    my_answer_display = alternatives[your_answer]
    print("My answer", my_answer_display)
    print("Computer answer", computer_answer)


# 0 Rock wins agains scissors 
# 1 paper wins against rock
# 2 Scissors wins against paper

# 2 beats 1 
# 1 beats 0
# 0 beats 2

# print(your_answer)


if(your_answer >= 3): print("Please select a valid number (0-2)")
elif(your_answer == 0 and random_number_computer == 2) : print("You win")
elif(random_number_computer == 0 and your_answer == 2) : print("You lose")
elif(your_answer > random_number_computer) : print("You win")
elif(random_number_computer > your_answer) : print("You lose")
elif(your_answer == random_number_computer): print("Its a draw")






# if(your_answer == 0):
#     if(random_number_computer == 0): print("draw")
#     if(random_number_computer == 1): print("Computer wins")
#     if(random_number_computer == 2): print("You win")
# elif(your_answer == 1):
#     if(random_number_computer == 1): print("duece")
#     if(random_number_computer == 2): print("Computer wins")
#     if(random_number_computer == 0): print("You win")    
# elif(your_answer == 2):
#     if(random_number_computer == 2): print("duece")
#     if(random_number_computer == 0): print("Computer wins")
#     if(random_number_computer == 1): print("You win")            


