# find_largest_no_among_three.py
# . Write a Python program to find the largest number among three numbers.

# . take input form user x, y, z
# . compare x with y and z
# . compare y with x and z  
# . compare z with x and y
# . use if else state ment 
# . print the largest number

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

if x >y and x > z:
    print("The largest number is:", x)
elif y > x and y > z:
    print("The largest number is:", y)          
else:  
     print("The largest number is:", z) 

