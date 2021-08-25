# Store a list of toppings
toppings_available = ["pepperoni", "onions", "mushrooms", 
    "sausage", "extra cheese"]

# Ask users the toppings they want on their pizza
active = True
while True:
    topping = input("\nWhat is the topping that you want on your pizza?"
        "\nEnter 'quit' to finish the program ")

    if topping == "quit":
        break
    elif topping in toppings_available:
        print(f"\n\t{topping.title()} is being added to your pizza!")
    elif topping == "quit":
        break
    else:
        print(f"\nSorry, we don't have {topping.title()} available")

    answer = input("\nDo you want to add an extra topping? ")
    if answer == "no":
        break

# Finish the program
print("\n\tYour pizza is ready!")