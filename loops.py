# default step is 1
for i in range(1,10):
    print(i)

# odd numbers in between 1 to 10
for i in range(1,10,2):
    print(i)

# even numbers in between 1 to 10
for i in range(5,100,5):
    print(i)

# default step is 1
# specify -1 for reverse order
for i in range(10,1,-1):
    print(i)

# break - terminate loop, even if the condition hasn't finished
for i in range(10):
    if i == 5:
        break # loop will terminate here
    print(i)

# continue - skip the current Iteration
for i in range(10):
    if i == 5:
        continue # skip this iteration
    print(i)

# pass - placeholder that does nothing
if 5<9:
    pass

# while demo
count = 1
while count <=5:
    print("Count", count)
    count += 1

# If you don't know number of Iterations before hand, use while loop
# password validation
password = "secret"
user_password = ""

while user_password != password:
    user_password = input("Enter Password: ")
print("Access Granted")

# Drink Water Till Bottle is Empty
water_in_bottle = 10
print("Drinking Water")

while water_in_bottle > 0:
    print("Took A Sip, Remaining Sip:", water_in_bottle-1)
    water_in_bottle -= 1

import random
# Assume the correct OTP is already stored in a variable
otp = random.randint(1000,9999)
print(otp)

# while loop
# After 3 incorrect attempts, display
# Maximum attempts done, try after 24 Hours
count = 3

while count>0:

    # condition
    # If the OTP entered is not 4 digits, display
    # OTP Must be 4 digit number only
    user_otp = int(input("Enter OTP: "))

    if len(str(user_otp))!=4:
        print("OTP Must be 4 digit number only")
    # If the OTP is correct, display:
    # Correct OTP - Success
    if otp == user_otp:
        print("Correct OTP")
        break
    count = count - 1
    
    # last msg to display
else:
    print("max attempt done, try after 24 Hours")