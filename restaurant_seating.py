# Ask the user how many people are in his dinner group
num_of_people = ""
while type(num_of_people) != int:
    num_of_people = input("How many people are going to have dinner tonight? ")
    try:
        num_of_people = int(num_of_people)
    except ValueError:
        print("You have to introduce a number!")

if num_of_people > 8:
    print("You'll have to wait for the table")
else:
    print("Your table is ready")