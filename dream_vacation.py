# Create a poll where you ask users their dream place to visit 
dream_places = {}
active = True
while active:
    name = input("What is your name?"
        "\nEnter \"quit\" to finish the program ")
    if  name == "quit":
        break
    dream_place = input("If you could visit one place in the world, "
        "where would you go?"
        "\nEnter \"quit\" to finish the program ")
    if  dream_place == "quit":
        break
    dream_places[name.title()] = dream_place
    continue_poll = input("Do you want to learn other people take the poll?"
        "\nPress \"n\" if you don't ")
    if continue_poll == "n":
        active = False

# Finish the poll
print("\nThese are the results from the poll:")
for name, place in dream_places.items():
    print(f"\t{name.title()}: {place.title()}")