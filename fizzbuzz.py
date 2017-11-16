print("Press q to quit")
quit = False

while quit is False:
    in_val = input("Please enter a positive integer.\n > ")
    if in_val is 'q':
        quit = True
    elif int(in_val) % 3 == 0 and int(in_val) % 5 == 0:
        print("FizzBuzz")
    elif int(in_val) % 5 == 0:
        print("Buzz")
    elif int(in_val) % 3 == 0:
        print("Fizz")
    else:
        pass
