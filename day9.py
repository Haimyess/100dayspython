
import os


# Dictionaries --> Like objects in javasript 

# books_qtty_cover = {
#     "paperback" : 30,
#     "hardback" : 20
# }

# print(books_qtty_cover["paperback"])



# -----------------------------------------
# -----------Grading Program---------------
# -----------------------------------------


# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}

# for student, score in student_scores.items():
#     print(student, score)   
       
#     if score >= 91 and score <= 100 : student_grades[student] = "Outstanding"
#     elif score >= 81 and score <= 90 : student_grades[student] = "Exceeds Expectations"
#     elif score >= 71 and score <= 80 : student_grades[student] = "Acceptable"
#     elif score <= 70 : student_grades[student] = "Fail"



# print(student_grades)

# travel_log = {
#     "France" :{
#         "cities_visited" :  ["Paris", "Lille", "Dijon"],
#         "total_visits" : 12
#     },

#     "Germany" : {
#         "cities_visited" : ["Hamburg", "Stuttgart", "Berlin"],
#         "total_visits" : 5

         
#      } 
# }


# Sttutgard
# print("Sttutgard?",  travel_log["Germany"]["cities_visited"][1] )

# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][0])


# -----------------------------------------
# -----------Blind Auction---------------
# -----------------------------------------


bid_people = {}
is_more_people = True


def add_auction(person, amount) :
    bid_people[person] = amount
  


def check_highest_bid(auctionaires) :
    max_bid = 0
    max_bidder_name = ""
    for person, bid in auctionaires.items() :
        # print(person, bid)
        if int(bid) > max_bid :
            max_bidder_name = person
            max_bid = bid
        
    print(f"The highest bidder was {max_bidder_name} with a bid of {max_bid}")
        # max_bidder.append(bid_people[max_bidder_name]) 


while is_more_people :

    print("Welcome to the Auction!")
    auctionare_name = input("Whats your name?\n")
    bid_amount = int(input("whats your bid?\n"))
    add_auction(auctionare_name, bid_amount)
    are_more_bidders = input("Is there any more auctionares?\n")

    if are_more_bidders == "no":
        is_more_people = False

    os.system('cls')


check_highest_bid(bid_people)

# print(bid_people)

# print(f"The max bid was made by {max_bidder[0][0]} and the amount was {max_bidder[0][1]}")



# if yes,
#  continue, 
# clear the conole 



# if not
#  loop the dictorioany 
# check the highest bid
# show result 

