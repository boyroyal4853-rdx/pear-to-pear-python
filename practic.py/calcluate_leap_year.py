# Normal year me 365 days hote hain, lekin leap year me 366 days hote hain.

# Leap year me February 28 din ki jagah 29 din ki hoti hai.

# Leap Year ke Rules

# Koi year leap year hoga agar:

# Year 400 se divisible ho → Leap Year
# Agar 400 se divisible nahi hai, lekin 100 se divisible hai → Not a Leap Year
# Agar 100 se divisible nahi hai, lekin 4 se divisible hai → Leap Year
# Baaki sab cases me → Not a Leap Year


year = input("Enter a year: ")

if year % 4 == 0:
    print(year, "is a leap year.")

elif year % 400 == 0:
    print(year, "is a leap year.")

elif year % 100 == 0:
    print("Not a Leap Year")

else:
    print("Not a Leap Year")