# Store some sandwich orders in a list
sandwich_orders = ["smoked meat", "pastrami", "tuna", "pastrami", 
    "grilled chicken", "pastrami", "vegetarian"]
finished_sandwiches = []

# Prepare the ordered sandwiches
while sandwich_orders:
    in_process_sandwich = sandwich_orders.pop()
    if in_process_sandwich != "pastrami":
        print(f"\tThe {in_process_sandwich} sandwich is being prepared")
        finished_sandwiches.append(in_process_sandwich)
    else:
        print(f"\tSorry, we run out of pastrami")

print("\nThe sandwices are ready! Here they are:")
for sandwich in finished_sandwiches:
    print(f"\tA {sandwich} sandwich")