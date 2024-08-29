import random
import string

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    """Generate a random password.

    Args:
        length (int): Length of the password.
        use_uppercase (bool): Whether to include uppercase letters.
        use_numbers (bool): Whether to include numbers.
        use_special_chars (bool): Whether to include special characters.

    Returns:
        str: Generated password.
    """
    # Define possible characters for the password
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to run the password generator."""
    print("Password Generator")

    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Length must be an integer.")
        return

    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == 'yes'

    if length <= 0:
        print("Length must be a positive integer.")
        return

    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
