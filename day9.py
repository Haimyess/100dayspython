# Dictionaries --> Like objects in javasript 

books_qtty_cover = {
    "paperback" : 30,
    "hardback" : 20
}

# print(books_qtty_cover["paperback"])



# -----------------------------------------
# -----------Grading Program---------------
# -----------------------------------------


# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, score in student_scores.items():
    print(student, score)   
       
    if score >= 91 and score <= 100 : student_grades[student] = "Outstanding"
    elif score >= 81 and score <= 90 : student_grades[student] = "Exceeds Expectations"
    elif score >= 71 and score <= 80 : student_grades[student] = "Acceptable"
    elif score <= 70 : student_grades[student] = "Fail"



print(student_grades)

travel_log = {
    "France" :{
        "cities_visited" :  ["Paris", "Lille", "Dijon"],
        "total_visits" : 12
    },

    "Germany" : {
        "cities_visited" : ["Hamburg", "Stuttgart", "Berlin"],
        "total_visits" : 5

         
     } 
}


# Sttutgard
print("Sttutgard?",  travel_log["Germany"]["cities_visited"][1] )

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][0])


# -----------------------------------------
# -----------Blind Auction---------------
# -----------------------------------------