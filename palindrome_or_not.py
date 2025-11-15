palindrome_or_not = str(input("Input your string here: "))
reversed_string = palindrome_or_not [::-1]
if palindrome_or_not == reversed_string:
    print ("Your string is a palindrome!")
else:
    print ("Your string is not a palindrome :( ")