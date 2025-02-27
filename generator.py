import hashlib
import random
import string

def generate_password(length, complexity, word_tip=False):
    chars = ""
    if complexity == 1:
        chars = string.ascii_lowercase
    elif complexity == 2:
        chars = string.ascii_letters
    elif complexity == 3:
        chars = string.ascii_letters + string.digits
    elif complexity == 4:
        chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    
    if word_tip and length > 4:
        tip_length = min(4, length // 2)
        print(f"Word Tip: {password[:tip_length]}...")
    
    return password

def hash_password(password, hash_type):
    if hash_type == "MD5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "SHA-256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif hash_type == "SHA-512":
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        return "Unsupported hash type!"

def main():
    print("Password Generator")
    mode = input("Choose mode (SelfMade/Custom): ")
    
    if mode.lower() == "selfmade":
        password = input("Enter your password: ")
    elif mode.lower() == "custom":
        length = int(input("Enter password length: "))
        complexity = int(input("Choose complexity (1-4): "))
        word_tip_choice = input("With a word tip? (yes/no): ").strip().lower()
        word_tip = word_tip_choice == "yes"
        password = generate_password(length, complexity, word_tip)
        print("Generated password: ", "*" * len(password))  # Versteckt die Ausgabe
    else:
        print("Invalid mode!")
        return
    
    hash_type = input("Choose hash type (MD5/SHA-256/SHA-512): ")
    hashed_password = hash_password(password, hash_type.upper())
    print("Hashed Password: ", hashed_password)

if __name__ == "__main__":
    main()
