# Functions 

# def greet(person_name):
#     print(f"Hello {person_name}!")

# greet("Haim")    


# Calculate how many weeks we have left 

def life_in_weeks(birth_year, current_year, years):
    age =  current_year -birth_year
    years_left = years - age
    print("Years left", years_left)
    weeks_left = years_left * 52
    
    print(f"You have {weeks_left} weeks left")

# life_in_weeks(1993, 2025, 90 )  


# Keyword parameters  
life_in_weeks(years=90, birth_year=1993, current_year=2025 )    






# Love calculator exercise
def calculate_love_score(name1, name2):
    word1 = "true "
    word2 = "love"
    # t_times = 0
    # r_times = 0
    # u_times = 0
    # e_times = 0
    # l_times = 0
    # o_times = 0
    # v_times = 0
    # e_times = 0
    
    true_matches = 0
    love_matches = 0

    names = [name1, name2]
    joined_names = " ".join(names)

    for letter in joined_names :
  
        # if(letter in name1 == "t" or letter in name2 == "t"): 
        #     t_times += 1
        # elif(letter in name1 == "r" or letter in name2 == "r"):
        #     r_times += 1
        # elif(letter in name1 == "u" or letter in name2 == "u"):
        #     u_times += 1
        if letter in word1 : true_matches += 1
        if letter in word2 : love_matches += 1 
            # print("Letter is in the name1")
        # else: 
        #     print(letter) 
        # elif(letter in name1 == "l" or letter in name2 == "l"):
        #     l_times += 1
        # elif(letter in name1 == "o" or letter in name2 == "o"):
        #     o_times += 1
        # elif(letter in name1 == "v" or letter in name2 == "v"):
        #     v_times += 1
        # elif(letter in name1 == "e" or letter in name2 == "e"):
        #     e_times += 1
        # else: print("That letter is not in any of the names ")    
        # else: print("Not in the phrase") 
        #  Propably  abetter way would be to use index 
            
    # print(f"T ccurs {t_times} times")            
    # print(f"R occurs {r_times} times")            
    # print(f"U occurs {u_times} times")            
    print(f"True matches {true_matches} and Love matches {love_matches}, giving you a love score of {str(true_matches) + str(love_matches)} ")            
    # print(f"L occurs {l_times} times")            
    # print(f"O occurs {o_times} times")            
    # print(f"V occurs {v_times} times")            
    # print(f"E occurs {e_times} times") 
    
    
calculate_love_score("Anna Yeshurun", "Haim Yeshurun")   