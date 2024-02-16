from string import ascii_letters, digits, punctuation
import secrets

def generate_password(num_letters, num_digits, num_special_chars, length):
    charset = []
    charset.extend(secrets.choice(ascii_letters.upper()) for _ in range(num_letters))
    charset.extend(secrets.choice(ascii_letters.lower()) for _ in range(num_letters))
    charset.extend(secrets.choice(digits) for _ in range(num_digits))
    charset.extend(secrets.choice(punctuation) for _ in range(num_special_chars))

    if len(charset) > length:
        raise ValueError("The generated character set is larger than the desired password length")

    for _ in range(length - len(charset)):
        charset.append(secrets.choice(charset))

    random.shuffle(charset)

    return ''.join(charset)

num_letters = int(input(f"how many letters ? \n"))
num_digits = int(input(f"how many digits ? \n"))
num_special_chars = int(input(f"how many special characters ? \n"))
length = int(input(f"how long should the password be ? \n"))

print(generate_password(num_letters, num_digits, num_special_chars, length))
