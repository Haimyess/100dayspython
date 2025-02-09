import random

# Later on, we could genrate random words form a library or something. 
word_list = ["tavi", "lisa", "millionaires", "travel", "happiness"]


# There is a word that we randomly geenrate
random_word =  random.choice(word_list)
# lifes = len(random_word)
lifes = 5
# print(lifes -1)
# print("Lifes", lifes)
print(random_word)

# placeholder = ""
# word_length = len(random_word)

# for position in range(word_length):
#     placeholder += "_"
# print(placeholder)

# while lifes >= 0:
#     lifes -= 1
#     print("Hello")

# if(user_answer in random_word ):
#     print("True")
# else: print("False")


word_arr = []



# while lifes > 0 :

#     print("Guess the word!! Please choose a letter")
#     user_answer = input("Type bellow your answer\n").lower()


#     for letter in random_word:
#         if letter == user_answer:
#                 word_arr.append(letter)
            
        
#         else:
#                 word_arr.append("_") 
               

#     lifes -= 1
#     print("Ramaining lifes", lifes)




# word_arr_joined = " ".join(word_arr)
# print(word_arr_joined)

# print("".join(word_arr))

# name_guess = "elefante"
display_word = ["_"]* len(random_word)

while lifes > 0 and "_" in display_word:
    final_word = " ".join(display_word)
    print( final_word)             
    letter_provided = input('Guess if the letter is in the word \n')


    for letter_index in range(len(random_word)):
        if  letter_provided == random_word[letter_index]:
            display_word[letter_index] =  letter_provided
        

    if  letter_provided not in random_word:
        lifes -= 1 
        print('Remaining lifes', lifes)


    if "_" not in display_word: 
        print("Congrats!!! You won!!")
        print(final_word)
    if lifes == 0:   print("Game Over") 
                 


            

# We show the quantity of letters as balnks 
# We need to guess it 
# Each time we choose a letter, the program checks if the letter selected is included in the word  
# If its corrects it adds it, prints it if there are more lettters to go, if not, you won!
# If its wrong, it adds a part of the body to the hangman. Lose a life (as many lifes as letter in th eword )
# We need to check if the wrong is the last or not
# If not, continue the game
# if it is, game over 

