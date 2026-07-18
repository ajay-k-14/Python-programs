from datetime import datetime

print("Age Calculator")
print("Enter your birth year:")
age=int(input())
current_year = datetime.now().year
print("Your age is:", current_year - age)