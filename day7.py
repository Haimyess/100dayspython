import random

# Later on, we could genrate random words form a library or something. 
word_list = ["tavi", "lisa", "millionaires", "travel", "happiness"]

# There is a word that we randomly geenrate
random_word =  random.choice(word_list)
print(random_word)

print("Guess the word!! Please choose a letter")
user_answer = input("Type bellow your answer\n")

if(user_answer in random_word ):
    print("True")
else: print("False")
# We show the quantity of letters as balnks 
# We need to guess it 
# Each time we choose a letter, the program checks if the letter selected is included in the word  
# If its corrects it adds it, prints it if there are more lettters to go, if not, you won!
# If its wrong, it adds a part of the body to the hangman. Lose a life (as many lifes as letter in th eword )
# We need to check if the wrong is the last or not
# If not, continue the game
# if it is, game over 

