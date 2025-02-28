import hashlib
import random
import string

# ASCII-Logo mit Titel "PASS HASH"
logo = r"""
$$$$$$$\   $$$$$$\   $$$$$$\   $$$$$$\        $$\   $$\  $$$$$$\   $$$$$$\  $$\   $$\ 
$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\       $$ |  $$ |$$  __$$\ $$  __$$\ $$ |  $$ |
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ /  \__|      $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |  $$ |
$$$$$$$  |$$$$$$$$ |\$$$$$$\  \$$$$$$\        $$$$$$$$ |$$$$$$$$ |\$$$$$$\  $$$$$$$$ |
$$  ____/ $$  __$$ | \____$$\  \____$$\       $$  __$$ |$$  __$$ | \____$$\ $$  __$$ |
$$ |      $$ |  $$ |$$\   $$ |$$\   $$ |      $$ |  $$ |$$ |  $$ |$$\   $$ |$$ |  $$ |
$$ |      $$ |  $$ |\$$$$$$  |\$$$$$$  |      $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ |  $$ |
\__|      \__|  \__| \______/  \______/       \__|  \__|\__|  \__| \______/ \__|  \__|
                              Secure Password Hasher v1.0
"""
print(logo)

def generate_password(length, complexity):
    chars = string.ascii_lowercase
    if complexity >= 2:
        chars += string.ascii_uppercase
    if complexity >= 3:
        chars += string.digits
    if complexity >= 4:
        chars += string.punctuation

    return "".join(random.choice(chars) for _ in range(length))

def hash_password(password, hash_type):
    if hash_type == "MD5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "SHA-256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif hash_type == "SHA-512":
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        return "Unsupported hash type!"

def save_hash_to_file(hash_value, mode):
    filename = "Shash1.txt" if mode == "selfmade" else "Chash.txt"
    with open(filename, "a") as file:
        file.write(hash_value + "\n")
    print(f"\nHash gespeichert in {filename} ✅")

# Benutzeroptionen
mode = input("Wähle Modus (SelfMade/Custom): ").strip().lower()
if mode == "selfmade":
    password = input("Gib dein Passwort ein: ")
else:
    length = int(input("Länge des Passworts: "))
    complexity = int(input("Komplexität (1=Einfach, 4=Max): "))
    password = generate_password(length, complexity)

# Passwort anzeigen
print("\nDein Passwort:")
print("*" * len(password))  # Versteckte Ausgabe

# Hashing
hash_type = input("Wähle Hash-Algorithmus (MD5/SHA-256/SHA-512): ").strip().upper()
hashed_pw = hash_password(password, hash_type)
print(f"\nGehashtes Passwort ({hash_type}): {hashed_pw}")

# Speichere den Hash in die passende Datei
save_hash_to_file(hashed_pw, mode)
