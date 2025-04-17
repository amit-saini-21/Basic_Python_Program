import re
import random
import string

def check_password_strength(password):
    if len(password) < 8:
        print("❌ Weak Password! It should be at least 8 characters long.")
        return

    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()_+={};:<>,.?/-" for char in password)

    strength_score = has_lower + has_upper + has_digit + has_special

    if strength_score == 4:
        print("✅ Strong Password! 🔥")
    elif strength_score == 3:
        print("⚠️ Medium Strength. Try adding numbers, uppercase letters, and symbols.")
    else:
        print("❌ Weak Password! Use a mix of uppercase, lowercase, numbers, and special characters.")

def generate_password(length=12):
    if length < 8:
        print("⚠️ Password should be at least 8 characters for better security.")
        return
    
    # Ensure at least one of each required type
    password_chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()_+={};:<>,.?/-")
    ]

    # Fill the rest randomly
    password_chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length - 4)

    # Shuffle to avoid patterns
    random.shuffle(password_chars)
    
    password = ''.join(password_chars)
    print(f"🔐 Your Secure Password: {password}")

def main():
    print("\n🔒 Welcome to Password Manager!")
    print("1️⃣ Check Password Strength")
    print("2️⃣ Generate a Strong Password")
    
    choice = input("Enter your choice (1/2): ").strip()

    if choice == "1":
        password = input("Enter your password: ").strip()
        check_password_strength(password)
    elif choice == "2":
        try:
            length = int(input("Enter desired password length (minimum 8): "))
            generate_password(length)
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
    else:
        print("❌ Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
