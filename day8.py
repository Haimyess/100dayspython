# Functions 

# def greet(person_name):
#     print(f"Hello {person_name}!")

# greet("Haim")    


# Calculate how many weeks we have left 

# def life_in_weeks(birth_year, current_year, years):
#     age =  current_year -birth_year
#     years_left = years - age
#     print("Years left", years_left)
#     weeks_left = years_left * 52
    
#     print(f"You have {weeks_left} weeks left")

# life_in_weeks(1993, 2025, 90 )  


# Keyword parameters  
# life_in_weeks(years=90, birth_year=1993, current_year=2025 )    






# Love calculator exercise
# def calculate_love_score(name1, name2):
#     word1 = "true"
#     word2 = "love"
#     t_times = 0
#     r_times = 0
#     u_times = 0
#     e_times = 0
#     l_times = 0
#     o_times = 0
#     v_times = 0
  

    # I tough we needed to count how many letter of each word they were in the names 
    
#     true_matches = 0
#     love_matches = 0

#     names = [name1.lower(), name2.lower()]
#     joined_names = "".join(names)

#     for letter in joined_names :
  
#         if letter in word1 : 
#             true_matches += 1
#         if letter in word2 : 
#             love_matches += 1 

        
#         if(letter == "t"):
#             t_times += 1
#         elif(letter == "r"):
#                 r_times += 1    
#         elif(letter == "u"):
#                 u_times += 1    
#         elif(letter == "e"):
#                 e_times += 1    
#         elif(letter == "l"): 
#             l_times += 1    
#         elif(letter == "o"):
#                 o_times += 1    
#         elif(letter == "v"):
#                 v_times += 1    
              
             
#     print(f"True matches {true_matches} and Love matches {love_matches}, giving you a love score of {str(true_matches) + str(love_matches)} ")            
#     print(f"T times {t_times},  R times {r_times}, U times {u_times}, E times {e_times}. L times {l_times}, O times {o_times}, V times {v_times}")            
 
    
    
# calculate_love_score("Anna Yeshurun", "Haim Yeshurun")   




# Ceasar Cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

continue_quest = True

# decipher function
def encrypt(msg, number_positions, mode ):
    
      encoded_msg = ""
      
      for letter in msg:

        if letter not in alphabet : encoded_msg += letter
        else : 
         index_alph =  alphabet.index(letter) + number_positions if mode  == 'encode' else alphabet.index(letter) - number_positions
      
        # if mode  == 'encode' :
        #     index_alph = alphabet.index(letter) + number_positions
        # if mode == 'decode' :    
        #     index_alph = alphabet.index(letter) - number_positions
           
        
         final_letter = alphabet[index_alph % len(alphabet)]
            
         encoded_msg += final_letter
  
  
      return encoded_msg
                  


while  continue_quest:
  direction = input("type 'encode' to encrypt and 'decode' to decrypt\n").lower()
  text = input("Type your message\n").lower()
  shift = int(input("Type the shift number\n"))

  msg = encrypt(text, shift, direction)  

  print(f"You {direction}d message is", msg)
                  
  restart = input("Do you want to continue?\n").lower()

 


  if restart == "no" :
    continue_quest = False
    print("Have a good one!")
  
  




# ask for question