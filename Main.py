import random
import string

def generate_password(num_letters, num_digits, num_special_chars, length):
    if num_letters + num_digits + num_special_chars > length:
        raise ValueError("The sum of specified characters exceeds the desired password length")
    
    password = []

    # Add at least one of each character type
    password.extend(random.sample(string.ascii_uppercase, num_letters))
    password.extend(random.sample(string.ascii_lowercase, num_letters))
    password.extend(random.sample(string.digits, num_digits))
    password.extend(random.sample(string.punctuation, num_special_chars))

    # Fill up the remaining length with random characters
    remaining_length = length - (num_letters + num_digits + num_special_chars)
    password.extend(random.sample(string.ascii_letters + string.digits + string.punctuation, remaining_length))

    # Shuffle the password
    random.shuffle(password)

    return ''.join(password)

def check_password_strength(password):
    # Check password strength based on commonly accepted criteria
    # You can customize this function based on your specific requirements
    # For example, you can check for length, presence of different character types, etc.
    # For simplicity, let's just check the length and presence of each character type
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    length = len(password)

    if length < 8 or not (has_upper and has_lower and has_digit and has_special):
        return "Weak"
    elif length < 12 or not (has_upper and has_lower and has_digit and has_special):
        return "Medium"
    else:
        return "Strong"

num_letters = int(input("How many uppercase and lowercase letters? "))
num_digits = int(input("How many digits? "))
num_special_chars = int(input("How many special characters? "))
length = int(input("How long should the password be? "))

password = generate_password(num_letters, num_digits, num_special_chars, length)
print("Generated Password:", password)
print("Password Strength:", check_password_strength(password))
