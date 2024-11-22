import random
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    if length < 1:
        print("Password length must be at least 1.")
        return None

    # Base character set (lowercase letters)
    character_pool = list(string.ascii_lowercase)

    # Add uppercase letters if chosen
    if use_uppercase:
        character_pool.extend(string.ascii_uppercase)

    # Add digits if chosen
    if use_digits:
        character_pool.extend(string.digits)

    # Add special characters if chosen
    if use_special:
        character_pool.extend(string.punctuation)

    # Ensure the pool isn't empty
    if not character_pool:
        print("No characters available to generate a password!")
        return None

    # Generate the password
    password = ''.join(random.choices(character_pool, k=length))
    return password

def main():
    print("--- Password Generator ---")

    try:
        # Get user input for password length
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        return

    # Ask for password complexity preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
    use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    use_special = input("Include special characters? (y/n): ").strip().lower() == 'y'

    # Generate and display the password
    password = generate_password(length, use_uppercase, use_digits, use_special)
    if password:
        print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
