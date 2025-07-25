#If Statement
num = -5
if num > 0:
    print("Positive Number")

# tell me condition to check if the given number is in range
# 10 - 20
num = 13
if num>=10 and num<=20:
    print(f"The given number {num} is in range") 

#Else Statement
num = 10
if num > 0:
    print("Positive Number")
else:
    print("Negative Number")

# vote app
age = 25
if age >=18:
    print("You Can Vote")
else:
    print("You Cannot Vote")   

#Elif Statements
marks = int(input("Enter Your Marks: "))
if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
else:
    print("FAIL")

# vote app with id card
has_id = False
age = int(input("Enter Your Age: "))
if age >=18:
    if has_id==True:
        print("You are Allowed To Voting Center")
    else:
        print("You Need An ID To Enter Voting Center")
else:
    print("You Cannot Vote")

#Match Statements
# Using match-case
age = 30

match age:
    case 0 | 1 | 2 | 3 | 4:
        category = "Toddler"
    case 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
        category = "Child"
    case _:
        category = "Adult"
print(category)

# Using with range()

age = int(input("Enter the age:"))
if age in (0,1,2,3,4):
   category = "Toddler"
elif age in range(5,13):
   category = "Child"
elif age in range(13,20):
   category = "Teenager"
elif age in range(20,27):
   category = "Young Adult"
else:
   category = "Adult"

print(category)  