import random


# fruits = ["Strawberry", "Banana", "Dates"]

# for fruit in fruits:
#     print(fruit)


# bills = [10,25,32,46]
# total_bills = sum(bills)
# print(total_bills)


# ---------------------------------------------------
# --------------------Highest score------------------
# ---------------------------------------------------

# student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
# print("with the built in function", max(student_scores))

# highest_score = 0
# current_score = 0

# for score in student_scores:
#         if(highest_score < score):
#             highest_score = score   


# print("With my code", highest_score)             

# total = 0
# for number in range(1, 101):
#       total += number

# print(total)



# ---------------------------------------------------
# ------------------FizzBuzz Game--------------------
# ---------------------------------------------------


# fizzbuzz_list = []

# for item in range(1, 101):
#     if item % 5 == 0 and item % 3 == 0: fizzbuzz_list.append("FizzBuzz")
#     elif item % 3 == 0: fizzbuzz_list.append("Fizz")
#     elif item % 5 == 0: fizzbuzz_list.append("Buzz")
#     else: fizzbuzz_list.append(item)  

# print(fizzbuzz_list)          




# ---------------------------------------------------------------
# ------------------Random password generator--------------------
# ---------------------------------------------------------------

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print(f"I want my password with {nr_letters} letters, {nr_symbols} symbols, and {nr_numbers} numbers ")


random_pass = []

random_number = random.choice(numbers)
print(random_number)

# Get number 
# Loop the list based on the number

for number in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    random_pass.append(random_number)

for symbol in range(1, nr_symbols + 1 ):
    random_symbol = random.choice(symbols)
    random_pass.append(random_symbol)

for letter in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    random_pass.append(random_letter)


# Each time get a difrent number 
# Add them to a string 
# 



print(f"Your new password is {random_pass}")


