print("Welcome to the tip calculator") #welcome statement
print()
total_bill = float(input("What was the actual total bill? $")) #Total bill
print()
perc_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? ")) #percentage tip
print()
no_of_people = int(input("How many people to split the bill? ")) #Number of people to split the bill

actual_tip = (perc_tip/100) * total_bill #actual tip calculation
bill_plus_tip = total_bill + actual_tip #Actual tip added to bill
bill_per_person = bill_plus_tip/no_of_people #bill sharing
bill_per_person_round = round(bill_per_person, 2) #round function to round up bill to 2decimal place
print()
print(f"Each person should pay: ${bill_per_person_round}") #print

