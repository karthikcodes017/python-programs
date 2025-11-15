number = input("Type your number here: ")
number = int(number)
remainder = number % 2

if remainder == 0:
    print ("Your number is Even!")
else:
    print ("Your number is Odd!")