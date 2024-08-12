import string
import random

def generate_password(length=40, use_special=True, use_numbers=True, use_uppercase=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def get_user_preferences():
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    return use_special, use_numbers, use_uppercase

def main():
    use_special, use_numbers, use_uppercase = get_user_preferences()
    password = generate_password(use_special=use_special, use_numbers=use_numbers, use_uppercase=use_uppercase)
    print(f"Generated password: {password}")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
