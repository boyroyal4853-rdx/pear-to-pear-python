# firstly we will take input from the user
# and then we will check whether the number is even or odd 
# using the modulus operator (%).
# If the number is divisible by 2 (i.e., num % 2 == 0), 
# then it is an even number; otherwise, it is an odd number.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an even number.")
else:
    print(num, "is an odd number.")
