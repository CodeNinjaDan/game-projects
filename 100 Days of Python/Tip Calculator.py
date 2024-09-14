print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? kshs "))
tip_percentage = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
tip = total_bill * (tip_percentage / 100)
total_bill += tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: kshs {final_amount}")
