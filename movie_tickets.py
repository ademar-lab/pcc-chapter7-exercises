# Tell users the price of their movie ticket based on their age
while True:
    active = input("\nDo you wnat to know the price of of your movie ticket?"
    "\nType \"n\" if you don't ")
    if active == "n":
        break

    #Ask the users their age
    age = ""
    while type(age) != int:
        age = input("What is your age? ")
        try:
            age = int(age)
        except ValueError:
            print("You have to introduce a number!")
    
    #Print the cost of the ticket
    if age < 3:
        print("\nYour ticket is free!")
    elif age < 12:
        print("\nYour ticket costs $10")
    else:
        print("\nYour ticket costs $15")