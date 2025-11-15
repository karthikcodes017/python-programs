first_side = int(input("Type your first side here: "))
second_side = int(input('Type your second side here: '))
third_side = int(input('Type your third side here: '))

if first_side == second_side == third_side:
    print ('Your triangle is an equilateral triangle!')
    
elif first_side == second_side or second_side == third_side or first_side == third_side:
    
    print ('Your triangle is an isoceles triangle!')
else:
    print ('Your triangle is a scalene triangle!')