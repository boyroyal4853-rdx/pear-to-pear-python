# Mathematical Algorithm

# Let n be the number.

# Store original number: temp = n
# Set rev = 0
# While n > 0:
# digit = n % 10
# rev = rev * 10 + digit
# n = n // 10
# If temp == rev, the number is a palindrome.

num = input("enter a number : ")
original_num = num
reverse_num = 0

while num > 0:
    digits = num % 10
    reverse_num = reverse_num * 10 + digits
    num = num // 10 

if original_num == reverse_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
