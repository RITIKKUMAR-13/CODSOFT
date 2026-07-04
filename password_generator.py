import random
import string

def generate_password(length):
    # सभी characters: letters + digits + special symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    # random choice से password बनाओ
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    length = int(input("Enter password length: "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
