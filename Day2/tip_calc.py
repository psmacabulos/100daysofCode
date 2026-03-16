print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? $"))

percentage = int(input("How much tip would you like to give? 10, 12, or 15?")) / 100

no_of_people = int(input("HOw many people to split the bill? "))

shared_tip = round((bill * percentage) / no_of_people, 2)

print(f"Each person should pay: ${shared_tip}")
