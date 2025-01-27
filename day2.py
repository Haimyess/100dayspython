
# Basic tip calculator with no conditionals

print('Welcome to the tip calculator!!')
total_bill = float(input('How much is the bill?\n'))
tip_percentage = int(input("How muchwould you like to give? 10, 12, or 15\n"))
people_splitting = int(input("How many people to split the bill?\n"))
tip_per_person = round(total_bill * (tip_percentage /100) /people_splitting, 2)
print(f"You will pay is {tip_per_person}\n")