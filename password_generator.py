import random
import string
import sys

# Keep asking until user enters a valid password length
while True:
    try:
        user_input = int(input("How long the password should be? (min 4): "))
        if user_input >= 4:
            break
        else:
            print("Password can't be less than 4")
    except ValueError:
        # Handles non-numeric input
        print("Enter a valid number")






container = ""        # Stores all allowed characters
types_count = 0       # Counts how many character types are selected

upper = input("Include uppercase letters? (y/n): ")
if upper.lower() == 'y':
    container += string.ascii_uppercase
    types_count += 1  # Track selected type

lower = input("Include lowercase letters? (y/n): ")
if lower.lower() == 'y':
    container += string.ascii_lowercase
    types_count += 1

num = input("Include numbers? (y/n): ")
if num.lower() == 'y':
    container += string.digits
    types_count += 1

char = input("Include special characters (!@#$%^&*)? (y/n): ")
if char.lower() == 'y':
    container += "!@#$%^&*"
    types_count += 1

# If no character type is selected, exit the program
if container == "":
    print("You must select at least one character. Exiting Program!")
    sys.exit()  #  Immediately stops the program execution





# Randomly pick characters from the container
password_list = [random.choice(container) for _ in range(user_input)]

# Convert list of characters into a single string
password = "".join(password_list)

print(f"Password is: {password}")






# Check password strength using length and variety of characters
password_length = len(password)

if password_length < 8 or types_count == 1:
    print("Your Password strength: Weak ⚠️")
elif password_length < 12 or types_count == 2:
    print("Your Password strength: Medium")
elif password_length < 16 or types_count == 3:
    print("Your Password strength: Strong")
else:
    print("Your Password strength: Very Strong ✅")




while True:
    #Ask if user wants another password
    generate_again = input("\nGenerate another password? (y/n): ")
    if generate_again.lower() == 'y':
        password_list = [random.choice(container) for _ in range(user_input)]
        password = "".join(password_list)
        print(f"New Password: {password}")

    else:
        break






