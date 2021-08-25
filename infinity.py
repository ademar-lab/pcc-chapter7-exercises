# This loop never ends
# Press Ctrl-C to interrupt the program
x = 0
while True:
    x += 1
    if x % 1000 == 0:
        print(x)