import random 
import string

def generate_password(password_length, use_symbols):
    material = string.ascii_letters + string.digits
    if use_symbols:
        material += string.punctuation
    
    return ''.join(random.choice(material) for _ in range(password_length))

while True:
    try:
        length = int(input("Enter the password length (8-32): "))
        symbols = input("Do you want to include symbols (Y/N): ").lower()
        if symbols == "y":
            use_symbols = True
        break
    except ValueError:
        print("Invalid input! Enter password length again (8-32): ")
        continue

password = generate_password(length, use_symbols)
print(f"Your password is: {password}")