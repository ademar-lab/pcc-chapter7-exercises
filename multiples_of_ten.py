# Ask users for a number
number = ""
while type(number) != int:
    number = input("Introduce a number: ")
    try:
        number = int(number)
    except ValueError:
        print("You have to introduce a number!")

# Is the number a multiple of 10?
if number % 10 == 0:
    print("Your number is a multiple of 10!")
else:
    print("Your number isn't a multiple of 10")