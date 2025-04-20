
from cryptography.fernet import Fernet

def cript_password(password: str):
    encrypted_message = cipher.encrypt(password.encode())
    return encrypted_message

def decrypt_password(encrypted_message: bytes):
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()