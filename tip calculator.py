print("Welcome to my tip calculator")
bill = float(input("what was tottal bill ? $"))
tip = int(input("how much tip would you like to give? 10, 15, 20? "))
people = int(input("how many people to split the bill ? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"each person should pay ${final_amount} ")