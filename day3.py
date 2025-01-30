
# Starting with conditionals


# Checking odd or even numbers

# given_number = int(input("Give me a number!\n"))

# if given_number % 2 == 0:
    # print('Even!!')
# else:
    # print("Odd!!")    



# -------------------------------------------
# ----------Ticket calculator price----------
# -------------------------------------------

# print('Welcome to the rollercoster buddy!!!')
# customer_heigth = int(input("Whats your height?\n"))

# ticket_cost = int
# photo_cost = 3


# if(customer_heigth >= 120):
#     print('You can ride the rollercoster, have fun!!!')
#     age = int(input("whats your age?\n"))

# # First if statement 
#     if(age <= 12):
#         # print("Please pay 10 USD")
#         ticket_cost = 10
#     elif(age <= 18):
#         # print("Please pay 20 USD")
#         ticket_cost = 20
#     elif(age >= 45 and age <= 55):
#         ticket_cost = 0    
#     else:
#         # print("Please pay 60 USD")
#         ticket_cost = 60
    
#     wants_photos = input("Would you like photos? Yes or no\n")

# # Second if statement
#     if(wants_photos == "yes"):

#         ticket_cost += photo_cost

#     if(ticket_cost == 0): 
#         print("Your total bill would be free")
#     else:  
#         print(f"Your total bill would be {ticket_cost}")    
   
# else:
#     print("Sorry, you are not tall enought yet!")




# ----------------------------------
# ----------Pizza delivery----------
# ----------------------------------

# Welcome to Python Pizza Deliveries!
# What size pizza do you want? S, M or L: L
# Do you want pepperoni on your pizza? Y or N: Y
# Do you want extra cheese? Y or N: N
# Your final bill is: $28.


# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L: ")
# pizza_price = 0
# # small_pizza =

# pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")

# if(size == "s"): 
#     print("Small pizza") 
#     pizza_price = 15

# elif(size == "m"):
#     print("Medium pizza")
#     pizza_price = 20
# elif(size == "l"):
#     print("Large pizza")
#     pizza_price = 25
# else: print("Please select the correct pizza size to continue with your order...")    

# if(pepperoni == "y"):
#     if(size == "s" ):
#       pizza_price += 2
#       print('Add 2 dolars for the pepperoni')
#     else:
#       pizza_price += 3 
#       print('Add 3 dolars for the pepperoni')

# if(extra_cheese == "y"):
#    pizza_price += 1


# print(f"The {size} pizza you ordered with {pepperoni} and {extra_cheese}")
# print(f"Your final bill is {pizza_price}")
 

# --------------------------------------
# ----------Find the Treasure ----------
# --------------------------------------

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
first = input("You are at a crossroad, where do you want to go? Left or Right? \n").lower()

if(first == "left"):
    print("You've come to the lake. There is an island in the middle of the lake")
    second = input("Type 'wait' to wait for a boat. Type 'swim  to swim across\n ").lower()

    if(second == "wait"):
        print("there is a door you must open to continue, and basd on that decision your future will take a diffeent form")
        third = input("Please type the door. Can be 'Red', 'Blue' or 'Yellow'\n").lower()

        if(third == 'yellow'):
            print("You win!! Congratulations")

        elif(third == 'blue'):
            print('You have entered a room full of fire. Game Over')    
        else: 
            print("Game over")  
    else: 
        print("attacked by trout. Game Over.")    
    
else: 
    print("You have falled into a hole. Game over")



