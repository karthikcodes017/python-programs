factorial_num = input("Type your number here: ")
factorial_num = int(factorial_num)

product = 1

for i in range(1, factorial_num + 1):
    product *= i
print (product)