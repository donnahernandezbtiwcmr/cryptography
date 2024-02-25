from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    cipher_suite = Fernet(key)
    encrypted_message = cipher_suite.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    cipher_suite = Fernet(key)
    decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
    return decrypted_message

# Generate a key
generate_key()

# Load the key
key = load_key()

# Encrypt and decrypt the message
message = "Hello, World!"
encrypted_message = encrypt_message(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt_message(encrypted_message, key)
print("Decrypted message:", decrypted_message)
