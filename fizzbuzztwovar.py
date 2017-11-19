def fizzbuzz1(num1):
    if int(num1) % 3 == 0 and int(num1) % 5 == 0:
        print("FizzBuzz")
    elif int(num1) % 5 == 0:
        print("Buzz")
    elif int(num1) % 3 == 0:
        print("Fizz")
    else:
        pass

def fizzbuzz2(num1, num2):
    result = str(fizzbuzz1(num1)) + "\n"
    result += str(fizzbuzz1(num2)) +"\n"
    return result

int_num = input("How many integers do you want to use? (1 or 2) \n> ")

if int_num == str(1):
    num1 = input("Please enter a positive integer.\n > ")
    fizzbuzz1(num1)
else:
    num1, num2 = eval(input("Please enter two positive integers, comma seperated.\n > "))
    fizzbuzz2(num1, num2)