print ("Calculator")
x = int(input("Type first no. here: "))
y = int(input("Type second no. here: "))
operation = input("Select your operation (+, -, *, /): ")
result = None
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y 
elif operation == '/':
    if y == 0:
        result = "Error"
    else:
        result = x / y

print (f"The result of {x} {operation} {y} is: {result} ")

    
    