num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
num_3 = int(input("Enter the third number: "))
if num_1 > num_2  and num_3:
    greatest = num_1
elif num_2 > num_1 and num_3:
    greatest = num_2
elif num_3 > num_1 and num_2:
    greatest = num_3

print (f"The greatest number is {greatest}")